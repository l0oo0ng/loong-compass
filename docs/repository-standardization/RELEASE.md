# 发布流程 / Release process

版本源 / Version source: `plugins/loong/.codex-plugin/plugin.json`。标签 / Tag: `v0.1.2-rc.1`。

1. 更新版本源、双语日志和 release.json。 / Update the version source, bilingual changelog and release metadata.
2. 通过 PR 执行 README 检查，再合并到原默认分支。 / Pass checks and merge the PR into the existing default branch.
3. 对合并提交打标签；标签任务再次检查并生成全新交付包。 / Tag the merge commit; tag checks build a fresh package.
4. 同一任务直接上传 GitHub Prerelease，不依赖 Actions artifact，不替换稳定版 Latest。 / Publish directly to a prerelease in the same job without Actions artifact storage or replacing stable Latest.
5. 下载附件复核 SHA256、ZIP 内清单和 BUILD_RECORD 提交。 / Download and verify hashes, ZIP manifest and build commit.

历史标签、授权与资料不覆盖；失败停止发布。 / Existing tags, licenses and archives are preserved; failures stop publication.

完整性区分：FILES_SHA256.csv 校验实际包内字节；REPOSITORY_INVENTORY.json 记录全部已跟踪路径的 Git 对象 ID，不将其宣称为原始资料的 SHA256。 / Package SHA256 verifies delivered bytes; repository inventory records Git object IDs, not raw-file SHA256.
