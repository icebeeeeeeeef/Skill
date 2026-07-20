# Knowledge handoff

Read and write durable knowledge only when it changes future work.

## Read before deciding

Start with the repository's routing surfaces such as `AGENTS.md`, `docs/index.md`, manifests, CI configuration, and nearby source. Follow links to ADRs, contracts, incident notes, or Git history only when they can constrain the current outcome, implementation, or evidence. Do not load the entire docs tree as ritual.

## Keep task state in the task

Use the current issue, plan, or conversation for temporary decisions and pending work. Create a durable checkpoint only when work must survive the current context, another task depends on it, or rebuilding the evidence would be expensive.

An issue or revisit item may capture deferred work as:

```text
Observed context
Current decision
Why revisit
Trigger for revisiting
Evidence already gathered
```

This is a task queue, not proof that the deferred work is required.

## Promote only durable knowledge

After completion, keep a document when it records a stable contract, accepted architectural decision, costly investigation, recurring operational fact, or reusable failure prevention. Put it near the domain that owns the fact and update the smallest relevant index when discovery has become unreliable.

Delete or leave transient notes in the task when they merely narrate work, duplicate source code, repeat an existing document, or have no plausible future reader decision.

Repository-specific mistakes belong with repository constraints. Broad, recurring reasoning mistakes may become a portable `proofloop-guardrails` rule only after checking that the trigger and required action generalize beyond one incident. The responsible engineer approves every portable-rule change.
