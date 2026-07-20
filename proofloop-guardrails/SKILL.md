---
name: proofloop-guardrails
description: Use when a persistent engineering change or independent review may match a recurring, cross-repository AI failure pattern, when proofloop requests a portable guardrail check, or when the user asks to add, revise, merge, or remove a guardrail. Do not use as a substitute for repository-specific rules or deterministic gates.
---

# Proofloop Guardrails

Apply only portable correction rules whose triggers match current evidence. Repository facts remain authoritative; a guardrail changes the required action or evidence, not the repository's contract.

## Route without loading the rulebook

1. Read the nearest repository facts that can constrain the task: `AGENTS.md`, docs indexes, manifests, lockfiles, CI, relevant source, and tests. Read only what can change the current decision.
2. Scan only rule headings and Trigger lines:

   ```bash
   rg -n '^### |^- Trigger:' references/guardrails.md
   ```

3. Match those triggers against the raw task, repository facts, relevant source, and actual diff. Do not rely on the main agent's claimed matches when acting as a reviewer.
4. Load the complete text only for plausible matches.
5. For every applicable rule, return:

   ```text
   Guardrail ID → Current action → Required evidence
   ```

6. If no rule matches, exit without a report.

Apply repository facts before portable rules. If a rule conflicts with a repository contract, follow the repository and propose that the portable rule be narrowed.

## Apply, do not narrate

Turn each matched rule into a concrete action in the current task and evidence that can falsify compliance. Do not paste the rulebook, manufacture a compliance report, or add checks unrelated to the current diff.

At Prove, verify the evidence already required by matched rules. Do not reload every rule merely because work is ending.

A fresh-context reviewer independently repeats the heading-and-trigger scan using the raw task, repository facts, and diff. It must not inherit the author's selected rule list.

## Change a rule only after a real event

When a failure, false positive, conflict, or repeated manual check suggests a rule change:

1. Classify the correction first:
   - deterministic invariant → nearest machine gate;
   - repository-specific fact → repository guidance or test;
   - language/tool behavior → the owning technical skill;
   - recurring cross-repository reasoning failure → portable guardrail candidate.
2. Propose the smallest add, rewrite, merge, move, or deletion in `Trigger → Failure → Required action → Evidence → Exceptions` form.
3. Use a fresh-context reviewer to check generality, duplication, conflicts, and whether a machine gate would be better.
4. Modify `references/guardrails.md` only after the responsible engineer approves.

Do not create an incident log, pending-proposal database, changelog, automatic self-update process, or separate hand-written index. Git history records rule evolution.
