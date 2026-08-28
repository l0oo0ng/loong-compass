# loong review protocol

This protocol applies to every complex task. The orchestrator owns the final answer and does not outsource the decision.

## 1. Normalize the brief

Write a short brief containing: goal, known facts, unknowns, constraints, authorized actions, acceptance test, and deadline if one exists. Remove irrelevant personal data and redact credentials before dispatching any subtask. Never include API keys, access tokens, passwords, private keys, session cookies, or secret-bearing environment values in agent context, logs, examples, or artifacts.

## 2. Independent first pass

Dispatch three agents in parallel. Give each the normalized brief, but not the other agents' conclusions.

| Role | Required output |
| --- | --- |
| Premise auditor | Explicit assumptions; false premises; logic jumps; missing variables; first-principles decomposition; questions that materially change the answer. |
| Evidence verifier | Claim ledger; source for each consequential claim; source date and authority; fact/inference/unknown label; confidence and unresolved conflicts. |
| Adversarial reviewer | Strongest opposing case; alternative causal model; failure modes; costs and opportunity costs; incentives, selection, measurement, and confirmation bias. |

Each report must distinguish observed evidence from interpretation and must refuse invented numbers, names, dates, citations, or examples.

## 3. Cross-review

After all three reports arrive, send each reviewer a sanitized digest of the other two. Each reviewer must return:

- one agreement that survives scrutiny;
- one disagreement or correction, with evidence;
- one risk the first pass missed;
- a confidence score and the condition that would change it.

If a second pass cannot be performed, mark cross-review as incomplete and do not claim independent corroboration. For a complex task, stop before irreversible execution when the required multi-agent capability is unavailable.

## 4. Orchestrator decision

Reconcile conflicts using this order: direct primary evidence, reproducible local evidence, independent corroboration, then reasoned inference. A majority is not evidence. Preserve unresolved disagreement when it changes the recommendation; give a conditional answer or ask one targeted question. Lower confidence when key evidence is missing.

## 5. Output labels

Use these labels where confusion is likely:

- **事实** — directly observed or cited and independently checked.
- **推测** — a reasoned implication that could be false.
- **观点** — a preference or value judgment.
- **未知** — not established with available evidence.

Do not present user-supplied figures as verified until checked. If a source cannot be accessed, say so and specify the missing verification.
