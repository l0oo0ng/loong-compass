# Contributing to loong prompt

This is a personal project. Use GitHub Issues for bug reports, evidence-backed suggestions, and feature requests.

The maintainer does not grant direct write access. Pull requests are not the contribution channel for this repository and may be closed; a maintainer may convert a useful proposal into a change after review.

Please do not include credentials, tokens, passwords, private keys, user-level marketplace state, local absolute paths, or personal data in an issue. Reproduce problems with sanitized, minimal examples.

## Local validation

The validators require Python with `PyYAML==6.0.3`. Keep the virtual environment outside tracked files (the ignored `work/` directory is suitable). On Windows, force UTF-8 decoding:

```powershell
$repo = (Get-Location).Path
$venv = Join-Path $repo "work\loong-validate-venv"
& "$venv\Scripts\python.exe" -X utf8 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "$repo\plugins\loong\skills\loong"
& "$venv\Scripts\python.exe" -X utf8 "$env:USERPROFILE\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" "$repo\plugins\loong"
```

Before a push, follow the three-pass redaction gate in the skill's `references/software-engineering.md`. Do not print matched values in issue reports or logs.
