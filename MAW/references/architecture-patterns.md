# Architecture Patterns

## Purpose

This reference provides reusable multi-agent reasoning patterns for Phase 1.

Patterns are **building blocks**, not complete workflows.

The Main Agent should select and combine patterns based on:

- decision-relevant uncertainty;
- evidence structure;
- search structure;
- availability of objective verification;
- expected information gain;
- approved budget.

Do not choose a pattern merely because it is familiar.

Do not force every task into one named architecture.

The usual workflow is:

```text
Task structure
      ↓
Uncertainty / evidence map
      ↓
Select one primary pattern
      +
optional supporting patterns
      ↓
Instantiate task-specific branches
```

---

# 1. Pattern Selection Principles

Before selecting a pattern, ask:

1. What kind of uncertainty dominates the task?
2. What is the natural independent exploration unit?
3. Can different branches genuinely produce decorrelated information?
4. Is there an objective verifier?
5. Does information need to stay isolated initially?
6. Is the task primarily searching, generating, diagnosing, or attacking an existing claim?
7. What failure mode would cause a naive single-agent approach to fail?

Prefer the smallest architecture that addresses the actual failure mode.

More agents and more stages do not imply a better investigation.

---

# 2. Independent Fan-Out

## Core Idea

Launch multiple initially independent branches that attempt the same high-level problem from materially different approaches.

```text
                 Problem
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     Approach A  Approach B  Approach C
        │          │          │
        └──────────┼──────────┘
                   ▼
               Main Reduction
```

The purpose is to increase search breadth and reduce early anchoring.

---

## Use When

Use Independent Fan-Out when:

- the solution space is broad;
- several materially different approaches may work;
- early commitment to one path is risky;
- there is no obvious single decomposition by evidence source;
- independent reasoning itself has value.

Typical tasks:

- difficult mathematical or algorithmic problems;
- research-direction exploration;
- broad technical brainstorming;
- independent architecture assessment;
- alternative design generation.

---

## Avoid When

Avoid or reduce Independent Fan-Out when:

- the task has one narrow factual answer;
- a strong deterministic verifier already identifies the answer cheaply;
- all branches would inspect the same evidence in the same way;
- the main bottleneck is evidence collection rather than reasoning diversity;
- the task can be resolved by one high-information experiment.

Do not create nominally different agents that all perform the same analysis.

---

## Natural Branch Unit

A branch should represent an:

- independent solution strategy;
- independent conceptual framework;
- substantially different interpretation;
- distinct design alternative.

Do not define branches only through different personas.

Bad:

```text
Senior engineer
Principal engineer
Skeptical engineer
```

Better:

```text
Queueing-theoretic explanation
Runtime-level explanation
Algorithmic explanation
```

---

## Information Flow

Initial branches should normally be isolated.

They receive:

- the original task;
- shared constraints;
- their assigned approach.

They should not initially receive:

- conclusions from peer branches;
- the Main Agent's preferred solution.

After completion, Main reduces the results.

---

## Typical Verification

Independent Fan-Out itself does not provide correctness.

Follow it with one of:

- objective verification;
- Generator–Verifier;
- Adversarial Review;
- comparison against primary evidence;
- formal or executable checking.

---

## Strengths

- increases search breadth;
- reduces early-path dependence;
- exposes alternative conceptual frames;
- useful when no single decomposition is obvious.

---

## Failure Modes

### Duplicate search

All agents independently rediscover the same approach.

Mitigation:

> specify materially different exploration objectives.

### False diversity

Different personas produce nearly identical reasoning.

Mitigation:

> differentiate by approach, assumption set, or search region rather than role-playing.

### Expensive weak candidates

Many branches generate low-value ideas.

Mitigation:

> use breadth only until additional branches have low expected information gain.

---

## Good Combinations

Common combinations:

```text
Independent Fan-Out
        +
Generator–Verifier
```

for difficult constructive tasks.

```text
Independent Fan-Out
        +
Adversarial Review
```

for architecture or research evaluation.

---

# 3. Evidence Specialists

## Core Idea

Split the investigation according to heterogeneous evidence sources or evidence domains.

```text
                 Problem
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
     Source        Logs       Profiler
       │            │            │
       └────────────┼────────────┘
                    ▼
             Evidence Reduction
```

The goal is not opinion diversity.

The goal is:

> efficient evidence acquisition with context isolation.

---

## Use When

Use Evidence Specialists when relevant information is distributed across:

- source code;
- logs;
- metrics;
- traces;
- profiler output;
- documentation;
- issue / commit history;
- runtime state;
- external literature;
- different repositories or subsystems.

Especially useful when putting all raw evidence into one Main context would create:

- context explosion;
- irrelevant-data interference;
- poor attention allocation.

Typical tasks:

- production RCA;
- performance diagnosis;
- large-repository investigation;
- distributed-system debugging;
- source + documentation cross-checking.

---

## Avoid When

Avoid separate evidence branches when:

- evidence volume is small;
- all relevant evidence fits naturally into one bounded investigation;
- splitting evidence would destroy necessary correlations;
- one objective experiment can answer the central question directly.

Do not split every file or telemetry type automatically.

---

## Natural Branch Unit

The natural branch unit is:

> a distinct evidence source whose analysis can be performed mostly independently.

Examples:

```text
repository / call-path evidence

runtime logs

distributed trace

GPU profiler

benchmark configuration
```

---

## Information Flow

Initial specialists should focus on evidence extraction, not global conclusions.

They should return:

- what was observed;
- what it supports;
- what it contradicts;
- what was not checked.

The Main Agent performs cross-evidence synthesis.

---

## Typical Verification

Evidence Specialists often feed into:

```text
Evidence Specialists
        ↓
Hypothesis construction
        ↓
Hypothesis–Falsification
```

They are usually not the final verifier themselves.

---

## Strengths

- reduces context pollution;
- allows tool specialization;
- allows parallel evidence acquisition;
- exposes conflicting evidence sources.

---

## Failure Modes

### Evidence silos

Each branch sees only a partial picture and overinterprets it.

Mitigation:

> specialists report evidence and local interpretation; Main performs global causal synthesis.

### Lost correlation

Important timing or causal relationships exist across evidence sources.

Mitigation:

> create a targeted correlation branch after initial reduction when needed.

### Redundant evidence reading

Several branches inspect the same large artifact.

Mitigation:

> clearly assign evidence ownership.

---

## Good Combinations

Most common:

```text
Evidence Specialists
        +
Hypothesis–Falsification
```

Particularly strong for performance and RCA tasks.

---

# 4. Hypothesis–Falsification

## Core Idea

Represent competing explanations explicitly and attempt to eliminate them using distinguishable predictions and evidence.

```text
                 Symptom
                    │
             Hypothesis Set
        ┌───────────┼───────────┐
        ▼           ▼           ▼
       H1          H2          H3
        │           │           │
   predicted    predicted    predicted
   evidence     evidence     evidence
        │           │           │
        ▼           ▼           ▼
     falsify      falsify     falsify
        └───────────┼───────────┘
                    ▼
               Survivors
```

The goal is not to prove each hypothesis.

The goal is to make hypotheses compete against observations.

---

## Use When

Use Hypothesis–Falsification when:

- the task is diagnostic;
- several plausible root causes exist;
- hypotheses predict different observable behavior;
- tests, experiments, traces, or source evidence can distinguish them.

Typical tasks:

- performance regression;
- production incident;
- concurrency bug;
- distributed-system failure;
- unexpected runtime behavior;
- unexplained benchmark results.

---

## Avoid When

Avoid this pattern when:

- there are no meaningful competing explanations;
- hypotheses cannot produce distinguishable predictions;
- the task is mainly constructive rather than diagnostic;
- evidence is unavailable and the process would degrade into competing opinions.

---

## Natural Branch Unit

The natural branch unit is:

> a causal hypothesis or hypothesis family.

Examples:

```text
scheduler-side queueing

communication saturation

kernel inefficiency

CPU synchronization

measurement artifact
```

---

## Information Flow

Early hypothesis branches should normally remain independent.

Each should receive:

- target hypothesis;
- known facts;
- allowed evidence;
- requirement to identify predicted observables.

Do not tell each branch:

> prove this explanation is correct.

Prefer:

> determine whether this explanation survives available evidence.

---

## Typical Verification

The strongest form is:

```text
Hypothesis
    ↓
Predicted observable
    ↓
Objective measurement
    ↓
Survive / weaken / falsify
```

Preferred evidence includes:

- controlled A/B experiments;
- profiler timelines;
- runtime traces;
- reproducers;
- source-level invariant checks.

---

## Strengths

- reduces confirmation bias;
- makes causal reasoning explicit;
- encourages measurable predictions;
- supports branch pruning;
- naturally produces rejected alternatives for the final report.

---

## Failure Modes

### Confirmation search

A branch seeks evidence supporting its assigned hypothesis.

Mitigation:

> frame the branch as falsification, not advocacy.

### Non-discriminating hypotheses

Two branches predict the same evidence.

Mitigation:

> merge them or redefine them at a causally meaningful level.

### Premature hypothesis set

Main generates hypotheses before enough evidence exists.

Mitigation:

> precede with Evidence Specialists when the evidence base is weak.

### Endless hypothesis generation

Every anomaly creates another explanation.

Mitigation:

> apply branch-value and information-gain rules.

---

## Good Combinations

Canonical diagnostic stack:

```text
Evidence Specialists
        ↓
Hypothesis–Falsification
        ↓
Objective Verification
```

For a discovered fix:

```text
Hypothesis–Falsification
        ↓
root cause
        ↓
Generator–Verifier
```

---

# 5. Generator–Verifier

## Core Idea

Separate solution generation from solution falsification or verification.

```text
Generator
    │
    ▼
Candidate
    │
    ▼
Verifier
   /      \
reject    survive
  │
repair
```

The roles are intentionally asymmetric.

Generator asks:

> How can this be solved?

Verifier asks:

> Why might this solution be wrong?

---

## Use When

Use Generator–Verifier when the task produces a concrete candidate that is easier to evaluate than to generate.

Typical tasks:

- mathematical proof;
- code patch;
- algorithm;
- migration plan;
- concrete technical design;
- structured explanation with checkable claims.

---

## Avoid When

Avoid using it as the primary architecture when:

- the task is broad evidence collection;
- there is no meaningful candidate yet;
- no useful verification criteria exist;
- the real uncertainty is which problem should be solved.

In such cases, search or diagnosis should happen first.

---

## Natural Branch Unit

The natural unit is:

> a candidate solution or candidate artifact.

Examples:

```text
proof candidate

patch candidate

algorithm candidate

design candidate
```

---

## Information Flow

The verifier should preferably receive:

- the problem;
- candidate;
- relevant evidence;
- verification criteria.

Avoid giving the verifier the full generator reasoning trace unless necessary.

The verifier should not inherit the generator's assumptions by default.

---

## Typical Verification

Prefer:

```text
formal checker
compiler
tests
reproducer
benchmark
source invariant
```

over purely verbal review.

LLM verifier is most useful when objective verification is incomplete.

---

## Strengths

- separates constructive and destructive objectives;
- reduces self-review anchoring;
- supports bounded repair loops;
- works naturally with objective tools.

---

## Failure Modes

### Verifier becomes a second generator

Verifier starts redesigning the solution instead of checking it.

Mitigation:

> ask for failure location, counterexample, violated assumption, or missing evidence before implementation advice.

### Rubber-stamp verification

Verifier is prompted to “review” and mostly agrees.

Mitigation:

> define an explicit falsification objective.

### Infinite repair loop

Generator and verifier iterate indefinitely.

Mitigation:

> bounded repair/recheck policy.

### Correlated errors

Generator and verifier share the same mistaken assumption.

Mitigation:

> use independent context and objective evidence.

---

## Good Combinations

For difficult constructive search:

```text
Independent Fan-Out
        ↓
candidate selection
        ↓
Generator–Verifier
```

For bug fixing:

```text
Hypothesis–Falsification
        ↓
root cause
        ↓
patch generator
        ↓
test / verifier
```

---

# 6. Adversarial Review

## Core Idea

Take an existing proposal, design, claim, project, or decision and deliberately attack its load-bearing assumptions from materially different failure dimensions.

```text
                  Proposal
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    correctness   feasibility   assumptions
       attack        attack       attack
        │            │            │
        └────────────┼────────────┘
                     ▼
             Critical Decisions
                     │
              targeted defense /
                verification
```

The purpose is not generalized negativity.

The purpose is to identify:

> which assumptions or technical decisions could invalidate the proposal.

---

## Use When

Use Adversarial Review for:

- RFCs;
- architecture proposals;
- research ideas;
- optimization plans;
- project selection;
- engineering designs;
- technical claims already supported by an argument.

Especially useful when the cost of a false positive is high.

---

## Avoid When

Avoid full adversarial decomposition when:

- the proposal is trivial;
- no meaningful decision is being made;
- most technical decisions are low leverage;
- the task is primarily discovery rather than evaluation.

Do not turn every design detail into an independent critic branch.

---

## Natural Branch Unit

Prefer:

> a load-bearing decision, assumption, or review dimension.

Possible review dimensions:

- problem validity / necessity;
- correctness;
- feasibility;
- integration constraints;
- performance economics;
- alternatives / duplication;
- failure modes;
- observability;
- operational risk.

Do not use every dimension automatically.

---

## Information Flow

A useful default is two-stage:

```text
Breadth Review
      ↓
Critical-decision triage
      ↓
Targeted adversarial branches
```

First identify the decisions that matter.

Then spend compute attacking those decisions.

Do not deeply attack every implementation detail.

---

## Typical Verification

Depending on the claim:

- source / upstream implementation;
- benchmark;
- analytical bound;
- controlled experiment;
- integration inspection;
- reproducer;
- failure injection;
- external literature.

A critic's opinion alone should not invalidate a design when stronger evidence is available.

---

## Strengths

- exposes hidden assumptions;
- reduces proposal-author anchoring;
- prioritizes high-impact weaknesses;
- produces defensible “why not” analysis;
- well suited to go / pivot / kill decisions.

---

## Failure Modes

### Adversarial ceremony

Many critics generate superficial objections.

Mitigation:

> each branch should target a specific high-leverage assumption or decision.

### Review explosion

Every design point gets first-principles treatment.

Mitigation:

> breadth triage first; depth only on critical decisions.

### Critic bias

The system treats criticism as inherently stronger than supporting evidence.

Mitigation:

> criticism generates claims to verify; it does not automatically win.

### Missing alternative

The review attacks the current solution but never asks whether better alternatives exist.

Mitigation:

> use an alternatives branch when replacement feasibility materially affects the decision.

---

## Good Combinations

Canonical proposal-review stack:

```text
Independent breadth review
        ↓
Critical-decision triage
        ↓
Adversarial Review
        ↓
Evidence Verification
```

For highly uncertain proposals:

```text
Adversarial Review
        +
Independent alternative generation
```

---

# 7. Debate / Cross-Examination

## Core Idea

Allow agents with conflicting conclusions to exchange targeted objections and responses.

```text
Claim A            Claim B
   │                  │
   └──── challenge ───┘
          │
     cross-examine
          │
          ▼
       Judge / Main
```

This pattern is intentionally **not** the default.

---

## Use When

Use Debate or Cross-Examination when:

- two or more serious interpretations remain after independent work;
- the disagreement is conceptual rather than easily resolved by an objective test;
- each side has meaningful evidence or arguments;
- direct challenge may expose hidden assumptions.

Typical examples:

- architecture tradeoffs without decisive benchmarks;
- interpretation of incomplete evidence;
- conceptual mathematical disagreement before formal verification is available;
- conflicting expert analyses.

---

## Avoid When

Do not use debate when:

- a test can resolve the disagreement;
- a primary source can resolve the disagreement;
- one side has materially stronger objective evidence;
- agents merely repeat opinions;
- debate would destroy useful initial independence.

Prefer:

```text
experiment
```

over:

```text
argument about what the experiment would show
```

---

## Natural Branch Unit

The natural unit is:

> a genuinely contested claim or interpretation.

Do not stage debate between arbitrary personas.

---

## Information Flow

Debate should occur **after** independent positions exist.

Bad:

```text
Agents share everything immediately
→ converge early
```

Better:

```text
Independent analysis
        ↓
Identify genuine disagreement
        ↓
Exchange targeted objections
        ↓
Main evaluates evidence
```

---

## Typical Verification

Debate itself is not verification.

After cross-examination, prefer:

- evidence reconciliation;
- targeted experiment;
- source inspection;
- formal check;
- explicit unresolved status.

---

## Strengths

- exposes assumptions hidden inside competing arguments;
- helps distinguish semantic disagreement from evidence disagreement;
- is useful when no stronger oracle is immediately available.

---

## Failure Modes

### Performative disagreement

Agents may manufacture opposition without introducing different evidence or reasoning.

### Premature convergence

Early sharing can erase the independent positions that made cross-examination useful.

### Consensus masquerading as verification

Agreement after debate still does not establish correctness.

### Excessive rounds

Repeated exchanges can consume budget without changing the evidence state.

---

## Good Combinations

Debate / Cross-Examination combines well with:

- Independent Fan-Out to establish positions before sharing;
- Adversarial Review to target assumptions;
- objective verification whenever a decisive check becomes available.

---

# 8. Pattern Selection Summary

Use the smallest pattern set that matches the task.

| Pattern | Natural branch unit | Prefer when |
|---|---|---|
| Independent Fan-Out | independent approach | several plausible search paths exist |
| Evidence Specialists | evidence source | evidence is heterogeneous |
| Hypothesis–Falsification | causal hypothesis | explanations make distinguishable predictions |
| Generator–Verifier | candidate solution | a candidate can be attacked or checked |
| Adversarial Review | critical decision or assumption | a design contains load-bearing choices |
| Debate / Cross-Examination | contested claim | a real disagreement remains without a strong oracle |

Do not select a pattern because it sounds sophisticated.

Select it only when it changes:

- information independence;
- evidence access;
- falsification power;
- verification quality;
- or search efficiency.

---

# 9. Pattern Composition

Patterns normally form a short pipeline rather than a large fixed team.

Examples:

```text
Evidence Specialists
        ↓
Hypothesis–Falsification
        ↓
Generator–Verifier
```

```text
Independent Fan-Out
        ↓
Adversarial Review
        ↓
Objective verification
```

Keep responsibilities distinct.

Do not let every worker perform every pattern.

---

# 10. Architecture Anti-Patterns

Avoid:

- fixed persona teams unrelated to evidence or uncertainty;
- one agent per file, module, or bullet point without decision relevance;
- debate as the default response to disagreement;
- duplicate reviewers with the same context and objective;
- workflow layers that do not improve evidence or control;
- treating agent count as a quality metric.

If a single investigator plus one verifier is sufficient, use that topology.

---

# 11. Completion Rule

Architecture selection is complete when:

- each branch has a distinct decision-relevant purpose;
- information flow preserves useful independence;
- the verification path is stronger than opinion aggregation;
- the topology fits the approved budget;
- no selected pattern exists only for ceremony.

Return to `planning-and-selection.md` to finish the Execution Spec and Human Review Plan.
