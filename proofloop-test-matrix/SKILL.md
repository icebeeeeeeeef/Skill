---
name: proofloop-test-matrix
description: Use when the user explicitly asks to create or update a test matrix or counterexample matrix, or when current evidence could pass while a credible implementation still violates the accepted behavior. Do not use merely because a task writes tests, fixes a bug, or changes several files.
---

# Proofloop Test Matrix

Design the smallest set of executable evidence that distinguishes the accepted behavior from credible wrong implementations. Do not write test or production code and do not own the TDD execution loop.

## Required input

Obtain:

```text
Target:
Confidence claim:
Basis:
Current evidence:
```

`Basis` must identify the source that defines correctness: accepted outcome, contract, specification, repository decision, or clarified user choice. Source code, existing tests, and a diff can reveal possible failure modes, but cannot define the oracle by themselves.

If any material outcome—such as an error type, ordering rule, compatibility boundary, or side effect—is needed for an assertion but absent from `Basis`, stop and return the missing decision to `proofloop`'s Decide step. Do not guess it and do not hide it in a note beneath a proposed test.

The word `reject` alone is not an executable oracle. Unless `Basis` defines the observable mechanism—such as an exception type, error value, or result variant—do not emit “rejects”, “raises an error”, or “direct rejection assertion” as a matrix row. Return the missing rejection contract and no matrix.

## Build the matrix

For each behavior obligation in the accepted scope:

1. Name a credible wrong implementation that could pass `Current evidence`. Prefer realistic shortcuts: hard-coded examples, wrong operation order, missing boundary branches, incorrect early exit, mutation, stale-version semantics, or success-only handling.
2. Choose the smallest scenario whose observable result differs between that implementation and the accepted oracle.
3. Name executable evidence that can observe the difference at the narrowest stable seam.
4. Keep one behavior obligation per row so a reviewer can audit the mapping. Reuse the same scenario or Evidence in several rows when it distinguishes several obligations. Merge rows only when both the obligation and counterexample are semantically the same; sharing a test case alone is not a reason to merge them.
5. Delete rows that cannot name a credible wrong implementation in the accepted scope.

Use implementation details and the latest diff only to discover additional counterexamples. Never change the expected behavior merely to match the implementation.

## Output

Return only:

```text
Target:
Confidence claim:
Basis:

| Behavior obligation | Credible wrong implementation | Distinguishing scenario and oracle | Evidence |
```

Do not append a generic test plan, risk score, coverage percentage, implementation steps, or long rationale.

## Roll forward

After each meaningful implementation result, inspect the real diff and current tests. Add a row only when they reveal a new credible wrong implementation inside accepted scope. Remove a row when its counterexample is no longer credible or another row supplies the same discrimination.

Stop when the known material counterexamples are excluded by executable evidence, or when the intended confidence claim has been explicitly narrowed to match the remaining evidence.

For independent review, send `proofloop-matrix-reviewer` only this matrix, the original `Basis`, and directly relevant code and tests. Do not send the author's defense of the matrix.
