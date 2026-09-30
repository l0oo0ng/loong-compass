# 贡献与维护 / Contributing

本次仓库管理维护通过独立分支和 PR 进入默认分支；保留既有外部贡献政策。 / Repository maintenance uses branches and PRs; existing external contribution policies remain in force.

1. 读取相关源码与历史说明，限定变更范围。 / Read the relevant source and limit scope.
2. 运行 README 所列检查；不要用测试修改历史记录或真实服务。 / Run documented checks without changing historical data or live services.
3. PR 写明问题、变更、验证及未覆盖事项。 / Describe the change, evidence and limitations.
4. 检查成功后合并，标签与权威版本一致。 / Merge after checks pass; tags match the version source.

[发布流程 / Release process](docs/repository-standardization/RELEASE.md)

<!-- preserved-history -->
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
