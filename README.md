# loong prompt

`loong` is a Codex personal plugin for evidence-first reasoning and risk-scaled execution.

It combines four operating principles:

- first-principles decomposition;
- role-based review with explicit epistemic responsibilities;
- strongest-counterargument analysis;
- independent cross-review before consequential decisions.

The plugin adapts to the task. A simple, reversible request stays concise and uses one agent. A complex request uses an orchestrator plus three independent reviewers, then a second cross-review pass. Coding work also routes to the installed `andrej-karpathy-skills` and `Superpowers` skills instead of copying their source.

## Use

Invoke the skill explicitly with `$loong`, or let Codex select it for ambiguous, high-impact, multi-step, source-sensitive, or review-heavy requests.

For project changes, expect a five-field contract: goal, current state, scope and boundaries, acceptance, and execution mode. Consequential claims are labeled as fact, inference, opinion, or unknown.

## Install from this repository

After cloning, register the repository root as a local marketplace and install the plugin:

```text
codex plugin marketplace add <clone-directory>
codex plugin add loong@loong-prompt
```

The companion plugins `andrej-karpathy-skills` and `superpowers` must already be installed when coding routing is needed. They are referenced by name and are not bundled or copied here.

## Data handling

Do not commit credentials, tokens, passwords, private keys, secret-bearing environment values, user-level personal marketplace state, local caches, or machine-specific absolute paths. The repository-local `.agents/plugins/marketplace.json` is intentionally tracked because it contains only portable relative paths required for installation. Run a three-pass redaction review before every push:

1. inspect the file list and suspicious filenames;
2. scan all content for credential patterns, secret words, and local identity/path leakage;
3. scan the complete Git history and final diff, then manually review every match and the archive to be pushed.

## Contributions

This personal repository uses Issues for suggestions. It does not grant collaborators write access; pull requests from forks may be closed under the policy in `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
