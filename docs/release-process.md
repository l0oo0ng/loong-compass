# 插件发布流程

唯一版本来源：`plugins/loong/.codex-plugin/plugin.json` 的 `version`。
当前清单基线为 0.1.1。市场入口引用插件目录，不新增重复版本字段。

SemVer：破坏兼容性升 MAJOR，新增兼容能力升 MINOR，兼容修复升 PATCH。
文档变更记 Unreleased；不得仅为本轮整理修改版本号。
发布标签必须是 `v<清单版本>`，已有标签不可覆盖。

## 验收

1. 校验插件清单、Skill 元数据、市场路径及双语 README 的安装命令。
2. 按 CONTRIBUTING 中的本地验证器检查；未安装的验证器明确记录。
3. 运行 `python scripts/check_version.py`；
   计划发版时用 `python scripts/check_version.py --tag v0.1.1` 校验标签。
4. 检查工作区和完整历史敏感信息；不复制用户私有环境或可选插件。
5. 在干净提交上记录 SHA，准备 Release 草稿。
6. 维护者另外批准后才能推送标签和正式发布。不得将草稿当成已安装兼容认证。

## 草稿内容

标题：loong v0.1.1；状态：草稿；目标：审核后的提交 SHA。
基线：当前插件清单 0.1.1；变更：中文主文、英文文档、导航与发布检查。
兼容记录及限制按 README 如实填写；本轮未重新执行安装。
安装地址仍为原市场入口。只链接源码，不伪造 skill.zip 或附件校验值。
