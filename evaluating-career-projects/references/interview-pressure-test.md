# Interview Pressure Test

Use this after the project question and evidence plan exist. Ask for concrete paths, measurements, and decisions rather than rehearsed definitions.

## Five-Level Follow-Up Chains

### Problem Choice

1. What observed phenomenon justified the project?
2. Why is it important for the target team or workload?
3. What evidence shows the named bottleneck dominates?
4. Why are existing systems or policies insufficient?
5. Under what condition would the project no longer be worth doing?

### Mechanism and Alternatives

1. What exactly changes in the data or control path?
2. Which state, invariant, or resource does the mechanism manage?
3. Why choose this design over the strongest alternative?
4. What is the break-even model for transfer, compute, memory, or coordination?
5. Which workload makes the chosen mechanism lose?

### Implementation Ownership

1. Which modules, functions, or interfaces did the candidate change?
2. Which behavior came from dependencies unchanged?
3. What was the hardest bug or incorrect assumption?
4. Which trace, profiler, test, or log established the root cause?
5. What would fail if the candidate's component were removed?

### Measurement and Causality

1. What are the baseline, primary metric, and guardrails?
2. How were warmup, variance, load shape, and repetitions controlled?
3. Which ablation isolates the claimed mechanism?
4. Did mean improvement hide p95/p99 or quality regressions?
5. Can another engineer reproduce the number from a command and artifact?

### Production and Scale

1. What happens on overload, timeout, partial failure, or stale state?
2. What fallback or rollback exists?
3. Which assumption breaks at 10x requests, context, workers, or model size?
4. What new bottleneck appears across PCIe, NVLink, RDMA, network, or storage?
5. Which claim remains simulated rather than production-validated?

## Red Flags

- The answer starts with a framework name rather than a phenomenon.
- Every dependency is described as personally implemented.
- A controller or platform wrapper hides several unrelated research questions.
- Only the winning workload or average metric is shown.
- There is no credible baseline, ablation, or negative result.
- A simulator, replay, or cost model is described as a production system.
- Hardware, model, scale, or metric values cannot be stated exactly.
- The resume bullet is more ambitious than the evidence ledger.
- Roadmap features appear in architecture diagrams without state labels.
- The candidate cannot explain why a fashionable technology was excluded.

## Pass Standard

A defensible project should support a 20-minute discussion in which the candidate can:

- trace one request or data object through the changed path;
- explain one quantitative trade-off and one rejected design;
- show one baseline, one ablation, and one losing condition;
- distinguish owned code from dependency behavior;
- name exact evidence artifacts and honest claim states;
- explain how constraints shaped scope.

If two or more chains collapse into generic definitions, reduce scope or deepen implementation before packaging the project.
