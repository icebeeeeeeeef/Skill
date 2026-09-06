# Verification and Synthesis

## Purpose

This reference defines:

- **Phase 3 — Verification**: determine which load-bearing conclusions survive adversarial and objective checking;
- **Phase 4 — Final Synthesis**: convert the verified investigation state into a compact, evidence-bounded human answer.

The transition is:

```text
Phase 2 Investigation State
          ↓
Identify load-bearing claims
          ↓
Targeted verification
          ↓
Verification Closure
          ↓
Evidence Freeze
          ↓
Final Synthesis
          ↓
Human-facing answer
```

Phase 3 is **not** a second full investigation.

Phase 4 is **not** an opportunity to silently reopen search or enlarge claims.

The core principles are:

> Verify what the final decision depends on.

and:

> Say no more than the verified evidence supports.

---

# PART A — PHASE 3: VERIFICATION

# 1. Phase-3 Objective

Phase 2 searches for plausible explanations, decisions, or candidate conclusions.

Phase 3 attempts to break the conclusions that matter most.

Its goal is not:

> review everything again.

Its goal is:

> identify the smallest set of claims whose failure could materially change the final answer, then test those claims using the strongest practical evidence.

---

# 2. Phase-3 Input

Phase 3 should begin from the frozen **Investigation State Projection** produced from Phase 2's Global Investigation State. It is a reduced view for verification, not an independently maintained state machine.

Expected contents include:

```text
Surviving hypotheses / conclusions

Established facts

Rejected hypotheses

Critical claims

Evidence ledger

Branch coverage

Residual uncertainty

Known limitations

Recommended verification targets
```

Do not begin by rereading every raw worker transcript.

Consult deeper branch artifacts only when needed to verify a specific claim or resolve provenance.

---

# 3. Identify Load-Bearing Claims

A **load-bearing claim** is a claim whose failure would materially change:

- the final decision;
- the root-cause attribution;
- the feasibility judgment;
- the proposed action;
- the proof;
- the validity of a major recommendation.

Example:

```text
Final conclusion:
"Proceed with the controller experiment."

Possible load-bearing claims:

C1. The target workload actually contains the relevant regime.
C2. Upstream does not already solve the same problem.
C3. The runtime exposes a usable integration seam.
C4. Required signals are observable.
C5. There exists a regime where the proposed decision can outperform the baseline.
```

A minor formatting or implementation-detail claim is not load-bearing if changing it would leave the final decision unchanged.

---

# 4. Load-Bearing Claim Triage

Prioritize verification when one or more of the following apply:

- the claim materially supports the final conclusion;
- the evidence is still uncertain;
- multiple branches disagreed;
- the claim is assumption-heavy;
- the claim is novel or counterintuitive;
- the claim is a synthesis across several weaker observations;
- the cost of being wrong is high;
- the claim defines the boundary of a go / pivot / kill decision.

Do not spend equivalent verification budget on low-impact findings.

---

# 5. Bundle Verification by Failure Mode or Evidence Source

Do not automatically create one verifier per claim.

Group claims when they share the same:

- evidence source;
- runtime mechanism;
- test methodology;
- failure mode;
- source-of-truth.

Example:

```text
C1 lifecycle semantics
C2 state observability
C3 controllable transition
```

may all be checked by one:

```text
Runtime Contract Verification
```

Similarly:

```text
C4 benefit regime exists
C5 benefit exceeds overhead
```

may be bundled into:

```text
Performance Economics Verification
```

This avoids repeated reading and unnecessary verifier multiplication.

---

# 6. Select the Oracle by Claim Type

Choose the most direct, reliable, and reproducible practical oracle for the claim; do not impose a strict total order across unlike claims.

Useful context-specific defaults:

- runtime behavior or a causal performance claim → controlled test, trace, profile, or reproduction that observes the behavior;
- interface, configuration, or compatibility contract → controlling source, specification, or authoritative documentation;
- code change → focused reproducer and relevant tests;
- mathematical proof → formal checker or independently checkable derivation;
- broad empirical effect → controlled experiment with scope-matched measurements.

Independent reproduction and adversarial review can strengthen a result when the direct oracle is incomplete. LLM consensus is always weak evidence and cannot establish correctness on its own.

However:

> weak opinion evidence should not override a stronger direct observation without a specific methodological reason.

Examples:

```text
5 agents say "looks race-free"
<
ThreadSanitizer finds a race
```

```text
several reviewers remember upstream lacks feature X
<
current upstream source implements feature X
```

---

# 7. Three Verification Failure Classes

Phase 3 should consider three distinct ways the investigation may still be wrong.

## 7.1 Claim Correctness

Question:

> Is this critical claim actually true?

Examples:

- root cause attribution;
- source-level behavior;
- proof lemma;
- performance regime;
- implementation assumption.

---

## 7.2 Search Coverage

Question:

> Did the investigation omit an entire high-leverage explanation or decision dimension?

Example:

```text
Investigated:
scheduler
communication
kernel

Potential missing family:
CPU launch bottleneck
```

The investigation may be internally consistent while still being incomplete.

---

## 7.3 Evidence-to-Conclusion Scope

Question:

> Even if the evidence is true, does it justify the breadth of the claim?

Example:

Evidence:

> offload beat recompute in workload A under low CPU contention.

Invalid synthesis:

> offload is generally better than recompute.

Correct bounded claim:

> offload was beneficial in the measured workload under the tested contention regime.

This audit protects against overgeneralization.

---

# 8. Verification Packet

A verifier should receive a bounded Verification Packet rather than the generator's full reasoning history.

A packet should normally include:

```text
Claim

Why the claim matters

Claim scope / boundary

Supporting evidence

Contradicting evidence

Relevant artifacts

Requested attack / verification objective
```

Example:

```text
Claim:
CPU restore can outperform recompute in regime R.

Importance:
If false, the proposed dynamic controller loses a core action regime.

Scope:
8k–32k prefix tokens under configuration X.

Supporting evidence:
E2, E5.

Contradicting evidence:
E7.

Task:
Attempt to falsify the claim.
Check omitted costs, boundary assumptions, and counter-regimes.
```

Avoid giving the verifier unnecessary prior prose that may anchor it to the original conclusion.

---

# 9. Verifier Objective

A verifier's primary goal is:

> test, falsify, narrow, or establish the claim.

It is not primarily:

> redesign the solution.

Prefer outputs such as:

```text
violated assumption

counterexample

missing condition

incorrect source interpretation

measurement mismatch

unsupported extrapolation
```

over:

> Here is a completely new architecture I would build instead.

Design alternatives may be proposed when they reveal why the original claim fails, but verification should not silently become a new full investigation.

---

# 10. Verification Report

Use a compact structured report.

```text
VERDICT

CLAIM TESTED

ATTACK / CHECK PERFORMED

KEY EVIDENCE

BOUNDARY OR COUNTEREXAMPLE

RESIDUAL RISK

RECOMMENDED DISPOSITION
```

Recommended verdict states:

```text
VERIFIED

CONDITIONALLY VERIFIED

NARROWED

FALSIFIED

UNRESOLVED

BLOCKED
```

---

## VERIFIED

The claim survives relevant checking within its stated scope.

---

## CONDITIONALLY VERIFIED

The claim holds only when explicit conditions are satisfied.

---

## NARROWED

The original claim was too broad, but a smaller claim survives.

Example:

```text
Original:
offload beats recompute for long gaps

Narrowed:
offload beats recompute for long gaps only when
restore-queue contention remains below threshold X
```

---

## FALSIFIED

A load-bearing part of the claim is contradicted by sufficiently strong evidence.

---

## UNRESOLVED

Available evidence cannot distinguish the competing possibilities.

---

## BLOCKED

Verification requires unavailable evidence or capability.

Unknown is a valid outcome.

---

# 11. Coverage Audit

Coverage audit should be lightweight and targeted.

Its task is:

> identify whether there exists an uninvestigated high-level hypothesis family or failure dimension that could materially overturn the current conclusion.

Do not ask:

> list every conceivable possibility.

Ask:

> is there a plausible missing category whose investigation has high expected decision impact?

Potential triggers include:

- no strong objective verifier exists;
- the search space was broad;
- Phase 2 converged unusually quickly;
- initial branches shared similar assumptions;
- the final decision is high-stakes;
- the Main Agent recognizes that early decomposition strongly shaped the result.

High-budget runs should generally include a lightweight coverage audit.

Medium runs use it conditionally.

---

# 12. Coverage Audit Output

Keep it short:

```text
Coverage assessment:
SUFFICIENT / MATERIAL GAP / UNCERTAIN

Potential missing family:
...

Why it matters:
...

Recommended action:
none / targeted reopen
```

If only low-value speculative possibilities remain, do not reopen the investigation.

---

# 13. Evidence-to-Conclusion Audit

Before closure, compare critical conclusions against actual evidence scope.

For each load-bearing conclusion, ask:

```text
What exactly was observed?

Under what conditions?

What is inferred rather than observed?

Does the final wording preserve those boundaries?
```

Common failure patterns:

### Universalizing a local result

```text
measured in one regime
→ claimed as universal
```

### Converting correlation to causation

```text
timing correlation
→ asserted root cause
```

without intervention or stronger causal evidence.

### Converting absence of evidence to evidence of absence

```text
not observed
→ impossible
```

### Treating source possibility as runtime reality

```text
code path exists
→ assumed exercised in workload
```

### Treating one benchmark improvement as mechanism proof

```text
performance improved
→ assumed proposed mechanism caused improvement
```

without sufficient isolation.

Narrow the wording rather than forcing a binary verdict when appropriate.

---

# 14. Conflicting Verification Results

If Phase 2 and Phase 3 disagree, do not automatically accept either side.

Move the claim to:

```text
CONTESTED
```

Compare:

- evidence authority;
- reproducibility;
- scope match;
- experimental controls;
- artifact freshness;
- methodological quality.

Example:

```text
Phase-2 conclusion:
H1 likely

Verifier:
H1 false
```

If:

```text
Phase 2 = static inference

Verifier = controlled reproducer
```

the reproducer normally dominates.

If two controlled measurements conflict:

```text
targeted reconciliation
```

may be warranted.

Do not resolve by majority vote.

---

# 15. Measurement Reconciliation

When strong evidence conflicts, ask whether:

- test conditions differ;
- workload regimes differ;
- software versions differ;
- artifacts are stale;
- one experiment is uncontrolled;
- one metric is measuring a different stage;
- both conclusions are valid under different boundaries.

Possible resolution:

```text
apparent conflict
      ↓
scope split
      ↓
both claims become conditional
```

If conflict remains irreducible:

```text
UNRESOLVED
```

is the correct state.

---

# 16. Targeted Repair

A verifier may identify a local defect that can be repaired without reopening the entire investigation.

Examples:

- proof misses one lemma;
- patch fails one narrow test;
- performance claim omitted a queue-delay term;
- source interpretation used the wrong lifecycle boundary.

Allow a bounded repair loop:

```text
claim / candidate
      ↓
verifier
      ↓
local flaw
      ↓
targeted repair
      ↓
recheck
```

Default:

> one repair / recheck round for a load-bearing claim.

High budget may justify one additional round.

Do not optimize for eventually obtaining PASS.

Repeated failure should result in:

```text
NARROWED
UNRESOLVED
or
FALSIFIED
```

---

# 17. When Verification Must Reopen Phase 2

Return formally to Phase 2 when verification discovers:

- a new load-bearing hypothesis family;
- a missing evidence domain;
- a major causal contradiction;
- an invalid core assumption requiring substantial investigation;
- a failure that changes the original decomposition.

Do not disguise substantial new search as "verification."

If reopening exceeds the approved execution envelope, follow the USER GATE rules in `SKILL.md` and `execution-control.md`.

---

# 18. Verification Stop Criteria

Phase 3 may close when:

## Load-bearing closure

Each load-bearing claim is:

```text
verified
conditional
narrowed
falsified
unresolved
or blocked
```

No critical claim remains silently assumed.

---

## No ignored fatal contradiction

No strong unresolved evidence directly contradicts the final candidate conclusion without being surfaced.

---

## Coverage is sufficient

No obvious uninvestigated high-leverage hypothesis family remains.

---

## Residual uncertainty is bounded

Remaining uncertainty is explicit enough to state:

- what is unknown;
- why it is unknown;
- what conclusion it could affect.

---

## Marginal verification value is low

Another verifier or review is unlikely to materially change the decision.

---

# 19. Verification Closure Package

Phase 3 should produce a compact internal package.

Conceptually:

```text
FINAL CLAIM LEDGER

Verified claims

Conditionally verified claims

Narrowed claims

Falsified claims

Unresolved / blocked claims

Load-bearing status

Validated boundaries

Rejected conclusions

Residual uncertainty

Coverage assessment

Oracle and evidence rationale

Wording constraints
```

The **Wording Constraints** section is important.

Examples:

```text
May say:
"Observed under workload X."

Must not say:
"Generally true across workloads."
```

```text
May say:
"The evidence is consistent with scheduler-side delay."

Must not say:
"Scheduler delay is definitively the only root cause."
```

Phase 4 must respect these constraints.

---

# PART B — PHASE 4: FINAL SYNTHESIS

# 20. Phase-4 Objective

Phase 4 turns the Verification Closure into a useful human answer.

It should optimize for:

```text
decision usefulness ↑

evidence fidelity ↑

human reading burden ↓
```

Phase 4 does not optimize for preserving every branch detail.

---

# 21. Evidence Freeze

Entering Phase 4 creates an **Evidence Freeze**.

Default rule:

```text
NO NEW INVESTIGATION
```

The Main Agent should not silently:

- open new branches;
- invent new claims;
- perform new broad research;
- change the success criteria.

If synthesis exposes a material contradiction:

```text
SYNTHESIS BLOCKED
      ↓
formally reopen Phase 3 or Phase 2
```

This prevents endless hidden search during answer writing.

---

# 22. Determine Final Disposition Before Writing

Before drafting prose, identify the final outcome type.

Examples for technical review:

```text
PROCEED

PROCEED WITH CONDITIONS

PIVOT

KILL

NOT ENOUGH EVIDENCE
```

Examples for RCA:

```text
ROOT CAUSE ESTABLISHED

ROOT CAUSE CONDITIONALLY ESTABLISHED

MULTIPLE PLAUSIBLE CAUSES REMAIN

INSUFFICIENT EVIDENCE
```

Examples for proof:

```text
PROOF VERIFIED

PROOF HAS UNRESOLVED GAP

COUNTEREXAMPLE FOUND

NO PROOF ESTABLISHED
```

The final disposition should follow from the verified claim ledger.

It should not be chosen because one worker sounded more persuasive.

---

# 23. Build the Minimal Sufficient Decision Chain

The final answer should explain:

> why the validated evidence leads to the final disposition.

Prefer a short causal or decision chain.

Example:

```text
TP=2 slower than TP=1
        ↓
communication time too small to explain delta
        ↓
idle gap occurs before collective
        ↓
scheduler / CPU-dispatch evidence aligns with gap
        ↓
targeted A/B changes both gap and latency
        ↓
scheduler-side dispatch is the strongest supported cause
```

This is more useful than reproducing the full chronological investigation.

---

# 24. Return Decision-Relevant Investigation History

Default final output should summarize:

```text
what was initially uncertain

what major alternatives were checked

what evidence changed the search

what survived verification
```

Do not return:

- every tool call;
- every dead-end thought;
- every worker's full chronology;
- every minor rejected possibility.

Prefer:

```text
The investigation first ruled out configuration mismatch
and dominant communication saturation. Runtime evidence then
shifted attention toward scheduler/CPU dispatch, which survived
targeted verification.
```

This provides auditability without transcript overload.

---

# 25. Preserve Important Rejected Alternatives

Final answers should normally retain the major competing hypotheses that were ruled out.

Examples:

```text
Ruled out:
- configuration mismatch;
- dominant NCCL saturation;
- CUDA Graph configuration difference.
```

Include an alternative when:

- it was a serious competing hypothesis;
- the user is likely to ask "why not X?";
- ruling it out materially strengthens the conclusion.

Do not list every low-probability branch.

---

# 26. Preserve Residual Uncertainty

Do not hide remaining uncertainty to make the answer feel cleaner.

State:

```text
What remains unknown?

Why?

How much could it change the conclusion?

What evidence would resolve it?
```

Example:

> The current evidence does not distinguish scheduler queue delay from a narrower CPU-side synchronization effect under higher concurrency. This does not overturn the observed bottleneck family, but it affects the exact fix.

Residual uncertainty should be proportional to its decision impact.

---

# 27. Respect Claim Boundaries

Phase 3 wording constraints are binding.

Maintain distinction between:

```text
FACT

INFERENCE

UNKNOWN
```

Useful language:

### Fact / observation

> The trace shows...

> Source code confirms...

> The controlled benchmark measured...

### Inference

> The strongest supported explanation is...

> Taken together, the evidence is most consistent with...

### Unknown

> Current evidence cannot establish...

> This remains unresolved because...

Do not convert:

```text
likely
→ certain
```

or:

```text
conditional
→ universal
```

during synthesis.

---

# 28. Default Human-Facing Structure

The default answer should be compact and decision-oriented.

A useful generic structure is:

## Conclusion

State the final disposition directly.

## Why

Give the shortest sufficient causal / decision chain.

## Key evidence

Only the most load-bearing evidence.

## Important alternatives ruled out

Only serious competing explanations.

## Conditions / boundaries

Where the conclusion applies.

## Remaining uncertainty

Only decision-relevant unknowns.

## Recommended next step

The highest-value action supported by the investigation.

Do not mechanically include every heading when natural prose is clearer.

---

# 29. Task-Specific Presentation

Adapt the final presentation to the task.

## Technical proposal review

Prefer:

```text
Final judgment

Why

Critical design decisions
- passed
- narrowed
- not established

Main risks

Ruled-out objections

Conditions for proceeding

Recommended next action
```

---

## Performance diagnosis

Prefer:

```text
Symptom

Strongest supported root cause

Causal evidence

Why major alternatives are weaker

Scope / workload boundary

Confidence / residual uncertainty

Next experiment or fix
```

---

## Bug / RCA

Prefer:

```text
Observed failure

Root cause

Evidence chain

Ruled-out causes

Reproducer / verifier status

Fix direction

Remaining risk
```

---

## Mathematical proof

Prefer:

```text
Status

Core proof idea

Load-bearing lemmas

Verification status

Assumptions / boundary

Remaining gaps or counterexamples
```

Do not label a proof verified when any load-bearing step remains unresolved.

---

# 30. Progressive Disclosure

Default to a compact **Decision View**. Use this term consistently for the human-facing final/partial result; it is not a separate investigation state.

Preserve a drill-down path:

```text
Final conclusion
      ↓
Load-bearing claim
      ↓
Verification result
      ↓
Evidence entry
      ↓
Branch report
      ↓
Raw artifact
```

Do not expose full worker transcripts by default.

Provide deeper detail when the user requests it or when it is required to justify the conclusion.

---

# 31. Traceability

Every load-bearing final statement should be traceable to:

- an established fact or clearly labeled inference;
- relevant evidence;
- a verification disposition;
- its scope and conditions.

Rejected alternatives should be traceable to the evidence that weakened or falsified them.

Unknowns should remain visible when they could change the decision.

---

# 32. Final Self-Check

Before returning the final answer, check:

- Does the disposition match the Verification Closure?
- Has any local result been generalized beyond its evidence?
- Has correlation been rewritten as causation?
- Has missing evidence been hidden?
- Are rejected alternatives actually supported as rejected?
- Are conditions and workload boundaries visible?
- Is residual uncertainty decision-relevant and concise?
- Did Phase 4 avoid new investigation?
- Is the answer shorter than the internal investigation while preserving the decision logic?

If not, narrow or revise the wording.

---

# 33. Phase-4 Completion

Phase 4 is complete when:

- the final disposition is evidence-bounded;
- the minimal sufficient decision chain is clear;
- load-bearing evidence is visible;
- important alternatives and uncertainty are represented accurately;
- no claim exceeds the Verification Closure.

Return the final answer without agent-count ceremony or transcript dumping.
