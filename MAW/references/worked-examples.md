# Worked Examples

## Purpose

This reference provides a small set of canonical examples for Phase 1 when the Main Agent is uncertain about:

- branch granularity;
- architecture selection;
- breadth-versus-depth balance;
- information isolation;
- verification strategy.

Do **not** load this reference during routine execution when the investigation structure is already clear.

These examples are not fixed workflows.

Their purpose is to demonstrate:

> how to move from task structure → uncertainty decomposition → branch strategy → verification.

Do not copy agent counts or branch names mechanically.

---

# Example 1 — Performance Diagnosis

## Task

A distributed inference workload shows:

> TP=2 has worse latency than TP=1.

The goal is to identify the dominant cause rather than merely list possible reasons.

---

## Task Characteristics

```text
Type:
Diagnostic

Search structure:
Multiple plausible causal explanations

Evidence:
source
runtime configuration
profiler / timeline
benchmark results

Verification strength:
strong objective measurement available
```

Potential causal families include:

- scheduler / batching;
- communication;
- kernel efficiency;
- synchronization / CPU dispatch;
- benchmark or configuration artifact.

---

## Bad Decomposition

A naive workflow might create:

```text
Agent 1 → scheduler code
Agent 2 → NCCL code
Agent 3 → CUDA kernels
Agent 4 → memory allocator
Agent 5 → CPU code
Agent 6 → reviewer
Agent 7 → another reviewer
```

This is weak because it maps branches to components before establishing which uncertainties matter.

It may:

- duplicate large amounts of source reading;
- miss measurement validity;
- produce static speculation;
- spend equal effort on low- and high-probability causes.

---

## Better Branch Granularity

Use two stages.

### Stage A — Evidence acquisition

Separate only genuinely heterogeneous evidence.

```text
Source / scheduler behavior
Profiler / GPU timeline
Benchmark / configuration sanity
Communication evidence
```

The first stage should answer:

> what was actually observed?

rather than:

> what is definitely the root cause?

---

### Stage B — Causal hypotheses

After Main reduces the evidence, instantiate only hypotheses still capable of explaining the observed delta.

Example:

```text
H1 scheduler-side queueing

H2 communication overhead

H3 CPU launch / synchronization
```

Each hypothesis should define a predicted observable.

Example:

```text
H2:
communication is dominant

Prediction:
the non-overlapped communication interval should explain
a large fraction of the TP=1 → TP=2 latency delta.
```

---

## Selected Architecture

```text
Measurement sanity
        +
Evidence Specialists
        ↓
Main evidence reduction
        ↓
Hypothesis–Falsification
        ↓
Profiler / benchmark verification
```

Primary pattern:

> Hypothesis–Falsification

Supporting pattern:

> Evidence Specialists

---

## Information Isolation

First-wave evidence branches should not be told:

> Main currently suspects NCCL.

They receive only:

- symptom;
- assigned evidence source;
- configuration;
- relevant scope.

This reduces confirmation bias.

After evidence reduction, second-wave falsifiers may receive compressed hypothesis cards.

---

## Example Human Review Plan

> **Overall approach:** first separate measurement/configuration validity from the major runtime evidence sources instead of immediately choosing a suspected bottleneck. After those branches return, I will construct only the causal hypotheses that remain consistent with the observations and spend the second wave trying to falsify the strongest ones.
>
> **Branch granularity:** the first wave is divided by heterogeneous evidence source; the second wave is divided by competing root-cause hypothesis. This avoids assigning one agent to every code subsystem.
>
> **Expansion rule:** a new branch opens only if the first-wave evidence reveals a distinct causal explanation that could materially account for the latency delta and has a measurable prediction.
>
> **Return:** each branch reports its scoped conclusion, key measurements/source evidence, what it checked, what it ruled out, and what remains unresolved.
>
> **Verification:** final root-cause claims should survive profiler/trace or controlled A/B evidence rather than reviewer consensus.
>
> **Budget:** Medium; roughly 3–5 first-wave branches, at most one targeted second wave.

```text
Evidence
 ├─ source
 ├─ profiler
 ├─ communication
 └─ benchmark sanity
       ↓
Main reduction
       ↓
H1 / H2 / H3
       ↓
targeted falsification
       ↓
root-cause verification
```

---

## Important Branch Decision

Suppose the communication branch reports:

> NCCL time is only a small fraction of the latency delta.

Meanwhile the profiler branch reports:

> the major idle interval occurs before the collective.

Do not open:

```text
another NCCL reviewer
```

Instead:

```text
prune dominant-NCCL hypothesis
        ↓
reallocate budget toward scheduler / CPU dispatch
```

The branch tree should shrink as evidence improves.

---

## Verification Closure

A valid final state might be:

```text
Scheduler/CPU-dispatch family:
strongly supported

Dominant NCCL saturation:
falsified

Kernel inefficiency:
not material under tested workload

Exact scheduler-vs-CPU synchronization split:
partially unresolved
```

The final answer should preserve the unresolved boundary rather than claim more precision than the evidence supports.

---

## What Would Be Wasteful

Avoid:

- one agent per subsystem before measurement;
- multiple generic performance reviewers;
- debating whether NCCL is expensive without profiling it;
- continuing to investigate a falsified cause;
- treating one benchmark improvement as proof of the proposed mechanism;
- spending the entire budget before reserving verification capacity.

---

# Example 2 — Technical Proposal / Architecture Review

## Task

Review a proposed KV-cache controller that chooses among:

```text
retain
offload
recompute
```

The goal is to decide whether the proposal should:

```text
proceed
proceed with conditions
pivot
or stop
```

---

## Task Characteristics

```text
Type:
Evaluative

Search structure:
Many design decisions, but only some are load-bearing

Evidence:
proposal
source / upstream implementation
runtime architecture
performance assumptions
prior systems / literature

Verification strength:
mixed
```

The main danger is review explosion:

> treating every implementation choice as deserving a deep adversarial branch.

---

## Bad Decomposition

Suppose the proposal contains 18 technical decisions.

A poor workflow creates:

```text
18 decision branches
×
first-principles critic
×
alternative-design agent
×
verifier
```

This is expensive and usually unnecessary.

Most decisions do not independently determine whether the proposal is worth pursuing.

---

## Better Branch Granularity

Start with **breadth-oriented review dimensions** that can independently change the final decision.

Example:

```text
Problem validity / necessity

Core mechanism and assumptions

Runtime / integration feasibility

Performance economics

Upstream duplication / alternatives
```

The first wave identifies **critical decisions**.

Example:

```text
D1:
required lifecycle state may not be observable

D2:
offload-vs-recompute break-even assumption may be wrong

D3:
scheduler integration seam may require an invasive fork
```

Only D1–D3 receive deep second-wave analysis.

---

## Selected Architecture

```text
Independent breadth review
        ↓
Critical-decision triage
        ↓
Adversarial Review
        ↓
Targeted evidence verification
```

Primary pattern:

> Adversarial Review

Supporting patterns:

> Independent Fan-Out

> Evidence verification

---

## Why Not One Agent per Component?

The question is not:

> Is each component internally reasonable?

The question is:

> Which assumptions or technical decisions could invalidate the proposal?

Therefore the natural branch unit is:

> high-leverage review dimension first, then critical decision.

---

## Example Human Review Plan

> **Overall approach:** I will not deeply audit every implementation detail. The first wave will independently review the few dimensions that can change the go/pivot/kill decision: whether the problem is real, whether the core mechanism is sound, whether a practical integration seam exists, whether the economics can produce a useful regime, and whether upstream or simpler alternatives already cover the value.
>
> **Branch granularity:** initial branches are review dimensions rather than modules. After the first wave, only high-impact and still-uncertain design decisions will receive dedicated first-principles or adversarial branches.
>
> **Expansion rule:** a decision becomes a deep branch only if being wrong could materially invalidate the proposal and additional evidence can reduce that uncertainty.
>
> **Return:** branches report conclusion, source/evidence, reviewed scope, rejected objections, remaining uncertainty, and any critical decision that deserves deeper review.
>
> **Verification:** load-bearing claims such as observability, integration feasibility, and performance break-even will be checked against source/runtime evidence or experiments when available.
>
> **Budget:** Medium; broad first wave followed by at most one targeted deep-review wave.

```text
Proposal
   ↓
Broad review
 ├─ necessity
 ├─ mechanism
 ├─ integration
 ├─ economics
 └─ alternatives
       ↓
critical-decision triage
       ↓
D1 / D2 / D3
       ↓
targeted attack + verification
       ↓
go / conditional / pivot / kill
```

---

## Important Branch Decision

Suppose the breadth review identifies:

```text
D1 observability
D2 offload economics
D3 naming / trace schema detail
```

D1 and D2 are high leverage.

D3 is not.

Correct:

```text
deep branch D1
deep branch D2
sanity-check D3 only if needed
```

Incorrect:

```text
give D3 equal adversarial-review budget because it is a "technical decision"
```

---

## Verification Closure

A plausible result:

```text
Problem validity:
verified

Integration seam:
conditionally verified

Observability:
not established

Offload economics:
verified only in regime R

Upstream duplication:
falsified as a fatal objection
```

Final disposition:

```text
PROCEED WITH CONDITIONS
```

with the conditions explicitly tied to observability and regime validation.

---

## What Would Be Wasteful

Avoid:

- first-principles review of every design choice;
- rewarding critics merely for finding objections;
- generic “architect / skeptic / principal engineer” personas;
- asking several agents whether the design “feels useful”;
- treating roadmap ideas as validated engineering evidence;
- ignoring simpler alternatives because the assigned task is to review the proposed solution.

---

# Example 3 — Bug / Root-Cause Analysis

## Task

A concurrent cache occasionally crashes under load.

Relevant information may exist in:

- source code;
- test logs;
- server logs;
- runtime traces;
- concurrency behavior.

The goal is to establish root cause and, if appropriate, validate a fix.

---

## Task Characteristics

```text
Type:
Diagnostic
then possibly Constructive

Search structure:
multiple plausible causes

Evidence:
heterogeneous runtime + source evidence

Verification:
reproducer / sanitizer / tests potentially strong
```

---

## Initial Uncertainty

Potential causal families:

```text
lifetime / use-after-free

race condition

incorrect locking

retry / timeout interaction

cache eviction state transition
```

Do not immediately create one advocate agent for every guessed cause if the evidence base is still weak.

---

## Selected Architecture

```text
Evidence Specialists
        ↓
Main reduction
        ↓
Hypothesis–Falsification
        ↓
Root cause
        ↓
Generator–Verifier for fix
```

This task naturally changes architecture after root cause is established.

---

## First-Wave Granularity

Example:

```text
Source / ownership path

Failure logs / runtime trace

Concurrency / synchronization evidence

Reproducer / test behavior
```

Each branch extracts evidence without being told the preferred root cause.

---

## Second-Wave Granularity

After reduction:

```text
H1 lifetime race

H2 lock coverage gap

H3 invalid eviction transition
```

Each should seek evidence capable of falsifying its assigned explanation.

---

## Example Human Review Plan

> **Overall approach:** first separate runtime evidence, ownership/source behavior, synchronization behavior, and reproducer/test evidence. I will use those results to construct a smaller set of competing causal hypotheses instead of asking several agents to guess the crash independently from the same logs.
>
> **Branch granularity:** first wave by evidence domain; second wave by causal hypothesis. If one cause survives, any patch work becomes a separate Generator–Verifier stage.
>
> **Expansion rule:** a new root-cause branch opens only when new evidence implies a materially different failure mechanism and provides a concrete way to distinguish it.
>
> **Return:** branches return observations, evidence locations, checked/not-checked coverage, rejected causes, and remaining uncertainty.
>
> **Verification:** root cause should preferably survive a reproducer, sanitizer, controlled failure test, or other executable evidence. Any patch must then pass the relevant correctness verifier.
>
> **Budget:** Medium.

```text
source / logs / runtime / tests
          ↓
      evidence state
          ↓
     H1 / H2 / H3
          ↓
     falsification
          ↓
       root cause
          ↓
     patch generator
          ↓
  sanitizer / tests
```

---

## Important Branch Decision

Suppose a source branch proposes:

> missing mutex causes the crash.

A runtime branch finds:

> the dereferenced object can already be freed before the lock-sensitive section.

Do not simply let two agents debate:

```text
mutex vs lifetime
```

Instead ask:

> What reproducer or sanitizer observation distinguishes them?

If ASAN/TSAN or a deterministic reproducer identifies use-after-free:

```text
objective evidence dominates the verbal disagreement.
```

---

## Generator–Verifier Transition

Once root cause is sufficiently established:

```text
Generator:
produce minimal fix

Verifier:
attempt to break fix

Objective checks:
unit tests
stress test
sanitizer
reproducer
```

The verifier should first identify correctness failure rather than redesigning the entire cache subsystem.

---

## Verification Closure

Possible result:

```text
Root cause:
object lifetime violation

Lock-gap explanation:
weakened / secondary

Reproducer:
passes before fix with failure,
no longer reproduces after fix

Sanitizer:
clean under tested workload

Residual risk:
rare shutdown path not covered
```

The final answer should not claim universal correctness beyond the tested boundary.

---

## What Would Be Wasteful

Avoid:

- dumping all logs into every worker;
- letting each agent invent a root cause independently without evidence ownership;
- fixing before causal evidence is strong enough;
- treating "tests pass" as proof the diagnosed mechanism was correct;
- allowing verifier failure to trigger a full subsystem redesign automatically;
- repeated worker retries when the branch itself is badly framed.

---

# Example 4 — Mathematical Proof

## Task

Prove a difficult mathematical claim.

The task has a large search space, and candidate proofs are easier to inspect than to discover.

---

## Task Characteristics

```text
Type:
Constructive

Search structure:
multiple independent solution paths

Evidence / verification:
counterexample search
symbolic / numerical checks
formal verification when available
```

The primary risk is early commitment to one proof strategy.

---

## Bad Decomposition

Weak:

```text
Solver
Reviewer
Judge
```

when the solver is the only source of candidate ideas.

This may search deeply but narrowly.

Also weak:

```text
10 solvers
→ majority vote on proof
```

A proof is not correct because many agents like it.

---

## Better Branch Granularity

Initial branches should represent materially different proof strategies.

Example:

```text
direct analytic approach

contradiction

induction / recursive structure

algebraic reduction

known-theorem reduction
```

Do not create branches simply by changing persona or temperature if they are expected to pursue the same argument.

---

## Selected Architecture

```text
Independent Fan-Out
        ↓
candidate triage
        ↓
Generator–Verifier
        ↓
Counterexample / boundary attack
        ↓
Formal verification when available
```

Primary pattern:

> Independent Fan-Out

Then:

> Generator–Verifier

---

## Information Isolation

Initial solvers should not see peer proof attempts.

This protects search diversity.

After the first wave, Main may reduce candidates into:

```text
Candidate A
core idea
critical lemma
known gap

Candidate B
...
```

Verification should focus on the strongest candidate rather than forcing every candidate through a complete formal review.

---

## Example Human Review Plan

> **Overall approach:** use a small set of initially independent proof strategies to avoid anchoring on the first plausible route. After the first wave, I will keep only the strongest candidate or candidates and spend most of the remaining budget on adversarial checking rather than continuing broad generation.
>
> **Branch granularity:** one branch per materially different proof strategy, not one per mathematical sub-expression or reviewer persona.
>
> **Expansion rule:** additional proof branches open only if the first wave exposes a genuinely new strategy or all current candidates fail for different reasons.
>
> **Return:** each solver returns the proof idea, critical lemmas, assumptions, unresolved gaps, and any counterexamples encountered.
>
> **Verification:** candidate proofs are checked by independent falsification, counterexample search, and formal verification when practical.
>
> **Budget:** Medium unless the user explicitly requests large-scale search.

```text
Independent proof strategies
  ├─ A
  ├─ B
  ├─ C
  └─ D
       ↓
candidate triage
       ↓
strongest candidate
       ↓
Verifier + counterexample search
       ↓
formal check if available
       ↓
verified / gap / falsified
```

---

## Important Branch Decision

Suppose:

```text
A fails immediately
B reaches a promising lemma
C duplicates B
D produces a different valid-looking reduction
```

Correct:

```text
prune A
merge C into B
keep B and D
allocate verification budget
```

Incorrect:

```text
open four more solvers simply because generation budget remains
```

---

## Verification Closure

Possible result:

```text
Candidate B:
falsified by boundary case

Candidate D:
core argument survives independent verification

Critical lemma:
formally verified

Remaining step:
informal but independently reproduced
```

Final status should reflect the weakest load-bearing step.

For example:

```text
PROOF HAS A REMAINING GAP
```

rather than:

> proof verified

if one critical step remains unverified.

---

## What Would Be Wasteful

Avoid:

- solvers sharing early proof ideas;
- majority vote over correctness;
- verifying every weak candidate;
- unlimited generate-review-repair loops;
- debate when a formal checker can resolve the issue;
- forcing a successful proof when the correct result is "no proof established."

---

# Cross-Example Lessons

These examples differ in domain, but the same principles recur.

## 1. Branch by uncertainty, not organizational structure

```text
Performance:
evidence source → causal hypothesis

Proposal review:
review dimension → critical decision

RCA:
evidence source → causal hypothesis → fix candidate

Proof:
independent solution strategy → candidate
```

---

## 2. Breadth has a purpose

Breadth is used to reduce early anchoring and expose materially different candidates.

It should stop when additional branches are unlikely to add new information.

---

## 3. Depth follows leverage

Deep branches should concentrate on:

- surviving causal hypotheses;
- load-bearing design decisions;
- promising candidate solutions;
- critical unresolved assumptions.

Do not distribute equal depth across low- and high-value branches.

---

## 4. Evidence determines the architecture

When an objective test exists, use it.

When evidence is heterogeneous, separate evidence acquisition.

When explanations compete, require predicted observables and falsification.

When a candidate exists, separate generation from verification.

When no strong oracle exists, use adversarial exchange carefully and preserve unresolved status.

---

## 5. Verification is asymmetric

Phase 3 does not repeat Phase 2.

It checks the claims whose failure would materially change the final answer.

Weak candidates and already-pruned branches do not automatically receive equal verification budget.

---

## 6. Compression preserves control

Workers return Branch Reports.

Main reduces them into Global Investigation State.

Phase 3 produces a Verification Closure.

Phase 4 returns a compact Decision View.

This compression keeps raw local exploration from consuming the Main context or the user's attention.

---

## 7. Unknown is a valid outcome

A multi-agent workflow is not successful merely because it produces a confident answer.

Valid outcomes include:

- conditionally supported;
- narrowed;
- unresolved;
- blocked by missing evidence;
- no proof established.

---

# How to Use These Examples

Read this file only when branch granularity, architecture selection, or information flow remains unclear after reading the authoritative phase reference.

Use the examples to compare task structure.

Do not copy:

- agent counts;
- branch labels;
- domain-specific evidence;
- exact diagrams;
- exact sequencing.

The current task's uncertainty and evidence structure remain authoritative.
