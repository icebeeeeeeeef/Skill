---
name: MAW
description: Use only when the user explicitly invokes this named skill for a controlled multi-agent investigation of a difficult analysis, diagnosis, review, proof, or research task.
---

# MAW

This is a human-controlled methodology for adaptive, evidence-bound investigation. It is not a fixed agent workflow.

## Activation

- This skill is explicit-invocation only. Do not activate it because a task is difficult, broad, ambiguous, or benefits from more reasoning.
- Loading or discovering this Skill without an explicit user request does not authorize the workflow or subagents. Continue normally.
- An explicit invocation authorizes **Phase 1 planning only**. It never authorizes investigation or side effects by itself.
- `agents/openai.yaml` disables implicit invocation. If a host behavior conflicts, keep the explicit trigger and follow host safety rules.

## Lifecycle and USER GATE

```text
Explicit trigger → Phase 1: plan → Human Review Plan → USER GATE
→ Phase 2: investigate → Phase 3: verify → Phase 4: Decision View
```

- Do not skip phases or begin Phase 2 before explicit approval of the current Human Review Plan.
- Phase 1 produces an internal Execution Spec and a compact user-facing **Human Review Plan**. The plan states the goal, success criteria, branch unit, strategy, expected evidence and verification, envelope, expansion boundary, and stop conditions.
- Clear execution intent such as “approve,” “execute,” “start,” or “proceed with this plan” passes the USER GATE. Discussion, praise, or a request to explain does not.
- After a material change, issue an updated Human Review Plan and wait for new explicit execution approval. The authoritative details are in `references/planning-and-selection.md` and `references/execution-control.md`.

## Phase-1 reconnaissance

Phase 1 is Main-Agent-only and read-only. Reconnaissance is allowed only to learn the minimum information needed to define a meaningful branch unit and execution envelope.

It must not dispatch subagents, run experiments, invoke tools with side effects, or begin evidence collection that belongs to execution. If that minimum cannot be obtained read-only, present the Human Review Plan with the limitation and wait at the USER GATE.

## Authority and V1 boundary

The Main Agent owns task framing, Execution Spec, branch admission, branch merge/prune/replace decisions, state reduction, phase transitions, termination, and final synthesis. Workers investigate only their assigned BranchSpec and return bounded Branch Reports; they cannot redefine the task, open global branches, delegate, or present a final conclusion.

V1 uses **Codex native subagents only**. It must not implement or depend on an external workflow engine, persistent database, fixed agent pool, agent-to-agent network, or automatic budget expansion. The host's safety, permission, and tool rules always take precedence over this Skill.

## Approved execution envelope

The approved envelope is a boundary for Main's adaptive choices, not a frozen DAG. It records scope, success criteria, default budget class (**Medium** unless the user chooses another), breadth/depth and verification allowance, allowed evidence sources, allowed tools/resources, side-effect boundary, and escalation/stop conditions.

Each BranchSpec must inherit those limits or explicitly state a narrower applicable subset: allowed evidence sources, exact allowed tools/resources, and side-effect boundary. “Allowed tools” never authorizes a new tool class, resource, or side effect. Workers remain subject to host safety rules.

Inside the envelope, Main may swap, merge, prune, reprioritize, or replace branches and choose dependency-aware waves. Those internal changes do not reopen the USER GATE when they do not change the user-visible strategy or envelope.

## Material deviation

Pause new global work when a change would alter the user-visible execution strategy or materially expand scope, goal/success criteria, overall budget, method/resources, side effects, or the approved envelope. Explain the evidence gap and proposed expansion, issue an updated Human Review Plan, then wait for approval.

Do not treat a small third dependency wave as automatically material. Wave limits are soft planning priors; judge materiality from total breadth, depth, verification consumption, resources, side effects, scope, and the user-visible strategy.

## Phase routing

- **Phase 1:** Read `references/planning-and-selection.md`; read `references/architecture-patterns.md` only when a pattern choice is genuinely unclear. Use `references/worked-examples.md` only for a needed example.
- **Phase 2:** Read `references/execution-control.md`. Use adaptive, dependency-aware branch/wave control and reduce reports into the single Main state.
- **Phase 3:** Read `references/verification-and-synthesis.md`. Verify only load-bearing claims using the most direct, reliable, reproducible oracle for that claim type; LLM consensus is always weak evidence.
- **Phase 4:** Use the same reference to produce an evidence-bounded **Decision View**. Do not silently reopen investigation while synthesizing.
- **Provenance:** `references/provenance.md` is design-review material only. Never load it during normal execution.

## Evidence and synthesis boundaries

Preserve fact, inference, and unknown as distinct. Objective or direct evidence appropriate to the claim outranks opinion aggregation; do not use majority vote as proof. Phase 3 establishes whether each load-bearing claim is verified, narrowed/conditional, falsified, unresolved, or blocked, and Phase 4 must respect those wording limits.

## Progress, interruption, and partial results

Avoid branch-level progress spam, but send non-blocking milestone updates when they materially help the user understand progress, a completed wave, changed confidence, or an upcoming decision. USER GATE and a key blocker requiring user-only information are blocking waits.

On mechanical failure, use only bounded recovery inside the envelope. On missing evidence, contradictory results, an early stop, or user cancellation, return a clearly labeled partial or blocked Decision View: established facts, ruled-out alternatives, unresolved items, why work stopped, and the highest-value next step.

## Reference authority

This file is the hard runtime contract. Each detailed mechanism has one authoritative reference home; references cannot weaken activation, USER GATE, authority, V1 boundary, envelope, material-deviation, evidence, or synthesis rules above. Load references lazily rather than preloading the tree.
