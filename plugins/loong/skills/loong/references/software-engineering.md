# loong software-engineering routing

Use this routing only for coding, debugging, refactoring, tests, repository changes, or implementation plans. The loong contract controls scope, permissions, evidence, and the final report.

## Companion routing

The core Karpathy invariants are already part of loong: state assumptions, choose the minimum sufficient change, edit surgically, and define observable acceptance checks. When available, invoke `andrej-karpathy-skills:karpathy-guidelines` for the same discipline. The tested local version is 1.0.0.

When available, route to these Superpowers skills by trigger:

- `superpowers:brainstorming` and `superpowers:writing-plans` only after the complexity gate identifies a real design or multi-step planning task;
- `superpowers:systematic-debugging` for a reproducible bug investigation;
- `superpowers:test-driven-development` for a behavior change that benefits from a regression test;
- `superpowers:verification-before-completion` before any completion claim or authorized commit/push.

The tested local Superpowers version is 6.2.0. These companions are optional accelerators, not hidden hard dependencies. If one is absent or a version is not the tested version, continue with loong's built-in rules, state which companion was unavailable, and lower confidence in any companion-specific behavior. After a companion upgrade, rerun the simple-task, complex-task, and failure-mode smoke checks before relying on changed behavior.

## Engineering stop conditions

Before mutation, record the current directory, branch, status, relevant files, and baseline test result when available. Do not modify unrelated files. All companion instructions about commits, pushes, external writes, or services are subordinate to the loong permission contract. If a test, build, or review fails, report the exact failure and keep the task open.

## Mandatory push gate: three-pass redaction

Before every `git push`, run all three passes against the repository and the exact commit/archive being pushed. A non-zero match or an inability to inspect a pass is a hard stop. Report only counts and filenames; never print matched secret values.

1. **Inventory:** list `git ls-files`; reject suspicious credential/environment/key filenames, untracked build output, user-level marketplace state, and machine-specific files.
2. **Content:** scan tracked files and the staged diff for high-confidence credential markers, secret assignments, private-key headers, bearer-like values, personal data, and absolute local paths. Review every match manually without copying its value to logs.
3. **History and artifact:** scan every reachable commit and the final `git archive` contents using the same rules; verify the archive file list, staged diff, author identity, and clean status. Only then push.

This gate covers the repository's data boundary; provider-side push protection is an additional check, not a substitute.

For code review, separate correctness, security, maintainability, and scope findings; rank them by impact and cite exact files or lines. For a plan, every step must have a concrete file, command, expected result, and acceptance check.
