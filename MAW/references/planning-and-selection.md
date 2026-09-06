# Planning and Selection

## Purpose

This reference defines how the Main Agent designs a multi-agent investigation during Phase 1.

Phase 1 answers:

> Given this task, what should be investigated independently, why should those branches exist, how should information flow, and what investigation structure is worth spending budget on?

Phase 1 does **not** execute the investigation.

The output is:

1. a detailed internal Execution Spec;
2. a compressed Human Review Plan for user approval.

The core principle is:

> Decompose the task by decision-relevant uncertainty, not by a predefined list of agent roles.

Phase-1 reconnaissance is Main-only, read-only, and limited to the minimum information needed to define the branch unit and execution envelope. It must not dispatch subagents, run experiments, cause side effects, or collect execution evidence early. If that minimum cannot be learned read-only, state the limitation in the Human Review Plan and wait for the USER GATE.

---

# 1. Frame the Task

Before selecting agents or architectures, establish the task frame.

Identify:

- **Primary question** — what must actually be answered?
- **Decision supported** — what decision will the answer change?
- **Success criteria** — what would constitute a satisfactory resolution?
- **Scope** — what is inside and outside the investigation?
- **Constraints** — time, tools, sources, environments, side effects, evidence limits.
- **Available evidence** — repository, runtime, logs, profiler, literature, tests, user-provided artifacts, etc.
- **Unknown evidence** — important information that may not be accessible.

Do not silently replace the user's question with a nearby but easier question.

When the task contains several questions, identify which are:

- primary;
- supporting;
- optional.

The workflow should optimize for the primary decision.

---

# 2. Characterize the Problem

Use the following characteristics as reasoning aids, not rigid labels.

## 2.1 Truth structure

The task may be:

- **Diagnostic** — identify an unknown cause.
- **Evaluative** — judge an existing design, claim, project, or decision.
- **Constructive** — produce a proof, patch, algorithm, or candidate solution.
- **Factual** — establish what is true from external evidence.
- **Exploratory** — search a broad space of possibilities.
- **Predictive** — estimate future/system behavior under assumptions.

Tasks may combine several types.

Examples:

```text
Performance regression
→ Diagnostic

Technical proposal review
→ Evaluative

Mathematical proof
→ Constructive + verifiable

Research direction exploration
→ Exploratory
```

---

## 2.2 Search structure

Determine whether the problem is dominated by:

- one deep reasoning chain;
- multiple competing hypotheses;
- multiple independent search directions;
- multiple heterogeneous evidence sources;
- multiple high-leverage design decisions.

This influences branch granularity.

---

## 2.3 Verification strength

For each expected claim type, identify the most direct, reliable, and reproducible practical oracle. There is no universal verifier ranking: a runtime-behavior claim normally calls for a controlled test, trace, or reproduction; a contract claim calls for the controlling source or specification; and a proof step calls for a checker or independently checkable derivation. LLM consensus is always weak supporting evidence, never a substitute for the relevant oracle.

---

# 3. Build the Decision / Uncertainty Map

Do not begin by asking:

> Which agents should I create?

Begin by asking:

> Which uncertainties could materially change the final answer?

Represent the problem conceptually as:

```text
Final Decision
     │
     ├─ U1
     ├─ U2
     ├─ U3
     └─ U4
```

An uncertainty may be:

- a competing causal explanation;
- a critical design decision;
- an assumption;
- an unknown system behavior;
- an evidence gap;
- an unresolved tradeoff;
- a possible alternative solution;
- an integration or feasibility risk.

Prefer uncertainties that are **decision-relevant**.

Do not create independent investigation branches for every detail.

---

# 4. Distinguish Evidence Decomposition from Hypothesis Decomposition

These are different search structures.

## Evidence decomposition

Use when useful information is distributed across heterogeneous sources.

Example:

```text
Source code
Logs
Runtime traces
Profiler
History / documentation
```

Natural branch unit:

> evidence source or evidence domain.

Typical purpose:

> build a reliable evidence base without contaminating one context with all raw information.

---

## Hypothesis decomposition

Use when multiple competing explanations already exist or emerge.

Example:

```text
H1 scheduler
H2 communication
H3 kernel efficiency
H4 synchronization
```

Natural branch unit:

> causal hypothesis.

Typical purpose:

> produce distinguishable predictions and attempt falsification.

---

These structures often compose:

```text
Evidence branches
      ↓
Evidence reduction
      ↓
Hypothesis set
      ↓
Targeted falsification branches
```

Do not confuse “different evidence sources” with “different explanations.”

---

# 5. Generate Branch Candidates

A branch is not synonymous with an agent.

A branch is:

> A bounded exploration trajectory with an independent objective, evidence target, and stopping condition.

One branch may require one worker or limited internal local deepening.

Generate branch candidates from:

- competing hypotheses;
- high-leverage design decisions;
- independent evidence domains;
- high-value adversarial attacks;
- distinct solution strategies;
- experiments with high expected information gain.

Avoid generating branches merely because the task contains many files, components, or bullet points.

---

# 6. Decide Whether a Branch Is Worth Opening

Use the following heuristic conceptually:

```text
Branch Value
≈
Leverage
× Uncertainty
× Expected Information Gain
÷ Investigation Cost
```

Do not calculate a numeric score unless there is a specific reason.

For each candidate branch, ask:

### 1. Leverage

If this question resolves differently, could it materially change the final decision?

If not, prefer a sanity check rather than a deep branch.

### 2. Independence

Will this branch produce substantially different information from existing branches?

If not, merge it with another branch.

### 3. Information gain

Is there a plausible investigation, experiment, source, or reasoning path that can reduce uncertainty?

If the branch amounts only to “ask another agent for an opinion,” its value is low.

### 4. Cost

Is the likely information gain worth the context, tool, and inference cost?

Prefer a high-information experiment over several speculative reviewers when possible.

---

# 7. Choose Branch Granularity

Branch granularity must match the task's uncertainty structure.

Possible natural granularities include:

- causal hypothesis;
- evidence source;
- critical technical decision;
- independent solution strategy;
- review dimension;
- subsystem, only when subsystem boundaries align with causal uncertainty.

Do **not** mechanically map:

```text
20 technical decisions
→ 20 branches
```

or:

```text
8 modules
→ 8 agents
```

Prefer:

```text
many low-level details
        ↓
decision / uncertainty triage
        ↓
few high-leverage branches
```

---

# 8. Special Rule for Technical Proposal Review

Do not default to deeply reviewing every technical decision independently.

First perform breadth-oriented triage.

Identify decisions that are:

- high leverage;
- high uncertainty;
- novel or assumption-heavy;
- difficult to reverse;
- likely to dominate feasibility, correctness, or value.

Then allocate deeper branches only to those decisions.

Default conceptual shape:

```text
Proposal
   ↓
Broad review
   ↓
Critical-decision triage
   ↓
D1      D2      D3
│       │       │
deep    deep    verify
review  attack
   \     |      /
      synthesis
```

A low-leverage decision should not receive deep first-principles review merely because such review is possible.

---

# 9. Special Rule for Diagnostic / Performance Tasks

Prefer an explicit causal structure.

For each important hypothesis, ask:

> If this hypothesis were true, what observable evidence should exist?

Where possible, require a **predicted observable**.

Example:

```text
Hypothesis:
communication is the dominant bottleneck

Predicted observable:
timeline should show communication occupying the dominant non-overlapped portion of latency
```

Prefer:

```text
hypothesis
   ↓
predicted observable
   ↓
measurement
   ↓
survive / falsify
```

over static source-level speculation.

For performance tasks, include measurement validity as a possible uncertainty when appropriate.

---

# 10. Select Architecture Patterns

Read `architecture-patterns.md` when necessary.

Select architecture **after** uncertainty and evidence structure are understood.

Patterns may be combined.

Examples:

```text
Bug / RCA

Evidence Specialists
        +
Hypothesis–Falsification
        +
Generator–Verifier for a patch
```

```text
Performance Analysis

Evidence Specialists
        +
Hypothesis–Falsification
        +
Objective Benchmark / Profiler Verification
```

```text
Technical Proposal Review

Independent Review
        +
Adversarial Review
        +
Evidence Verification
```

```text
Mathematical Proof

Independent Generation
        +
Generator–Verifier
        +
Counterexample Search
        +
Formal Verification when available
```

Do not force a task into a single named pattern.

---

# 11. Prefer Breadth Before Targeted Depth

Unless the task naturally has a single candidate solution that mainly needs verification, default to:

```text
independent breadth
      ↓
state reduction
      ↓
identify critical uncertainty
      ↓
targeted depth
```

The purpose of breadth is not agent count.

It is to reduce early anchoring and discover materially different explanations or failure modes.

Stop broad exploration once additional independent branches are unlikely to add meaningful information.

---

# 12. Design Information Isolation

Specify who may see what and when.

Default for genuinely independent first-wave branches:

Workers receive:

- the original task;
- their assigned scope;
- necessary common facts;
- required evidence targets.

They should not receive:

- peer conclusions;
- the Main Agent's preferred hypothesis;
- unnecessary prior reasoning that could anchor the branch.

After the first reduction step, later workers may receive compressed:

- hypothesis cards;
- evidence cards;
- target claims.

Prefer:

```text
raw worker investigation
        ↓
Main reduction
        ↓
compressed shared state
        ↓
next-wave worker
```

over direct transmission of complete worker transcripts.

Direct agent-to-agent debate should be selected intentionally rather than used by default.

---

# 13. Define What Each Branch Returns

Phase 1 should define the information-return policy at an abstract level.

Workers should return decision-relevant branch reports containing:

- conclusion;
- key evidence;
- investigation coverage;
- rejected alternatives;
- residual uncertainty;
- suggested next investigation.

They should not return unrestricted reasoning transcripts by default.

The Main Agent needs to know:

> What did this branch establish, what did it actually inspect, what did it rule out, and what remains unknown?

not:

> Every intermediate thought the worker generated.

Detailed execution rules live in `execution-control.md`.

---

# 14. Define Branch Expansion Policy

Phase 1 does not need to predict every future branch.

Instead define the rule under which new branches may be admitted.

A new branch is normally justified when it is:

- materially relevant to the final answer;
- not substantially duplicated by current work;
- still uncertain;
- associated with meaningful expected information gain;
- inside the approved execution envelope.

Workers may discover and propose new directions.

Global branch admission belongs to the Main Agent.

Distinguish:

```text
local deepening
→ worker autonomy

new global direction inside envelope
→ Main autonomy

material expansion outside envelope
→ USER GATE
```

---

# 15. Map Evidence and Verification Before Execution

Before finalizing the topology, identify how important claims could eventually be verified.

For each expected load-bearing question, ask:

```text
Question / Claim
        ↓
Best available evidence
        ↓
Potential verifier
```

Examples:

```text
"Upstream already implements this"
→ source / RFC

"Scheduler causes the bubble"
→ scheduler + CPU/GPU trace

"Patch fixes the bug"
→ reproducer + tests

"Optimization improves performance"
→ controlled A/B benchmark

"Proof step is valid"
→ formal checker / independent proof
```

This prevents an investigation from reaching Phase 3 with claims that were never designed to be testable.

---

# 16. Choose the Budget Envelope

Unless the user specifies otherwise, default to the Medium profile defined in `SKILL.md`.

The following are the authoritative **Medium planning priors** for this Skill:

- initial Independent Fan-Out: roughly 3–5 branches when justified;
- investigation: normally up to two waves, with roughly 2–3 targeted follow-up branches when justified;
- verification: roughly 1–2 bundled checks;
- targeted repair/recheck of a load-bearing claim: normally one bounded round.

These are planning aids, not quotas or automatic escalation thresholds. A smaller topology is correct for a narrow task; a third small dependency wave is not automatically material. Assess materiality from aggregate breadth, depth, verification consumption, resources, side effects, scope, and user-visible strategy as defined in `execution-control.md`.

Budget is best understood along three dimensions:

```text
Breadth
Depth
Verification intensity
```

Do not optimize for filling the maximum number of branches.

Plan enough independent search to reduce anchoring, then concentrate budget on high-value uncertainty.

If a narrow task does not justify broad multi-agent search, explicitly recommend a smaller topology even though the skill was invoked.

---

# 17. Define Stop Criteria Before Execution

Avoid open-ended search.

At planning time, define conditions such as:

- key uncertainties are closed;
- one explanation survives while major alternatives are falsified;
- load-bearing claims have identifiable verification paths;
- evidence has saturated;
- remaining uncertainty requires inaccessible evidence;
- expected information gain of another branch is low;
- approved budget is exhausted.

`Unknown` and `insufficient evidence` are valid terminal states.

Do not design a workflow that requires certainty when the available evidence cannot support certainty.

---

# 18. Build the Detailed Execution Spec

The internal Execution Spec should capture enough structure for Phase 2.

It should normally contain:

```text
Task goal

Success criteria

Approved scope

Selected architecture

Branch granularity

Initial branches

Dependencies / waves

Information-isolation rules

Branch return policy

Evidence targets

Allowed evidence sources

Allowed tools / resources

Side-effect boundary

Verification plan

Expansion policy

Budget envelope

Stop criteria
```

Individual branch definitions may additionally include:

```text
Question

Motivation

Scope

Known context

Evidence target

Allowed evidence sources

Allowed tools / resources

Side-effect boundary

Isolation rule

Return contract

Stop condition

Budget bound

Dependencies
```

Do not expose all of this detail to the user by default.

---

# 19. Compress into the Human Review Plan

The Human Review Plan is a human-facing abstraction of the Execution Spec.

Optimize it for:

> fast understanding of the search strategy.

The user should be able to answer:

- Why is the problem being divided this way?
- What will be explored independently?
- Where may deeper branches open?
- What will come back from those branches?
- How will the important conclusions be checked?
- What level of resource use is being authorized?
- Which evidence, tools/resources, and side effects are authorized?
- What changes would require a revised plan and renewed execution approval?

Default structure:

## Goal

What decision/question will be resolved?

## Overall approach

Explain the search strategy in natural language.

Examples:

> First perform a broad independent review across the major dimensions that could change the final decision. After the first wave, only high-impact and still-uncertain decisions will receive deep adversarial branches.

or:

> First collect independent source, trace, and profiler evidence. The Main Agent will then construct competing causal hypotheses and open targeted falsification branches only for the strongest candidates.

## Branch granularity

State explicitly what defines a branch and why that granularity was chosen.

## Branch expansion

Explain what type of discovery is allowed to create another branch.

## Information return

Explain at a high level that branches return conclusions, evidence, coverage, rejected alternatives, and residual uncertainty rather than full transcripts.

## Verification

Explain how load-bearing conclusions are expected to be checked.

## Budget

State the budget class and approximate aggregate breadth/depth/verification envelope. Treat default wave limits as soft planning priors; materiality is assessed from total consumption, resources, side effects, scope, and user-visible strategy.

## Conceptual diagram

For Medium and High investigations, provide a small diagram showing the search logic.

Example:

```text
Broad independent scan
   ├─ A
   ├─ B
   └─ C
        ↓
Main reduction
        ↓
Critical uncertainties
   ├─ D1 deep review
   └─ D2 falsification
        ↓
Verification
        ↓
Final synthesis
```

The diagram should explain the reasoning structure, not reproduce the exact runtime DAG.

---

# 20. Human Review Burden Is a Design Constraint

Do not expose complexity merely because the internal plan is complex.

The planning process should optimize both:

```text
investigation quality ↑

human review burden ↓
```

Detailed execution information remains available on request.

The default Human Review Plan should normally fit within a compact, quickly reviewable response.

If the plan cannot be explained simply, first ask whether the workflow itself is unnecessarily complicated.

---

# 21. Phase-1 Self Review

Before presenting the plan, the Main Agent should check:

- Does every planned branch address a materially different uncertainty?
- Are any branches redundant?
- Is the chosen branch granularity decision-relevant?
- Are high-leverage assumptions exposed?
- Are first-wave branches independent where independence matters?
- Is there a strong evidence target for important claims?
- Is unnecessary debate being introduced?
- Is the topology larger than the task justifies?
- Are stop criteria explicit?
- Can branches be merged or pruned later?
- Is the expected verification strategy strong enough?
- Can the Human Review Plan be understood without reading the detailed Execution Spec?

If not, revise the plan before presenting it.

---

# 22. Phase-1 Completion

Phase 1 is complete when:

1. the internal Execution Spec is coherent;
2. the Human Review Plan accurately compresses it;
3. the approved execution envelope is clear enough for the user to review.

Return the Human Review Plan and stop.

Execution approval is governed by `SKILL.md`.
