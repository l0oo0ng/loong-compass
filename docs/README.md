# 文档与安装排错

1. 核对当前运行时是否支持 Codex 插件和 Skill；未安装不等于仓库代码错误。
2. 市场入口是 `l0oo0ng/loong-prompt`，插件名是 `loong`，不能互换。
3. 本地目录包含空格时给路径加引号；不要提交用户级市场状态。
4. 插件载入失败时检查[插件清单](../plugins/loong/.codex-plugin/plugin.json)
   与[市场入口](../.agents/plugins/marketplace.json)中的相对路径。
5. 可选依赖缺失时报告其名称，不自行复制第三方插件源码。
6. 多代理能力不足时遵循能力边界，不伪造交叉审查。

[贡献政策](../CONTRIBUTING.md)包含既有本地校验说明。
[发布流程](release-process.md)规定版本来源和草稿验收；
[变更日志](../CHANGELOG.md)记录本轮文档变更，不推测过去未发布版本。
