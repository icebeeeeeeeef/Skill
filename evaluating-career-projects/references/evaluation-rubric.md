# Evaluation Rubric

Use hard gates before scoring. A failed gate determines the verdict even when the numeric total is high.

## Hard Gates

| Gate | Pass condition | Failure action |
|---|---|---|
| Target | Names a role family, candidate level, and evaluator | State assumptions or defer selection |
| Real problem | Bottleneck is supported by a trace, issue, paper, source code, incident, benchmark, or credible workload | Research before implementation |
| Falsifiability | One question can be disproved by declared metrics | Reshape the project |
| Ownership | Candidate owns a hard mechanism, not only configuration or glue | Move closer to the data path or choose another project |
| Feasibility | Time, hardware, data, and dependency access support the central claim | Reduce the claim or reject the project |
| Baseline | At least one credible existing behavior or system is available for comparison | Build the baseline first |
| Measurement | Workload, metrics, environment, repetitions, and attribution method are defined | Add instrumentation before optimization |
| Reproducibility | Another engineer can run or inspect the evidence | Add scripts, configs, versions, and result artifacts |
| Defensibility | Candidate can answer five levels of why, alternatives, failure, and scale questions | Deepen or narrow the project |
| Credibility | Every claim has an honest state and evidence owner | Correct the claims before packaging |

## 100-Point Score

### Role relevance and problem value: 15

- 0-5: generic technology demo or weak role connection.
- 6-10: relevant subsystem but unclear business or system bottleneck.
- 11-15: direct responsibility match with a real, important problem.

### Personal ownership and attribution: 15

- 0-5: mostly deployment, configuration, or dependency behavior.
- 6-10: owns integration and part of the mechanism.
- 11-15: owns the critical decision, implementation, and diagnosis path.

### Mechanistic and cross-layer depth: 20

- 0-7: API-level understanding.
- 8-14: explains internals and one resource trade-off.
- 15-20: connects workload, algorithm, runtime, hardware, and system metrics.

### Evidence and experimental rigor: 25

- 0-8: screenshots or a single unqualified number.
- 9-17: baseline and useful metrics but weak attribution or workload coverage.
- 18-25: controlled baselines, ablations, tails, negative cases, repeated runs, and causal explanation.

### Engineering completeness and reproducibility: 10

- 0-3: demo-only or manual setup.
- 4-7: tests, configuration, metrics, and documented run path.
- 8-10: robust failure handling, deterministic artifacts, and third-party reproduction.

### Trade-off judgment and failure boundaries: 10

- 0-3: only success narrative.
- 4-7: alternatives and known limitations.
- 8-10: quantified break-even points, losing workloads, rollback, and rejected alternatives.

### Communication and packaging clarity: 5

- 0-1: feature or keyword list.
- 2-3: understandable problem and result.
- 4-5: concise causal story with exact scope and evidence links.

## Verdict Bands

- `85-100`: select, provided all hard gates pass.
- `70-84`: select after closing named evidence gaps.
- `55-69`: reshape around the strongest causal mechanism.
- `<55`: defer or reject.

Do not use the band to override a failed gate. Unsupported metrics, production status, or ownership are credibility failures, not small point deductions.

## Interpretation Rules

- Novelty is optional. A rigorous extension to a mature system can score highly.
- Difficulty is not value unless it creates relevant, attributable evidence.
- JD keyword count is not a dimension.
- Match the role cluster. Do not optimize for mutually incompatible platform, engine, compiler, and research profiles in one project.
- State which dimensions are evidenced now and which assume future completion.
