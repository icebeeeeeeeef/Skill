# Intake and Review Reference

仅在原始材料零散、ownership 不清、指标复杂，或用户要求完整面试准备时读取本文件。

## Compact fact sheet

```text
Project / system:
Target role / JD signals:

Problem:
Who benefited / why it mattered:

Claim state:
- planned / prototype / experimental / shipped / production-observed

My contribution:
- independently owned:
- designed or decided:
- implemented:
- diagnosed or measured:

Boundaries:
- team-owned:
- upstream / framework-owned:
- decisions made by others:

Constraint or failure mode:
Alternatives considered:
Decision and trade-off:

Evidence:
- delivery / adoption / scale:
- baseline -> result:
- workload / time window:
- measurement source and method:
- attribution strength:
- regressions or limits:

Interview depth:
- implementation path I can explain:
- failure or iteration I can explain:
- facts I do not know or did not own:
```

## Claim-state language

Keep status visible in wording:

| State | Safe wording | Avoid |
|---|---|---|
| Planned | proposed, scoped, designed a plan | built, delivered, improved |
| Prototype | prototyped, demonstrated locally | shipped, productionized |
| Experimental | evaluated, measured under X, observed | improved generally, validated in production |
| Shipped | implemented, launched, migrated | production impact unless observed |
| Production-observed | reduced/increased X under stated evidence | causal attribution beyond evidence |

Negative and inconclusive results remain results. State what was ruled out, what boundary was found, or why the approach was stopped.

## Attribution test

For each claim, ask:

1. What exact artifact, decision, implementation, diagnosis, or experiment belongs to the candidate?
2. If that contribution were removed, what result would change?
3. Is the result direct, reasonably influenced, merely correlated, or only team-level?
4. Which verb remains true after answering those questions?

If the candidate cannot identify a changed outcome or owned artifact, prefer `contributed to X by implementing Y` over `owned X`.

## Evidence ladder

Use the strongest truthful evidence available; do not force every claim to reach the top.

1. `Specific work` — named artifact, path, component, migration, policy or diagnosis;
2. `Delivery` — shipped, adopted, reused, rolled out, incident resolved;
3. `Scale` — requests, users, data, services, teams, regions, workload;
4. `Measured change` — before/after with units and method;
5. `Attributable outcome` — experiment, controlled comparison or clear causal chain.

An unverified percentage is weaker than a concrete shipped artifact with honest scope.

When a team-level metric is materially confounded, keep it out of the resume wording unless it is clearly useful as concise system context. Put the attribution limitation in review notes; do not turn the bullet itself into a disclaimer.

## Follow-up simulation

Follow the claim rather than asking random trivia:

1. `Context` — What was wrong before? Who cared? How was success defined?
2. `Ownership` — What did you personally own? What did the team or upstream own?
3. `Decision` — What alternatives existed? Why this one? What was sacrificed?
4. `Mechanism` — Walk through the request/data/control path. Where could it fail?
5. `Evidence` — Baseline, workload, measurement, attribution, regression.
6. `Boundary` — When would this design stop working? What changes at 10x scale?
7. `Reflection` — What failed? What would you change now?

Do not require an arbitrary number of follow-up layers. Depth should match the strength and scope of the claim.

## Compression review

For each bullet:

- underline the personal action;
- circle the object/problem;
- mark one decision/mechanism if it matters;
- mark the evidence;
- delete everything that does not improve truth, relevance, comprehension or defensibility.

Across the project entry, check portfolio coverage rather than forcing every bullet to contain every element:

- Does at least one bullet show outcome or scope?
- Does at least one show technical depth, judgment or a nontrivial constraint?
- Are ownership and claim state clear throughout?
- Is the strongest evidence first?
