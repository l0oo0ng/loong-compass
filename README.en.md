# Loong Compass · Evidence-First Task Orchestration

[简体中文](README.md) · [English](README.en.md)

**0.1.2-rc.1** · Codex plugin / Python checks

[![Repository checks](https://github.com/l0oo0ng/loong-compass/actions/workflows/repository.yml/badge.svg)](https://github.com/l0oo0ng/loong-compass/actions/workflows/repository.yml)

This repository provides the capabilities below. Current evidence and limitations are stated explicitly.

## Capabilities

| Capability |
|---|
| Facts, inferences and risk-scaled execution |
| Task review and execution boundaries |
| Portable plugin and marketplace manifests |

## Project structure

- [plugins](plugins)
- [scripts](scripts)
- [LICENSE](LICENSE)
- [docs](docs)

## Install and use

```text
codex plugin marketplace add l0oo0ng/loong-compass
codex plugin add loong@loong-prompt
```

[Quick start / 快速开始](docs/repository-standardization/QUICK_START.md)

## Development and verification

```text
python scripts/check_version.py
python -m unittest discover -s scripts -p "test_*.py"
```

## Downloads and releases

[Candidate v0.1.2-rc.1](https://github.com/l0oo0ng/loong-compass/releases/tag/v0.1.2-rc.1) · [All releases](https://github.com/l0oo0ng/loong-compass/releases) · [Actions](https://github.com/l0oo0ng/loong-compass/actions)

Candidate packages are published only after checks succeed. Before then, use the Actions page for status. Existing stable releases remain unchanged.

## Limits and security

- Host capabilities are required; package and version checks do not establish full live-agent behavioral acceptance.

Repository visibility and existing licenses are unchanged. No additional license is granted by this documentation.

[贡献 / Contributing](CONTRIBUTING.md) · [安全 / Security](SECURITY.md) · [发布流程 / Releases](docs/repository-standardization/RELEASE.md)
