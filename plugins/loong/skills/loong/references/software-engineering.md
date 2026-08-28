# loong software-engineering routing

Use this routing only for coding, debugging, refactoring, tests, repository changes, or implementation plans. The loong contract still controls scope, permissions, evidence, and the final report.

## Required companion skills

- `andrej-karpathy-skills:karpathy-guidelines` — surface assumptions, choose the minimum sufficient change, edit surgically, and define verifiable success criteria.
- `superpowers:brainstorming` — before designing a new feature or behavior; do not implement before the design gate is approved.
- `superpowers:systematic-debugging` — when diagnosing a bug; reproduce the symptom and trace the root cause before editing.
- `superpowers:test-driven-development` — when implementing a behavior change; write a failing test, make it pass minimally, then refactor only as needed.
- `superpowers:verification-before-completion` — immediately before claiming completion, committing, pushing, or opening a pull request.
- `superpowers:writing-plans` — when a reviewed multi-step implementation plan is required.

These are references to installed skills, not copied source. Codex does not provide a general plugin-to-plugin dependency field, so a missing companion must be reported rather than silently replaced by an invented workflow.

## Engineering stop conditions

Before mutation, record the current directory, branch, status, relevant files, and baseline test result when available. Do not modify unrelated files. Do not commit, push, start a long-lived service, or write an external system without explicit authorization. If a test, build, or review fails, report the exact failure and keep the task open.

For code review, separate correctness, security, maintainability, and scope findings; rank them by impact and cite exact files or lines. For a plan, every step must have a concrete file, command, expected result, and acceptance check.
