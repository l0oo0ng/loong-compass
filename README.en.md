# loong prompt

[简体中文](README.md)

`loong` is a personal Codex plugin for evidence-first reasoning and risk-scaled execution.
It combines first-principles decomposition, role-based review, strongest-counterargument
analysis and independent cross-review. Simple reversible tasks stay concise.

## Use and install

Invoke `$loong` explicitly or let a supported Codex runtime select the skill.
Project work starts with five fields: goal, current state, scope, acceptance and execution mode.
Distinguish facts, inferences, opinions and unknowns.

Existing installation commands are retained; installation was not repeated in this documentation pass:

```text
codex plugin marketplace add l0oo0ng/loong-prompt
codex plugin add loong@loong-prompt
```

For local development, replace the repository argument with a quoted clone directory.
The marketplace name and `$loong` invocation remain unchanged.

## Compatibility and limits

Optional coding companions: `andrej-karpathy-skills` (previously tested 1.0.0)
and `superpowers` (previously tested 6.2.0).
Without them, loong retains its internal constraints and reports unavailable companions.
The global-skill-router is optional; the plugin's own complexity gate remains active.

Complex tasks require an orchestrator, three independent reviewers and a second cross-review pass.
If the runtime cannot provide these capabilities, stop and report the limitation instead
of claiming that independent reviews occurred.

## Layout and maintenance

- `plugins/loong/`: plugin manifest, skill and reference documents.
- `.agents/plugins/marketplace.json`: portable repository-local marketplace metadata.
- [Documentation and troubleshooting](docs/README.md)
- [Release process](docs/release-process.md)
- [Changelog](CHANGELOG.md)
- [Contribution policy](CONTRIBUTING.md)

This is a personal project. Issues are the suggestion channel; this pass does not
change the existing policy on pull requests or grant collaborators write access.

## Data handling and license

Never commit credentials, user-level marketplace state, personal absolute paths or caches.
Review filenames, content and complete history before pushing; do not print matched secret values.
Repository-local relative marketplace metadata is intentionally tracked.
The [MIT license](LICENSE) is unchanged. Companion plugin sources are not copied.
