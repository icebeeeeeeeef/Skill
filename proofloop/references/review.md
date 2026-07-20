# Fresh-context review

Use independent review only when a different context can produce evidence that may change the decision or completion claim.

## Select one narrow reviewer

| Reviewer | Use when |
|---|---|
| `proofloop-matrix-reviewer` | A test matrix may still allow a credible wrong implementation. |
| `proofloop-bug-reviewer` | The causal chain, contract owner, regression seam, or fix brief may be wrong. |
| `proofloop-decision-reviewer` | Facts, alternatives, or external semantics may not support the chosen design. |
| `proofloop-implementation-reviewer` | The final diff may not conform to the accepted outcome and constraints. |
| `proofloop-simplicity-reviewer` | The implementation may duplicate capability or contain removable complexity. |
| `proofloop-reviewer` | A narrow concern exists but no named contract fits. |

Do not call all reviewers by default. Review tiny changes only when a concrete independent question remains.

## Send a minimal evidence packet

Include:

- raw task and accepted outcome;
- authoritative basis and relevant repository constraints;
- directly relevant source, tests, diff, or matrix;
- commands and raw results already obtained;
- the single review question.

Exclude the author's persuasive narrative and claimed conclusion. The reviewer must independently inspect applicable repository facts and portable guardrail triggers.

## Process findings

A useful finding contains a falsifiable claim, direct evidence location, consequence, and smallest discriminating check. The main agent verifies it before changing code. After a change, re-run the affected evidence and re-review only the changed concern.

The reviewer is read-only: it must not repair the artifact it judges, approve residual risk, or claim that missing evidence passed.
