---
name: steelman
description: >
  Strengthen an idea into its best defensible form before criticizing it, then
  expand the design space, attack the strongest variants, and synthesize the
  smallest high-value direction worth pursuing. Use for technical brainstorming,
  research ideas, system design, project selection, architecture proposals, and
  other situations where premature rejection or shallow idea generation would be costly.
---

# Steelman Brainstorm

## Purpose

This skill prevents two common brainstorming failures:

1. **Premature rejection**: dismissing an idea because its first formulation has an obvious flaw.
2. **Shallow elaboration**: making small local edits to the user's initial idea without discovering the stronger underlying design space.

The core workflow is:

**Steelman → Extend → Adversarial Attack → Synthesize**

The goal is not to defend the user's idea. The goal is to ensure that:

- an idea is rejected only after its strongest reasonable version has been examined;
- an idea is accepted only after surviving serious adversarial scrutiny;
- the final recommendation is often a refined or narrowed version, not necessarily the original proposal.

---

## When to Use

Use this skill when the user asks to:

- brainstorm a technical or research idea;
- evaluate whether an early-stage idea is worth pursuing;
- strengthen a rough proposal before review;
- explore alternative architectures or mechanisms;
- turn a narrow optimization into a more general systems problem;
- perform adversarial review without prematurely killing promising directions;
- compare several possible implementations of the same underlying insight.

This skill is especially useful when the input contains phrases such as:

- "brainstorm this idea"
- "steelman this"
- "is this idea viable?"
- "what could this evolve into?"
- "help me make this idea stronger"
- "challenge this proposal"
- "find a better formulation"
- "don't reject it too early"

Do **not** use this skill for questions that only require factual lookup, routine debugging, direct implementation, summarization, or simple explanation unless the user explicitly asks for brainstorming or design-space exploration.

---

## Core Principle

Never criticize only the weakest version of an idea.

Before attacking an idea, ask:

> If a strong researcher or systems engineer believed this idea was promising, how would they formulate and implement its strongest reasonable version?

Then attack **that** version.

Steelmanning is not agreement.

Do not invent evidence, hide constraints, or rescue an idea with unrealistic assumptions. Strengthening must stay within plausible engineering, scientific, economic, and resource constraints.

---

# Workflow

## Phase 0 — Extract the Core Insight

Before discussing implementation details, identify:

- the underlying problem;
- the proposed mechanism;
- the hoped-for benefit;
- the implicit assumptions;
- the target workload / regime / user;
- the relevant baseline;
- the resource or engineering constraints already given.

Then state the idea in one compact sentence:

> **Core insight:** ...

Distinguish the core insight from the user's current implementation proposal.

Example:

- Current proposal: "Offload KV cache during tool gaps."
- Possible core insight: "Temporarily inactive KV state has a lifecycle and should be managed according to expected future reuse and resource opportunity cost."

The rest of the workflow should reason from the **core insight**, not remain trapped inside the first implementation.

---

## Phase 1 — Steelman

Construct the strongest reasonable version of the idea.

Do not merely patch individual flaws. Improve the proposal across the dimensions that actually determine whether it could work.

Consider, when relevant:

### Mechanism

- What is the precise decision being made?
- At what granularity?
- At what lifecycle point?
- What state does the mechanism observe?
- What action space is available?

### Cost model

- What is being optimized?
- Latency?
- Throughput?
- Goodput?
- Memory?
- Cost?
- Reliability?
- Some weighted or constrained objective?

Convert vague intuition into an explicit decision rule when useful.

For example:

\[
a^* = \arg\min_{a \in A} \mathbb{E}[C(a)\mid state, workload]
\]

Do not force mathematical notation if it adds no clarity.

### Uncertainty

Ask whether the strongest version should include:

- probability rather than deterministic prediction;
- confidence thresholds;
- hysteresis;
- fallback behavior;
- online estimation;
- conservative default behavior;
- bounded exploration.

### Engineering realism

Add only mechanisms that could plausibly exist in a real system:

- observability hooks;
- failure handling;
- asynchronous execution;
- queue pressure;
- concurrency control;
- capacity limits;
- cleanup;
- compatibility constraints;
- degradation to baseline.

### Evaluation

Specify the fairest strong baseline.

A proposal is not strengthened merely by making its own mechanism more complicated. It must also survive comparison against strong alternatives.

At the end of this phase, provide:

> **Strongest reasonable formulation:** ...

and list the important changes made relative to the original idea.

---

## Phase 2 — Extend

Now deliberately leave the user's original formulation.

Ask:

> What broader or adjacent design space becomes visible once we preserve the core insight but relax the current mechanism?

Generate **3–5 meaningful extensions**, not cosmetic variants.

Useful extension moves include:

### Generalize the object

Example:

- one tool-gap optimization
- → lifecycle management for temporarily inactive state
- → hot / warm / cold tiers
- → admission, eviction, offload, recompute, and GC policy

### Generalize the decision

Example:

- binary keep/drop
- → multi-action controller
- → resource-aware admission and migration

### Generalize the scope

Example:

- per-request rule
- → global scheduler interaction
- → service-level policy under contention

### Change the source of information

Example:

- fixed threshold
- → historical statistics
- → workload classification
- → online measurement
- → confidence-aware policy

### Change the objective

Example:

- average latency
- → Goodput under SLO
- → tail latency
- → cost/performance
- → robustness under load

### Change the layer of intervention

Example:

- policy-only change
- → runtime scheduling
- → memory management
- → data placement
- → storage hierarchy
- → kernel/runtime co-design

For each extension, state:

- what changed;
- why it could be stronger;
- what new complexity it introduces;
- whether it still preserves the original core insight.

Do not generate arbitrary novelty. Every extension must have a causal connection to the original problem.

---

## Phase 3 — Adversarial Attack

Attack the **strongest formulations**, not the original rough idea.

For each serious candidate, examine at least the following categories when applicable:

### 1. Mechanism risk

- Is the assumed signal observable?
- Is the action actually controllable?
- Does the mechanism interact badly with scheduling, caching, batching, memory allocation, or concurrency?
- Is the causal path real?

### 2. Economic / performance risk

- Is the optimization opportunity large enough?
- Can the overhead exceed the benefit?
- Is there a regime where a trivial baseline already captures most of the gain?
- Does the mechanism merely move cost elsewhere?

### 3. Prediction / policy risk

- Does the proposal depend on predicting something fundamentally noisy?
- What happens under misprediction?
- Can a robust policy still outperform static rules?

### 4. Engineering risk

- Does the proposal require an invasive fork?
- Does it rely on unavailable instrumentation?
- Does it create correctness or cleanup hazards?
- Is the maintenance surface disproportionate to the gain?

### 5. Evaluation risk

- Can the benefit be measured causally?
- Are the baselines fair?
- Is the workload representative?
- Could the apparent win come from hidden confounders?
- Can the idea survive regime changes?

### 6. Value / novelty risk

- Is the idea already solved upstream?
- Is it merely configuration tuning?
- Is the contribution too narrow?
- Is the result interesting only in a contrived workload?

For every major attack, classify it as one of:

- **Fatal** — invalidates this variant unless a foundational assumption changes.
- **Serious but testable** — requires an experiment or prototype.
- **Mitigable** — can reasonably be handled by design.
- **Non-issue after steelman** — the strong formulation already resolves it.

Do not exaggerate criticism merely to appear adversarial.

---

## Phase 4 — Synthesize

Do not finish with a binary "good idea / bad idea" unless the evidence genuinely supports that conclusion.

Instead, synthesize.

Ask:

1. Which parts of the original insight survived?
2. Which mechanisms should be removed?
3. Which extension created the most value?
4. Which design has the best ratio of:
   - expected value,
   - differentiation,
   - engineering depth,
   - experimentability,
   - implementation cost,
   - risk?
5. What is the smallest version that can falsify the key hypothesis?

Produce **1–3 surviving variants**.

For each surviving variant include:

- **Problem**
- **Core mechanism**
- **Why it is stronger than the original**
- **Main unresolved risk**
- **Minimum decisive experiment**
- **Kill condition**
- **Expansion path if successful**

Prefer a narrow, falsifiable next step over a large architecture with weak evidence.

---

# Branching Rules

## If the original idea is already strong

Do not manufacture unnecessary extensions.

Spend more effort on:

- stronger baselines;
- hidden failure modes;
- evaluation design;
- regime boundaries;
- simplification.

## If the original idea has an obvious flaw

Do not immediately reject it.

First determine whether the flaw belongs to:

- the core insight, or
- only the current implementation.

If the core insight survives, reformulate the mechanism.

If the flaw destroys the core causal hypothesis itself, mark it as fatal and explain why.

## If multiple variants emerge

Do not evaluate them as a flat list.

Group them by the real strategic choice, such as:

- static vs adaptive;
- local vs global;
- policy-only vs runtime modification;
- heuristic vs measurement-driven;
- request-level vs service-level.

Then compare the strongest representative from each branch.

## If evidence is missing

Separate:

- what is known;
- what is inferred;
- what is hypothesized;
- what must be measured.

Never convert uncertainty into confidence merely to keep the brainstorm moving.

---

# Anti-Patterns

Avoid all of the following.

## Strawman rejection

Bad:

> Prediction can be wrong, therefore the idea is useless.

Better:

> The strongest version would use probabilistic estimates and fallback behavior. The remaining question is whether prediction quality is sufficient to outperform a robust static baseline after overhead.

## User-agreement bias

Do not assume the user's preferred direction is correct.

Steelman means "make it strong enough to evaluate fairly," not "find arguments to support it."

## Complexity as sophistication

Do not make the proposal stronger by adding controllers, ML models, queues, tiers, or parameters without demonstrating why they are necessary.

A simpler mechanism with the same causal leverage is preferable.

## Fake generalization

Do not rename a local optimization as a "framework" or "platform" without showing a real reusable abstraction.

## Novelty theater

Do not produce many exotic variants just to appear creative.

Three causally distinct, defensible directions are better than ten superficial ideas.

## Baseline neglect

Always ask whether:

- the default system;
- a static threshold;
- always-do-X;
- never-do-X;
- a simple heuristic

already captures most of the gain.

## Unfalsifiable recommendations

Every surviving direction should have a practical way to prove itself wrong.

---

# Output Contract

Default output structure:

## 1. Core Insight

One short paragraph distinguishing the underlying insight from the current proposal.

## 2. Steelman

The strongest reasonable version of the idea.

Include:

- mechanism;
- required state/signals;
- objective;
- fallback;
- strongest baseline;
- what was changed from the original formulation.

## 3. Extensions

3–5 meaningful branches.

For each:

- idea;
- why it follows from the core insight;
- expected advantage;
- added risk.

## 4. Adversarial Review

Attack the strongest branches.

Focus on the few risks that could actually change the decision.

Classify major risks:

- Fatal
- Serious but testable
- Mitigable
- Non-issue after steelman

## 5. Synthesis

Return:

- the best 1–3 surviving formulations;
- what was discarded;
- why.

## 6. Minimum Next Step

For the top candidate:

- **Hypothesis**
- **Minimal implementation/probe**
- **Baseline**
- **Metric**
- **Success condition**
- **Kill condition**
- **What to do if positive**
- **What to do if negative**

---

# Response Style

Use clear technical language.

Prefer:

- causal reasoning;
- explicit tradeoffs;
- concrete mechanisms;
- compact decision trees;
- equations only when they improve precision;
- small tables only when comparison benefits from them.

Avoid:

- motivational filler;
- excessive terminology;
- repeating the same conclusion in several forms;
- pretending uncertain claims are established facts;
- turning every idea into a large architecture.

The user should be able to understand:

1. why each branch exists;
2. what assumption distinguishes it;
3. where it can fail;
4. what experiment would decide whether to continue.

---

# Compact Invocation Template

When applying this skill internally, use the following reasoning directive:

> Perform a Steelman → Extend → Adversarial Attack → Synthesize brainstorm.
>
> First extract the core insight from the user's current formulation.
> Do not treat the initial implementation as fixed.
>
> Steelman the idea into the strongest realistic version that a strong researcher
> or systems engineer could defend, including necessary mechanisms, uncertainty
> handling, fallback behavior, observability, constraints, and strong baselines.
>
> Then generate 3–5 causally meaningful extensions by generalizing the object,
> decision, scope, information source, objective, or intervention layer.
>
> Attack the strongest variants rather than the original weak formulation.
> Distinguish fatal flaws from testable risks and mitigable engineering issues.
>
> Finally synthesize the best 1–3 surviving formulations and identify the smallest
> decisive experiment for the top candidate, including a success condition and a
> kill condition.
>
> Do not optimize for agreement with the user. Optimize for finding the strongest
> version of the idea that still survives serious scrutiny.

---

# Success Criterion

A successful use of this skill should leave the user with a better answer to:

> "What is the strongest version of this idea that is actually worth testing, and what is the cheapest decisive test that could prove us wrong?"

The skill has failed if it merely:

- praises the original idea;
- attacks an obviously weak version;
- generates a long list of unrelated alternatives;
- adds complexity without causal justification;
- or ends without a falsifiable next step.
