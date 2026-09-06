# Evidence Templates

Use only the templates needed for the current evaluation. Preserve unknowns as explicit placeholders.

## Evaluation Lens

```text
Target roles:
Candidate level:
Evaluator: resume screener / technical interviewer / TL / hiring committee
Evaluation state: current completion / planned completion
Time budget:
Hardware and data:
Existing strengths:
Critical skill gap to close:
Assumptions requiring verification:
```

## JD Responsibility Mapping

| JD responsibility or verb | Required capability | Project mechanism | Owned artifact | Evidence | Claim state |
|---|---|---|---|---|---|
| Design / optimize / diagnose ... | ... | ... | ... | ... | shipped / experimentally validated / simulated / roadmap |

Separate terms into `core responsibility`, `required mechanism`, `stack term`, and `bonus`. A technology noun without an artifact or defensible mechanism is not matched.

## Project Charter

```text
Observed phenomenon:
Target workload and user:
Core bottleneck:
Falsifiable question:
Hypothesis:
Primary mechanism owned by candidate:
Baselines:
Primary metric:
Guardrail metrics:
Expected losing conditions:
Environment and scale:
Explicit non-goals:
```

## Causal Chain and Removal Test

```text
[workload] -> [resource pressure or interference] -> [mechanism] -> [system behavior] -> [metric]
```

For every proposed technology, ask:

1. Which arrow changes because of it?
2. What owned implementation uses it?
3. Which experiment isolates its effect?
4. If removed, does the core question remain intact?

If the final answer is yes, classify it as an extension. If the proposal has multiple independent chains or success criteria, split it into projects or milestones.

## Evidence Ledger

| Claim | State | Owned artifact | Experiment or trace | Environment | Result | Limitation | Resume-safe wording |
|---|---|---|---|---|---|---|---|
| ... | ... | path, commit, module | command or report | model, hardware, scale | measured value | boundary | exact claim |

No evidence cell may contain a plan presented as a result. Link real paths, commits, commands, traces, or reports when available.

## Minimum Experiment Plan

```text
Question:
Baseline A:
Baseline B:
Single changed mechanism:
Realistic workloads:
Adversarial workload:
Primary metric and SLO:
Tail and guardrail metrics:
Warmup and repetition policy:
Ablations:
Failure injection or fallback:
Artifacts to retain:
Decision rule for accepting the hypothesis:
```

## Milestone Gate

At each roadmap change or milestone, report:

```text
New evidence:
Invalidated assumptions:
Hard gates rerun and failures:
Updated rubric score:
Current weakest rubric dimension:
Claims promoted or demoted between states:
Scope added and its causal necessity:
Next smallest experiment:
```

## Resume Bullet

```text
针对 [workload] 下的 [bottleneck]，在 [real system] 中实现 [owned mechanism]；相比 [baselines]，在 [hardware and scale] 下将 [metric] 改善 [measured result]，并通过 [ablation or trace] 解释收益来源及失效边界。
```

If results are unavailable, keep `[measured result]` visible or write a project-plan statement outside the resume. Never replace missing evidence with adjectives such as production-grade, high-performance, large-scale, or significant.

## Evaluation Output

```text
Verdict:
Lens and assumptions:
JD mapping:
Core question and causal chain:
Hard gates:
Score and weakest dimensions:
Minimum credible implementation:
Evidence plan:
Claim-state boundaries:
Risks and interview questions:
Resume bullet:
```
