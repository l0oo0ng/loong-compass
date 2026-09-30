"""Validate repository documentation and build a versioned, allowlisted release."""
import argparse
import ast
import csv
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'docs/repository-standardization/release.json').read_text(encoding='utf-8'))


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def version():
    source = CONFIG['version_source']
    text = (ROOT / source['path']).read_text(encoding='utf-8')
    if source['kind'] == 'json':
        return json.loads(text)['version']
    if source['kind'] == 'python':
        for node in ast.parse(text).body:
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == source['key'] for t in node.targets):
                return ast.literal_eval(node.value)
        raise ValueError('Version constant missing')
    return text.strip()


def tracked():
    return [p.decode('utf-8') for p in git('ls-files', '-z').split(b'\0') if p]


def check():
    v = version()
    assert v == CONFIG['version'], 'Version source and release configuration disagree'
    tag = CONFIG['tag_prefix'] + v
    if os.environ.get('GITHUB_REF_TYPE') == 'tag':
        assert os.environ['GITHUB_REF_NAME'] == tag, 'Tag and version disagree'
    names = set(tracked())
    required = ['README.md', 'README.en.md', 'CHANGELOG.md', 'CHANGELOG.zh-CN.md',
                'CONTRIBUTING.md', 'SECURITY.md', 'docs/repository-standardization/RELEASE.md']
    for name in required:
        assert name in names, 'Required document missing: ' + name
    for name in required:
        content = (ROOT / name).read_text(encoding='utf-8')
        # Prior material remains verbatim in a clearly labelled history section.
        content = content.split('<!-- preserved-history -->', 1)[0]
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip('<>').split('#')[0]
            if not target or ':' in target or target.startswith('//'):
                continue
            path = (ROOT / name).parent / target
            relative = os.path.relpath(path, ROOT).replace('\\', '/')
            assert relative in names or any(p.startswith(relative.rstrip('/') + '/') for p in names), f'Broken link in {name}: {target}'
    # Only new/changed files are scanned; historical binaries are not reinterpreted.
    changed = git('diff', '--name-only', '-z', CONFIG['baseline'], 'HEAD').split(b'\0')
    for raw in changed:
        if not raw:
            continue
        name = raw.decode('utf-8')
        p = ROOT / name
        if not p.is_file():
            continue
        assert not ({'.venv', 'node_modules', 'local_data', '__pycache__'} & set(p.relative_to(ROOT).parts)), 'Generated/private path: ' + name
        assert not (p.name.startswith('.env') and not p.name.endswith('.example')), 'Local credentials file: ' + name
        text = p.read_bytes().decode('utf-8', errors='ignore')
        patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
        assert not any(re.search(pattern, text) for pattern in patterns), 'Potential secret in ' + name
    if CONFIG['kind'] == 'skill':
        skill = ROOT / 'skills/anti-defensive-business-writing/SKILL.md'
        body = skill.read_text(encoding='utf-8')
        assert body.startswith('---') and '\nname:' in body and '\ndescription:' in body
        assert (skill.parent / 'agents/openai.yaml').is_file()
        assert (skill.parent / 'references/review-checklist.md').is_file()
    print('PASS repository documentation, version and changed-file checks:', tag)


def build():
    check()
    out = ROOT / 'release_assets'
    out.mkdir(exist_ok=False)
    names = tracked()
    selected = [n for n in names if any(n == p or n.startswith(p.rstrip('/') + '/') for p in CONFIG['include'])
                and not any(n == p or n.startswith(p.rstrip('/') + '/') for p in CONFIG.get('exclude', []))]
    files = {}
    for name in selected:
        p = ROOT / name
        if p.is_symlink():
            raise ValueError('Release symlink requires explicit review: ' + name)
        data = p.read_bytes()
        if data.startswith(b'version https://git-lfs.github.com/spec/v1'):
            raise ValueError('Unrestored LFS resource: ' + name)
        files[name] = data
    assert files, 'Empty delivery'
    inventory = []
    for record in git('ls-tree', '-rz', 'HEAD').split(b'\0'):
        if record:
            meta, name = record.split(b'\t', 1)
            mode, kind, oid = meta.decode().split()
            inventory.append({'path': name.decode(), 'git_object': oid, 'type': kind, 'mode': mode})
    # Git object IDs describe repository contents; SHA256 below verifies delivered bytes.
    files['REPOSITORY_INVENTORY.json'] = json.dumps(inventory, ensure_ascii=False, indent=2).encode('utf-8')
    commit = git('rev-parse', 'HEAD').decode().strip()
    record = {'repository': CONFIG['repository'], 'version': version(), 'tag': CONFIG['tag_prefix'] + version(),
              'commit': commit, 'build_url': os.environ.get('GITHUB_SERVER_URL', 'https://github.com') + '/' + CONFIG['repository'] + '/actions/runs/' + os.environ.get('GITHUB_RUN_ID', 'local'),
              'checks': CONFIG['checks'], 'limitations': CONFIG['limitations'], 'kind': CONFIG['kind']}
    files['BUILD_RECORD.json'] = json.dumps(record, ensure_ascii=False, indent=2).encode('utf-8')
    files['ACCEPTANCE.md'] = ('# Candidate verification / 候选版验证\n\nCommit: `' + commit + '`\n\n'
        + 'Build record identifies the workflow; publication runs only after its required checks succeed.\n\n'
        + '## Executed checks / 检查命令\n\n' + '\n'.join('- `' + c + '`' for c in CONFIG['checks'])
        + '\n\n## Not covered / 未覆盖\n\n' + '\n'.join('- ' + s for s in CONFIG['limitations']) + '\n').encode('utf-8')
    files['QUICK_START.md'] = (ROOT / 'docs/repository-standardization/QUICK_START.md').read_bytes()
    table = io.StringIO(newline='')
    writer = csv.writer(table, lineterminator='\n')
    writer.writerow(['path', 'bytes', 'sha256'])
    for name, data in sorted(files.items()):
        writer.writerow([name, len(data), hashlib.sha256(data).hexdigest()])
    files['FILES_SHA256.csv'] = table.getvalue().encode('utf-8')
    archive = out / (CONFIG['repository'].split('/')[-1] + '-' + version() + '-' + CONFIG['kind'] + '.zip')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            assert not PurePosixPath(name).is_absolute() and '..' not in PurePosixPath(name).parts
            z.writestr(name, data)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for row in csv.DictReader(io.StringIO(z.read('FILES_SHA256.csv').decode('utf-8'))):
            data = z.read(row['path'])
            assert len(data) == int(row['bytes']) and hashlib.sha256(data).hexdigest() == row['sha256']
    for name in ['FILES_SHA256.csv', 'BUILD_RECORD.json', 'ACCEPTANCE.md', 'QUICK_START.md']:
        (out / name).write_bytes(files[name])
    for pattern in CONFIG.get('extra_artifacts', []):
        matches = list(ROOT.glob(pattern))
        assert matches, 'Required build output missing: ' + pattern
        for p in matches:
            (out / p.name).write_bytes(p.read_bytes())
    sums = '\n'.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name for p in sorted(out.iterdir()))
    (out / 'SHA256SUMS.txt').write_text(sums + '\n', encoding='utf-8')
    print('PASS delivery byte hashes and ZIP:', len(files), 'files')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['check', 'build'])
    args = parser.parse_args()
    check() if args.action == 'check' else build()
