"""Validate the plugin's release identity without changing any files."""
import argparse
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--tag")
args = parser.parse_args()
manifest = json.loads((root / "plugins/loong/.codex-plugin/plugin.json").read_text(encoding="utf-8"))
version = manifest["version"]
if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?", version):
    raise SystemExit("Invalid semantic version")
if manifest["name"] != "loong":
    raise SystemExit("Plugin invocation changed")
if args.tag and args.tag != "v" + version:
    raise SystemExit("Tag does not match manifest version")
marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
if "plugins/loong" not in json.dumps(marketplace):
    raise SystemExit("Marketplace no longer points to the plugin")
print("PASS plugin version " + version)
