# Loong Compass · 证据优先任务编排

[简体中文](README.md) · [English](README.en.md)

**0.1.2-rc.1** · Codex plugin / Python checks

[![Repository checks](https://github.com/l0oo0ng/loong-compass/actions/workflows/repository.yml/badge.svg)](https://github.com/l0oo0ng/loong-compass/actions/workflows/repository.yml)

本仓库提供以下能力，当前版本的验证范围与限制见下方说明。

## 功能概览

| 能力 |
|---|
| 事实、推断与风险分级 |
| 任务审查与执行边界 |
| 可移植插件与市场清单 |

## 项目结构

- [plugins](plugins)
- [scripts](scripts)
- [LICENSE](LICENSE)
- [docs](docs)

## 安装与使用

```text
codex plugin marketplace add l0oo0ng/loong-compass
codex plugin add loong@loong-prompt
```

[Quick start / 快速开始](docs/repository-standardization/QUICK_START.md)

## 开发与验证

```text
python scripts/check_version.py
python -m unittest discover -s scripts -p "test_*.py"
```

## 下载与发布

[Candidate v0.1.2-rc.1](https://github.com/l0oo0ng/loong-compass/releases/tag/v0.1.2-rc.1) · [All releases](https://github.com/l0oo0ng/loong-compass/releases) · [Actions](https://github.com/l0oo0ng/loong-compass/actions)

候选包仅在检查成功后发布；尚未发布时请查看 Actions 状态。既有稳定版保持不变。

## 能力边界与安全

- 需要宿主提供对应工具与多角色审查能力；本轮只验证包结构和版本，不声称真实 Agent 行为已全面验收。

仓库可见性和既有许可证保持不变；本文档不授予额外使用许可。

[贡献 / Contributing](CONTRIBUTING.md) · [安全 / Security](SECURITY.md) · [发布流程 / Releases](docs/repository-standardization/RELEASE.md)

<!-- preserved-history -->
<details>
<summary>原项目指南与历史说明（版本状态以本页上方为准）</summary>

# loong prompt

[English](README.en.md)

> English: A personal Codex plugin for evidence-first reasoning and risk-scaled execution.

`loong` 将第一性原理、角色审查、最强反方论证与独立交叉审查组织为任务流程。
简单、可逆任务保持简短；高影响任务要求明确证据、风险与执行边界。
当前插件版本以清单为准，不把文档整理视为新功能发布。

## 使用与安装

显式调用 `$loong`，或由支持的 Codex 运行时按任务选择。
工程变更先明确目标、现状、范围、验收、执行模式五项契约；
重要结论区分事实、推断、观点和未知。

沿用仓库既有安装方式（本轮未重新安装插件）：

```text
codex plugin marketplace add l0oo0ng/loong-prompt
codex plugin add loong@loong-prompt
```

本地开发可将第一条的仓库参数改为带引号的克隆目录。
仓库名、市场名与插件调用名保持不变。

## 依赖与运行限制

| 组件 | 定位 | 既有兼容记录 |
|---|---|---|
| Codex 插件运行时 | 必需，支持插件与 Skill | 本轮不重新安装 |
| andrej-karpathy-skills | 可选编码辅助 | 1.0.0 |
| superpowers | 可选编码辅助 | 6.2.0 |
| global-skill-router | 可选路由 | 缺失时内建门禁仍生效 |

复杂任务需要一个编排者和三个审查者，并进行第二轮交叉审查；
运行时不具备此能力时应停止并说明，不能假称完成多人审查。
缺少可选编码插件时保留内建约束并报告缺失。

## 结构与文档

- `plugins/loong/`：插件清单、Skill 和配套参考资料。
- `.agents/plugins/marketplace.json`：可移植的仓库级市场入口，应继续跟踪。
- [文档与安装排错](docs/README.md)
- [发布流程](docs/release-process.md) / [变更日志](CHANGELOG.md)
- [贡献政策](CONTRIBUTING.md)：个人维护，使用 Issues 提建议，不改变既有 PR 政策。

## 数据与许可

不提交凭据、用户级市场状态、私人路径和运行缓存。
提交前检查路径、内容及完整历史中的敏感信息，只输出命中位置，不输出秘密值。
仓库级相对路径市场清单与用户级私人配置必须区分。
[MIT License](LICENSE) 保持不变；第三方辅助插件不复制到本仓库。


</details>
