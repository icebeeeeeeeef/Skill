---
name: evaluating-career-projects
description: Use when selecting, comparing, scoping, reviewing, or packaging an engineering project for recruiting; deriving a project from JDs; deciding whether to add fashionable technologies; or checking resume and interview claims against actual implementation evidence.
---

# Evaluating Career Projects

## Principle

Treat a project as evidence in a hiring decision, not as a technology showcase:

`Hiring Signal = Role Relevance x Ownership x Technical Depth x Evidence Quality x Transferability x Credibility`

Complexity, novelty, and keyword count matter only when they improve these factors.

## Workflow

1. **Freeze the lens.** State target role family, candidate level, current versus planned completion, time, hardware, data, and collaboration constraints. If current JD facts matter, verify them from representative current sources.
2. **Map the JD.** Extract responsibility clusters and capability verbs before mechanisms, stack terms, and bonus terms. Prefer several related JDs over one listing. Mark assumptions when no JD is supplied.
3. **Form one question.** Write one falsifiable problem, hypothesis, and causal chain. Apply the removal test: if deleting a technology leaves the question intact, move it to an extension or remove it.
4. **Run hard gates.** Check real problem evidence, role relevance, owned hard part, feasible environment, realistic workload, baseline, measurable outcome, reproducibility, and five-level interview defensibility. Read [evaluation-rubric.md](references/evaluation-rubric.md). A failed hard gate overrides the numeric score.
5. **Score the evidence.** Use the fixed 100-point rubric. Identify the weakest dimension; do not average away a credibility or feasibility failure.
6. **Shrink to credible scope.** Keep the smallest real system containing baseline, instrumentation, one deep mechanism, ablations, failure cases, and reproducible artifacts. Split proposals with multiple independent success criteria.
7. **Audit every milestone.** At roadmap changes and implementation milestones, rerun every hard gate, rescore the rubric, and update the evidence ledger. Map each claim and JD term to owned code, experiment, trace, benchmark, or document. Use [evidence-templates.md](references/evidence-templates.md).
8. **Pressure-test and package.** Use [interview-pressure-test.md](references/interview-pressure-test.md). Generate bullets only from verified evidence; retain explicit placeholders for missing measurements.

## Scope Veto

Apply this before proposing architecture or bullets:

- If two mechanisms can succeed or fail independently and each needs its own implementation, baseline, or ablation, they are separate projects or milestones.
- Adapters, pluggable backends, comparison lanes, orchestration, and an adaptive controller do not turn independent mechanisms into one causal question.
- A mainline may own one deep mechanism plus necessary enabling integration. Add a second deep mechanism only when the hypothesis explicitly concerns their interaction and one experiment can isolate it.
- A request to combine technologies for keyword coverage is itself sufficient for a `reshape` verdict, even when constraints are missing. State the veto before asking follow-up questions; do not postpone it until hardware or time is known.
- After the veto, select one assumed mainline from role fit and evidence potential or offer at most two narrow alternatives whose choice depends on a missing constraint. Classify every other technology as baseline, supporting dependency, optional extension, or excluded.
- For a vetoed broad scope, do not continue with its architecture, implementation plan, or resume bullets. Select a narrowed mainline, then apply the complete output contract to that mainline. Never mention excluded or roadmap technologies in its bullet.

## Claim States

Label every material claim:

- `shipped`: implemented and exercised in the stated system.
- `experimentally validated`: measured under a declared environment and workload.
- `simulated`: supported only by a model, replay, trace, or simulator; include calibration limits.
- `roadmap`: planned and never written as completed work.

Never turn one state into another through wording. Never invent metrics, scale, hardware, production status, or personal ownership.

## Mandatory Output

For every substantial evaluation, produce:

1. Verdict: `select`, `reshape`, `defer`, or `reject`.
2. Lens and assumptions.
3. JD responsibility and evidence mapping.
4. Core question, hypothesis, and causal chain.
5. Hard-gate results and rubric score.
6. Minimum credible implementation and evidence plan.
7. Claim-state boundaries.
8. Principal risks and interview follow-ups.
9. Resume bullet with measured values or visible placeholders.

When scope is vetoed, apply every output item to the narrowed mainline and make the rejected scope and exclusions explicit. For a narrow question, return only relevant sections, but enforce every evidence and claim rule.

## Non-Negotiable Rules

- Match responsibilities and capability verbs before technology nouns.
- Require every named technology to map to a mechanism, owned artifact, experiment, or defensible knowledge claim. Otherwise exclude it from project packaging.
- Do not use a broad controller, comparison lane, or deployment layer to disguise several projects as one.
- Do not present simulation as production performance.
- Treat missing hardware or data as scope constraints.
- Challenge the user's preferred direction when role fit, feasibility, ownership, or evidence is weak.
- Prefer one deep, reproducible mechanism over several shallow integrations.
