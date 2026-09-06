# Execution Control

## Purpose

This reference defines how the Main Agent executes an approved multi-agent investigation during Phase 2.

Phase 1 answers:

> What investigation should be run?

Phase 2 answers:

> How should the approved investigation adapt, branch, merge, prune, and stop without losing evidence discipline, budget control, or human oversight?

The core execution loop is:

```text
Approved Execution Envelope
          ↓
Initialize Global Investigation State
          ↓
Open dependency-ready branches
          ↓
Workers perform local exploration
          ↓
Structured Branch Reports
          ↓
Main performs State Reduction
          ↓
merge / prune / update / reprioritize
          ↓
continue only if another branch has sufficient value
```

Phase 2 should behave as a controlled search process, not an uncontrolled agent swarm.

The authority rules in `SKILL.md` remain binding.

---

# 1. Approved Execution Envelope

Before execution begins, translate the user-approved Phase-1 plan into an explicit execution envelope.

The envelope should capture:

```text
Task goal

Success criteria

Scope

Budget class

Breadth allowance

Depth / wave allowance

Verification allowance

Allowed evidence sources

Allowed tools / resources

Side-effect boundary

Expansion boundary

Stop criteria
```

The execution envelope is a **boundary for autonomy**, not a frozen DAG.

The Main Agent MAY inside the envelope:

- replace a low-value branch;
- merge overlapping branches;
- prune branches;
- reprioritize work;
- alter branch ordering;
- open newly discovered high-value branches;
- use fewer agents than originally estimated.

The Main Agent MUST NOT silently cross the envelope through material deviation.

---

# 2. Budget Interpretation

Budget is a ceiling, never a quota.

Do not create work merely because capacity remains.

Think about budget in three dimensions:

```text
Breadth
How many genuinely independent directions can be explored?

Depth
How many rounds of targeted deepening are allowed?

Verification allowance
How much later checking has been reserved?
```

Preserve enough budget for verification.

Do not consume the entire approved budget during initial exploration if important claims will still require Phase-3 verification.

For the default Medium profile, use the planning priors in `planning-and-selection.md` as priors rather than exact quotas.

---

# 3. Branch as the Execution Unit

A branch is a bounded investigation trajectory.

A branch is not necessarily identical to one worker process.

The branch should exist because it addresses a materially distinct uncertainty, evidence domain, hypothesis, decision, or search direction.

Conceptually:

```text
Global Investigation
      │
      ├── Branch B1
      ├── Branch B2
      └── Branch B3
```

A branch may perform local deepening internally, but its global purpose should remain stable.

---

# 4. BranchSpec

Before dispatching a branch, define enough of a BranchSpec to prevent vague or duplicative work.

A BranchSpec inherits the approved execution envelope. It must state the applicable limits when they are narrower or not obvious. A worker may use **only** the evidence sources, tools/resources, and side effects named by its BranchSpec or inherited from the envelope; an allowed tool does not authorize a new tool category, resource, or side effect. Host safety and permission rules remain stricter when applicable.

A BranchSpec should normally contain:

## Branch question

What specific uncertainty should this branch reduce?

## Motivation

Why does resolving this question matter to the final task?

## Scope

What is inside this branch?

What adjacent problems should it avoid taking ownership of?

## Known context

What established facts or constraints should the worker know?

Do not provide unnecessary peer conclusions that would compromise useful independence.

## Evidence target

What evidence would materially change the branch conclusion?

Examples:

- source location;
- trace pattern;
- benchmark difference;
- counterexample;
- reproducer;
- primary-source confirmation.

## Allowed evidence sources

Which approved sources may support the branch, and which sources are out of bounds?

## Allowed tools / resources

Which exact approved tools and resources may be used? Do not write a broad capability label that a worker could interpret as permission to choose new tools.

## Side-effect boundary

What read/write, external, compute, or other side effects are permitted? If none are permitted, say `read-only`.

## Isolation rule

What information should the branch not receive yet?

## Return contract

What decision-relevant information must come back?

## Stop condition

When should the branch return rather than continue exploring?

## Budget bound

What amount of local exploration is proportionate?

## Dependencies

What previous branch or state, if any, must exist before this branch can start?

A branch does not need all fields written verbatim when obvious.

The purpose is disciplined task construction, not schema ceremony.

---

# 5. Branch Lifecycle

Use a small conceptual lifecycle.

```text
PLANNED
   ↓
ACTIVE
   ↓
RESOLVED / BLOCKED
```

A resolved branch may end as:

```text
SUPPORTED
FALSIFIED
INCONCLUSIVE
NO MATERIAL FINDING
NEW_DIRECTION_PROPOSED
```

These statuses describe the branch outcome, not necessarily the final global conclusion.

For example:

```text
Branch:
"Could NCCL saturation explain the slowdown?"

Outcome:
FALSIFIED
```

does not mean:

> the entire performance investigation is resolved.

---

# 6. Dependency-Aware Waves

Execute branches according to causal or informational dependency.

Parallelize only work that does not require results from another branch.

Good:

```text
Wave 1

Source ─────┐
Trace ──────┼── independent evidence collection
Profiler ───┘

              ↓

Main Reduction

              ↓

Wave 2

H1 falsifier
H2 falsifier
```

Avoid:

```text
evidence collection
hypothesis construction
falsification
verification
```

all starting simultaneously when later stages depend on earlier evidence.

A wave is a reasoning synchronization boundary, not merely a batch of tool calls.

---

# 7. Safe Parallelism

Parallel work is valuable when it creates:

- independent search;
- independent evidence acquisition;
- context isolation;
- genuinely separate hypotheses;
- reduced wall-clock latency without increasing reasoning dependence.

Parallelism is not valuable when branches:

- repeatedly read the same artifacts;
- depend on each other's results;
- differ only by persona;
- are likely to produce identical information;
- should instead be one deeper branch.

Optimize for independent information gain, not maximum concurrency.

---

# 8. Worker Local Autonomy

Workers should have meaningful autonomy inside the assigned branch.

A worker MAY:

- inspect additional relevant files;
- follow local call paths;
- run bounded experiments;
- test local hypotheses;
- read supporting documentation;
- use approved tools;
- pursue a locally discovered sub-question necessary to answer the branch.

This is **local deepening**.

Example:

```text
Branch:
"Does scheduler batching explain the observed idle gap?"

Worker:
read scheduler
→ inspect queue transition
→ inspect dependent helper
→ compare trace
→ run small local check
```

The worker does not need Main approval for each local step.

---

# 9. Global Branching Is Owned by Main

A worker that discovers a materially new direction should not recursively expand the global search tree.

Instead it should return a branch proposal.

Example:

```text
NEW DIRECTION PROPOSAL

Question:
Could CPU/NCCL stream synchronization explain the idle gap?

Why material:
The observed gap precedes the collective and is not explained
by the assigned scheduler hypothesis.

Evidence:
...

Suggested evidence:
CPU/GPU correlated timeline
```

Main decides whether to:

```text
OPEN
MERGE
DEFER
REJECT
```

the proposed branch.

Use this rule:

```text
local detail
→ worker autonomy

new global direction inside envelope
→ Main autonomy

material expansion outside envelope
→ USER GATE
```

---

# 10. BranchReport

Workers should return compact Branch Reports rather than unrestricted reasoning transcripts.

The default structure is:

```text
Status

Conclusion

Key Evidence

Coverage
- checked
- not checked

Rejected Alternatives

Residual Uncertainty

Suggested Next Investigation
```

---

## Status

Examples:

```text
SUPPORTED
FALSIFIED
INCONCLUSIVE
BLOCKED
NO MATERIAL FINDING
```

---

## Conclusion

State the strongest branch-level conclusion supported by the investigation.

Keep it scoped.

Bad:

> Communication is not a problem.

Better:

> Under the inspected TP=2 trace, non-overlapped NCCL time is too small to explain most of the observed latency delta.

---

## Key Evidence

Return decision-relevant evidence, not generic assertions.

Useful evidence may include:

- source locations;
- trace observations;
- profiler measurements;
- benchmark outputs;
- reproducer behavior;
- primary-source statements;
- explicit counterexamples.

Where possible, state which claim the evidence supports or contradicts.

---

## Coverage

Return a compact investigation-coverage summary.

Example:

```text
Checked:
- NCCL collective duration
- overlap with compute
- TP=1 vs TP=2 call frequency

Not checked:
- PCIe topology
- CPU affinity
```

Coverage is valuable because Main can avoid duplicate work.

Do not return full chronological reasoning.

---

## Rejected Alternatives

Record materially plausible alternatives that were actually checked and rejected.

This prevents dead hypotheses from being repeatedly reopened.

Do not list every fleeting thought.

---

## Residual Uncertainty

State what the branch could not establish.

Example:

> Current evidence cannot distinguish scheduler queue delay from CPU-side launch synchronization without correlated CPU/GPU tracing.

Unknown is a valid branch result.

---

## Suggested Next Investigation

A worker MAY recommend the highest-information next action.

This is a proposal, not authorization to open another global branch.

---

# 11. Global Investigation State

Main should maintain a compact structured representation of the current investigation.

Conceptually:

```text
GLOBAL INVESTIGATION STATE

Goal

Approved Execution Envelope

Current Phase / Wave

Budget Used / Remaining

Established Facts

Open Hypotheses

Rejected Hypotheses

Critical Decisions / Claims

Active Branches

Completed Branches

Evidence Ledger

Residual Uncertainties

Pending Branch Proposals
```

The state does not need to be persisted as JSON in V1.

It must, however, be explicit enough that Main can answer:

- What do we currently know?
- What remains uncertain?
- What has already been ruled out?
- Which branches are active?
- Which directions are closed?
- What evidence supports the current hypotheses?
- What budget remains?

At the Phase-2/Phase-3 boundary, freeze a **reduced projection** of this single state for verification. It contains only the claims, evidence, coverage, limitations, and provenance needed by Phase 3. It is not a second state machine and must not be maintained independently while Phase 2 continues.

---

# 12. Established Facts vs Hypotheses

Keep facts and hypotheses separate.

Example:

```text
Established fact:
The TP=2 trace contains a 2.1 ms GPU idle interval before the collective.

Hypothesis:
Scheduler-side dispatch delay causes that interval.
```

Do not allow repeated branch summaries to convert an inference into an established fact merely through repetition.

Use three broad epistemic categories:

```text
OBSERVED / ESTABLISHED

INFERRED / HYPOTHESIZED

UNKNOWN / UNRESOLVED
```

This distinction must survive later state reductions.

---

# 13. Evidence Ledger

Maintain evidence around claims, not agent personalities.

Prefer:

```text
Claim C1:
Communication is the dominant bottleneck.

Evidence for:
E2 ...

Evidence against:
E5 ...
E7 ...

Status:
weakened
```

over:

```text
Agent A supports communication.
Agent B disagrees.
```

The Evidence Ledger should record enough provenance to allow later verification or drill-down.

Relevant fields may include:

```text
Evidence ID

Observation

Source / artifact

Supports / contradicts

Scope

Reliability / limitations
```

Do not turn the ledger into a heavyweight database.

Its purpose is reliable reasoning and later verification.

---

# 14. State Reduction After Each Wave

After a wave completes, Main MUST reduce the results before opening more branches.

State Reduction should perform:

```text
1. extract decision-relevant evidence

2. merge duplicate evidence

3. identify contradictions

4. update hypothesis / claim status

5. close falsified or exhausted branches

6. merge overlapping branches

7. identify new high-value uncertainty

8. evaluate pending branch proposals

9. update budget

10. decide stop vs next wave
```

Do not continue by simply appending all branch summaries to the Main context.

The purpose is to transform:

```text
many local investigations
```

into:

```text
one compact global state
```

---

# 15. Branch Merge

Branches should be merged when investigation reveals they are parts of the same causal or decision chain.

Example:

```text
H1:
scheduler queue delay

H2:
CPU dispatch delay
```

Later evidence indicates:

```text
scheduler queueing
      ↓
CPU dispatch delay
      ↓
GPU idle bubble
```

Instead of maintaining two competing branches, create one integrated causal branch when appropriate.

Branch trees should be capable of shrinking as knowledge improves.

---

# 16. Branch Pruning

Prune a branch when:

- its hypothesis is strongly falsified;
- its expected information gain becomes low;
- another branch subsumes it;
- it is materially redundant;
- required evidence is unavailable and no useful alternative exists;
- it no longer affects the final decision.

Do not continue a branch to consume its budget allocation.

Budget is a maximum, not an entitlement.

---

# 17. Branch Replacement

Main may replace a branch inside the approved envelope.

Example:

```text
Initial branch:
CUDA Graph difference

Early evidence:
CUDA Graph disabled in both configurations

Action:
close branch early
```

If a newly discovered:

```text
CPU synchronization
```

branch has higher value, remaining budget may be reallocated to it.

No USER GATE is required when:

- scope remains unchanged;
- budget class remains unchanged;
- total breadth, depth, and verification consumption remain inside the envelope;
- allowed evidence sources, tools/resources, and side-effect boundary remain unchanged.

The change must also preserve the user-visible execution strategy. Otherwise issue an updated Human Review Plan and wait for renewed approval.

---

# 18. Branch Admission Policy During Execution

For a newly proposed branch, Main should ask:

## Materiality

Could its answer materially change the final conclusion?

## Novelty

Does it provide substantially different information from active or completed branches?

## Information gain

Is there an identifiable investigation that could reduce uncertainty?

## Cost

Is the expected gain worth the remaining budget?

## Envelope

Can it be executed inside the approved scope, resources, evidence sources, tools, side-effect, and aggregate breadth/depth/verification boundaries?

A branch that fails these tests should be:

```text
MERGED
DEFERRED
or
REJECTED
```

rather than opened automatically.

---

# 19. Delayed Information Sharing

Initial independent branches should remain independent when independence is part of the design.

After a wave, Main may construct compressed shared objects such as:

```text
Hypothesis Card

Claim:
...

Supporting evidence:
...

Contradicting evidence:
...

Unknown:
...

Requested attack:
...
```

or:

```text
Evidence Card

Observation:
...

Source:
...

Interpretation boundary:
...
```

Later branches should normally receive these compressed representations instead of raw peer transcripts.

This preserves useful evidence while reducing:

- anchoring;
- context contamination;
- duplicate reading;
- consensus collapse.

---

# 20. Direct Worker-to-Worker Communication

Direct worker debate or long peer conversations are **not** the default.

Prefer:

```text
Worker
   ↓
BranchReport
   ↓
Main Reduction
   ↓
compressed shared state
   ↓
next Worker
```

Use direct cross-examination only when Phase 1 intentionally selected Debate / Cross-Examination for a genuine unresolved dispute.

---

# 21. Material Deviation

This section is the authoritative detailed definition of material deviation for this skill.

A material deviation occurs when continuing would materially exceed what the user approved **or change the user-visible execution strategy**. It requires an updated Human Review Plan and a new explicit execution approval.

Five classes are recognized.

---

## 21.1 Budget Expansion

Examples:

```text
approved:
small, source-only review

needed:
multiple additional evidence families plus a full runtime test environment
```

or:

```text
approved:
approximately 4 initial branches + limited targeted follow-up

needed:
large new investigation family requiring many additional branches
```

Waves are synchronization boundaries and their default count is a soft planning prior, not an automatic material-deviation trigger. A third small dependency wave can remain inside the envelope. Assess total breadth, targeted depth, verification consumption, resources, side effects, scope, and user-visible strategy instead.

Small branch replacement, reallocation, merge, or pruning inside the existing envelope and strategy is not material deviation.

---

## 21.2 Scope Expansion

Example:

```text
approved:
review one KV-cache controller

new requirement:
perform a broad redesign of the entire scheduler architecture
```

A discovery may reveal that a larger problem exists.

Main must not silently adopt that larger problem as the new task.

---

## 21.3 Method / Resource Expansion

Example:

```text
approved:
source / documentation analysis

needed:
build full environment
run GPU benchmarks
install major dependencies
perform extensive profiling
```

If the new method was already inside the approved envelope, no escalation is needed.

Otherwise pause.

---

## 21.4 Side-Effect Expansion

Examples:

```text
read-only
→ modify source
```

```text
local analysis
→ push commit
```

```text
existing environment
→ destructive configuration change
```

```text
no external compute
→ expensive cloud workload
```

Side-effect permissions remain governed by the surrounding Codex/runtime safety rules as well as this skill.

---

## 21.5 Goal / Success-Criteria Change

Example:

Original goal:

> determine the performance bottleneck.

Investigation discovers:

> the benchmark is invalid, so bottleneck attribution is not currently meaningful.

Do not silently redefine the task as:

> build a new benchmark framework.

Instead report the new blocking conclusion and propose a pivot.

---

# 22. Material-Deviation Escalation

When material deviation occurs:

```text
PAUSE NEW GLOBAL WORK
        ↓
Compress current state
        ↓
Explain deviation
        ↓
Issue updated Human Review Plan
        ↓
USER GATE
```

The escalation should explain:

- what was discovered;
- why the current envelope is insufficient;
- what additional work is proposed;
- what new resource/budget/scope is required;
- what happens if the expansion is declined.

Do not present internal branch-level detail unless needed for the decision.

---

# 23. Mechanical Failure Recovery

Mechanical failures include:

- tool timeout;
- malformed structured output;
- temporary command failure;
- transient environment issue;
- interrupted worker execution.

A bounded automatic retry is allowed when retry is likely to succeed without changing the investigation.

Default:

```text
one retry
```

If the failure persists:

```text
BLOCKED
```

and return control to Main.

Main may:

```text
RETRY WITH REFRAME
REPLACE WORKER
USE ALTERNATIVE TOOL
DEFER
DROP
```

inside the execution envelope.

---

# 24. Reasoning Failure Recovery

Reasoning failure includes:

- branch returns unsupported opinion;
- branch drifts outside scope;
- branch repeats another branch;
- branch produces no decision-relevant evidence;
- branch misunderstood the assigned uncertainty.

Do not blindly retry the same prompt.

Main should diagnose whether the failure is caused by:

```text
bad BranchSpec

wrong granularity

redundant branch

missing evidence

worker execution quality
```

Then prefer:

```text
REFRAME
MERGE
REPLACE
PRUNE
```

as appropriate.

---

# 25. Missing Tool or Evidence

If an important branch requires unavailable evidence:

```text
BLOCKED
```

must remain a legitimate state.

The worker should report:

```text
Missing capability / evidence

Why it matters

Which distinction cannot be made without it

Possible weaker alternative

Expected confidence loss
```

Main may use a weaker alternative if useful, but must preserve the limitation in the Global Investigation State.

Do not replace missing evidence with confident speculation.

---

# 26. Conflicting Evidence

When credible evidence sources conflict:

Do not vote.

Create a targeted reconciliation task when the conflict is load-bearing.

Ask:

- Are the measurements from different conditions?
- Is the scope mismatched?
- Is one artifact stale?
- Is the methodology inconsistent?
- Can both observations be true under different regimes?
- Is one measurement unreliable?

Example:

```text
Experiment A supports H1
Experiment B contradicts H1
        ↓
Measurement Reconciliation
        ↓
scope split / methodological error / unresolved
```

If the conflict cannot be resolved inside the envelope:

```text
UNRESOLVED
```

is valid.

---

# 27. Stop-or-Continue Decision

After every wave, Main should ask in order:

1. Can the primary question now be answered?
2. Do the surviving load-bearing claims have adequate evidence?
3. Are major competing hypotheses closed or explicitly unresolved?
4. Is there another in-envelope branch with high expected information gain?

Continue only when the fourth answer is yes and further work remains inside the approved envelope.

Stop when:

- the success criteria are met;
- evidence has saturated;
- remaining uncertainty requires inaccessible evidence;
- another branch is unlikely to change the answer;
- or the approved budget is exhausted.

Budget exhaustion is a stop condition, not a reason to overclaim.

Early stopping is correct when additional work would be low value.

---

# 28. Budget Accounting

Track budget at the level needed to enforce the approved envelope:

- branches opened and closed;
- waves completed;
- remaining targeted-depth capacity;
- remaining verification capacity;
- material tool or side-effect use.

Exact token accounting is not required in V1.

Do not convert approximate limits into rigid quotas.

---

# 29. Phase-2 Output

Phase 2 freezes an **Investigation State Projection**: a reduced Phase-3 view of the Global Investigation State, containing:

```text
Approved envelope

Established facts

Surviving hypotheses / claims

Rejected hypotheses

Evidence ledger

Completed branch reports

Coverage

Residual uncertainty

Blocked evidence

Candidate load-bearing claims
```

This projection is the input to Phase 3. It is not independently updated or treated as a parallel state machine.

It is not the final user-facing answer.

---

# 30. Transition to Verification

Before entering Phase 3, Main should ensure that:

- branch reports have been reduced into global state;
- duplicates and obsolete branches are closed;
- important conflicts are resolved or labeled unresolved;
- likely load-bearing claims are identifiable;
- no material deviation has been hidden;
- the remaining task is verification rather than another broad search.

If substantial investigation is still required, remain in Phase 2.

---

# 31. Execution Self-Check

Before declaring Phase 2 complete, check:

- Did Main retain global branch authority?
- Did workers remain inside their BranchSpecs?
- Did every additional branch satisfy the admission policy?
- Were branches merged or pruned when their value fell?
- Did objective evidence override consensus?
- Were limitations preserved instead of filled with speculation?
- Is the frozen Investigation State Projection compact enough for Phase 3?

If not, reduce or correct the state before proceeding.
