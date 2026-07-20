---
name: proofloop
description: Use for engineering tasks that intend persistent repository changes, including features, bug fixes, behavior or configuration changes, refactors, migrations, dependency upgrades, and test changes. Do not use by default for a single source fact, code explanation, pure review, or a small read-only investigation.
---

# Proofloop

Use the lightest workflow that can support an honest completion claim. Own the overall flow; other skills supply a method, reviewers supply independent findings, and machine gates supply deterministic facts.

## The four questions

For every persistent change, answer these questions at the fidelity the task needs:

1. **Understand — What outcome and boundary are actually accepted?**
   - Inspect the relevant source before making code claims.
   - Separate facts, inferences, and unknowns.
   - Read only the repository guidance and history that can change the decision.
2. **Decide — What is the smallest correct next slice?**
   - Preserve the accepted outcome, oracle, compatibility, and safety boundaries.
   - Prefer one vertical behavior slice over horizontal scaffolding.
   - Resolve uncertainty that could materially change the implementation; do not inventory hypothetical risks.
3. **Do — What is the smallest patch that realizes that slice?**
   - Follow existing repository conventions and reuse present capabilities.
   - Change tests and production code in short feedback loops when useful.
   - After each meaningful green result, inspect the real diff for newly visible boundaries or counterexamples.
4. **Prove — What does fresh evidence now justify claiming?**
   - Run the narrowest checks that distinguish the intended change from credible wrong implementations.
   - Re-run relevant checks after the final relevant edit.
   - State what was verified, what was not, and keep the completion claim no broader than the evidence.

For a small, explicit change, run all four questions in one short sequence. Do not create a spec, plan, matrix, report, or reviewer merely to represent the questions.

## Return instead of pushing forward

- Return to **Understand** when source, repository history, or external semantics contradict the current framing.
- Return to **Decide** when the oracle is unclear, an implementation choice changes behavior or scope, or evidence exposes a materially different option.
- Return to **Do** when verification reveals an implementation defect with an unchanged outcome.
- Narrow the completion claim when remaining uncertainty cannot be removed proportionately.

## Load only the missing method

| Information gap | Action |
|---|---|
| A bug is non-trivial, difficult to reproduce, or causally unclear | Read [bug.md](references/bug.md). |
| External or upstream semantics may have changed | Read [evidence-moves.md](references/evidence-moves.md); use `research` only when primary-source legwork is substantial. |
| Multiple real options remain or a falsifiable experiment can distinguish them | Read [evidence-moves.md](references/evidence-moves.md). |
| One proof could pass while a credible wrong implementation remains | Use `proofloop-test-matrix`. |
| Repository facts or recurring AI mistakes may constrain the change | Use `proofloop-guardrails`; no hit should produce no report. |
| A fresh context could find a materially different counterexample | Read [review.md](references/review.md) and call the narrowest reviewer. |
| Work must survive this context or become durable repository knowledge | Read [knowledge-handoff.md](references/knowledge-handoff.md). |

Do not let a leaf skill replace this flow. Strict TDD, research reports, complete code audits, Ponytail, plans, and subagent orchestration are explicit modes or lenses, not automatic gates.

## Choose evidence, not ceremony

Find the closest deterministic fact owner first: existing tests, repository lint or build commands, schemas, manifests, lockfiles, or CI rules. Add a permanent machine gate only when it expresses a durable, unambiguous invariant with low false positives and a clear maintainer.

Use a fresh-context reviewer only when independence can change the answer. Give it the raw task, accepted basis, directly relevant source or diff, and existing evidence—not the author's long justification. Treat every finding as a falsifiable claim for the main agent to verify. The reviewer must not edit the implementation it reviews.

## Finish

Before claiming completion:

- inspect the final relevant diff;
- run fresh, proportionate evidence;
- check applicable repository constraints and portable guardrails;
- report changed behavior, commands and results, evidence coverage, and material unverified boundaries.

Stop when the accepted outcome is met and the intended confidence claim is supported. Do not add workflow artifacts for future possibilities.
