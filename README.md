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

Install directly from the public Git marketplace:

```text
codex plugin marketplace add l0oo0ng/loong-prompt
codex plugin add loong@loong-prompt
```

For local development, use a quoted clone path:

```text
codex plugin marketplace add "<clone-directory>"
codex plugin add loong@loong-prompt
```

The companion plugins `andrej-karpathy-skills` (tested 1.0.0) and `superpowers` (tested 6.2.0) are optional coding accelerators. If unavailable, loong keeps its built-in Karpathy invariants and reports the missing companion. The global-skill-router is also optional; loong's own complexity gate remains active without it. Complex tasks require a runtime with one orchestrator plus three reviewer agents and a second cross-review pass; loong stops rather than pretending this happened when that capability is absent.

## Data handling

Do not commit credentials, tokens, passwords, private keys, secret-bearing environment values, user-level personal marketplace state, local caches, or machine-specific absolute paths. The repository-local `.agents/plugins/marketplace.json` is intentionally tracked because it contains only portable relative paths required for installation. Run a three-pass redaction review before every push:

1. inspect the file list and suspicious filenames;
2. scan all content for credential patterns, secret words, and local identity/path leakage;
3. scan the complete Git history and final diff, then manually review every match and the archive to be pushed.

## Contributions

This personal repository uses Issues for suggestions. It does not grant collaborators write access. GitHub public repositories cannot technically prevent fork pull requests, so pull requests may be closed under the policy in `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
