# Bug work

Use this reference when the observed failure, cause, or safe fix is not already obvious from direct evidence.

## Establish the failure

Record the observed signal, affected behavior, environment, and smallest known trigger. Distinguish an exact reproduction from a proxy signal or an unverified report. Do not silently upgrade a proxy into proof that the production incident is reproduced.

## Build the causal chain

Trace `trigger → state transition → violated contract → failure signal`. For each competing cause, name an observation that would distinguish it. Instrument or probe the earliest discriminating seam instead of accumulating generic logs.

## Choose the regression seam

Use the narrowest stable seam that fails for the defect and passes for the intended behavior. Prefer a public contract, but use a stable internal seam when the public path is non-deterministic, prohibitively slow, or cannot expose the causal boundary. Do not bind tests to incidental implementation details.

## Write a Fix Brief before non-trivial implementation

Present the following to the responsible engineer when the fix changes behavior, scope, oracle, compatibility, or residual risk:

```text
Failure signal:
Causal chain and discriminating evidence:
Contract owner:
Smallest stable regression seam:
Proposed minimal fix:
Expected evidence:
Residual uncertainty:
```

Wait for human review when those choices are not already accepted. Tiny mechanical defects can remain compressed.

## Close honestly

For a substantial bug, preserve a compact report when it has future diagnostic value:

```text
Observed phenomenon
Code location
Trigger and causal failure
Incorrect behavior in code
Fix
Post-fix reproduction or proxy result
Residual uncertainty
```

If the original failure cannot be reproduced after the fix, do not say it is definitively eliminated. Ask whether to retain an incident checkpoint when recurrence is plausible and the investigation would be costly to rebuild. The checkpoint is resumable evidence, not a claim of closure.
