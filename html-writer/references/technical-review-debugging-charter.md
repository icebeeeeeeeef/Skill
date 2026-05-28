# Technical Review And Debugging Charter

This is the v1 minimum charter for technical proposals, architecture reviews, incident notes, and debugging reports. Expand this reference later with a fuller review/debugging doctrine.

## Purpose

Make a technical judgment easy to read while preserving the evidence chain needed to audit that judgment.

## Preferred Thinking Flow

1. State the problem, goal, incident, or observed symptom.
2. State constraints, assumptions, non-goals, and what is known.
3. Put the current conclusion or recommendation near the top.
4. Present options or hypotheses.
5. Show evidence and validation results.
6. Compare tradeoffs and risks with concrete decision criteria.
7. State the decision, next actions, and owners if known.
8. Collapse raw material: logs, command output, failed attempts, long traces, and detailed investigation notes.

## HTML Pattern

- Use a table of contents plus a phase timeline or status board.
- Use status tags such as confirmed, likely, ruled out, risky, unknown, and next action.
- Use decision tables for options and tradeoffs.
- Use evidence blocks for commands, logs, screenshots, traces, and code pointers.
- Fold aggressively: the reader should see conclusion, risk, and next action without scrolling through raw evidence.

## Minimum Quality Bar

- Do not claim a root cause without evidence.
- Separate facts, hypotheses, inferences, and recommendations.
- Mark uncertainty and unresolved questions.
- Preserve enough raw evidence for a later reader to replay the reasoning.
