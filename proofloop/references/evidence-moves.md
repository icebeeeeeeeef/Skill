# Evidence moves

Use the same evidence-to-decision spine for investigation, design discussion, and experiments.

## Keep claims typed

- **Fact:** directly supported by current source, primary documentation, an executed command, or an observed result.
- **Inference:** an explanation derived from facts; name the supporting facts.
- **Unknown:** information that could change the decision and lacks sufficient evidence.

Do not turn convention, memory, or a plausible API interpretation into a fact.

## Verify unstable semantics

Check upstream source or current primary documentation when behavior may vary by version, configuration, platform, dependency, or recent release. Prefer the repository's pinned version and actual call path over examples for the newest release. Use a small local probe when documentation does not establish runtime behavior.

Use the `research` skill only when the question needs substantial primary-source legwork or a durable cited report. A focused documentation lookup or source read stays inside the current task.

## Compare real options

Only present alternatives that satisfy the accepted outcome and could reasonably be chosen. For each option, state the behavior difference, evidence, irreversible cost, and reason it may win. Delete decorative options that exist only to make a list.

Ask the responsible engineer when the remaining choice changes product behavior, scope, compatibility, risk acceptance, or the oracle. Do not repeatedly reconfirm an already accepted and evidence-compatible choice.

## Run falsifiable experiments

State:

```text
Question:
Competing explanations or options:
Cheapest observation that distinguishes them:
Result:
Decision changed or unchanged:
```

Discard exploratory code unless it becomes part of the accepted implementation or reusable evidence. Return to Decide after the observation; an experiment does not own the development workflow.
