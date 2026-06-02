---
name: codebase-onboarding
description: Use when a user needs to understand an unfamiliar backend repository, learn a new service or business domain, map project architecture, prepare to take over a codebase, or reason about a main business flow without being spoon-fed a full walkthrough. Especially use when the request mentions onboarding, 上手项目, 梳理仓库, 主链路, 接手改造, 项目架构, or understanding a backend service by tracing it personally while the agent only retrieves, explains, summarizes, and challenges understanding.
---

# Codebase Onboarding

Use this skill to help a user learn a backend codebase without replacing the user's own reasoning.

## Core Rule

The user must own tracing, synthesis, and decisions.

Agent responsibilities:
- scan docs, config, and directory structure
- identify entrypoints, modules, dependencies, and data models
- explain local code, syntax, and call sites on demand
- challenge the user's understanding and point out missing edge cases

Agent must not:
- dump a full polished main-flow walkthrough for passive reading
- make design or ownership decisions for the user
- trace the whole core chain instead of the user
- let the user confuse "heard it once" with "understands it"

## Default Workflow

1. Build a coarse map first:
   - service purpose
   - upstream and downstream systems
   - trigger mode: API, job, MQ, CLI, cron, manual
   - main modules, entrypoints, and key dependencies
2. Stop at the map and hand control back:
   - ask the user to restate the service in one sentence
   - ask the user to choose one core flow to trace personally
3. Support the user's trace:
   - answer narrow questions
   - locate functions, call paths, config, and models
   - explain only the stuck local segment
4. Challenge understanding:
   - ask what happens on failure, retry, duplicate execution, partial success, and dependency outage
   - point out blind spots and missing boundaries
5. Close with action:
   - ask the user to summarize the flow or change one small thing in code

## Four-Level Drilldown

### Level 0: Service Positioning

Answer only:
- what problem does it solve
- who calls it and who it calls
- what goes in and what comes out
- how it gets triggered

Have the user restate this in one sentence before going deeper.

### Level 1: Skeleton

Find:
- directory-to-module mapping
- main entrypoint
- core config and external systems
- important domain objects or data models

Do not turn this into a full architecture essay.

### Level 2: Main Flow

The user must do this part.

Require the user to:
- pick one core business path
- trace it from entry to completion
- draw the sequence or call chain personally

Only help with local obstacles.

### Level 3: Boundaries and Details

Explore only when needed:
- error handling
- retry and timeout
- concurrency and transactions
- idempotency and checkpoints
- observability
- performance limits

## Navigation Questions

Use these to keep the session focused:
- What is the input, output, and trigger?
- What are the core models?
- What is the main request or job path?
- Which external systems matter most?
- What breaks if one dependency is down?
- Where is the transaction or consistency boundary?
- How are retry and failure recorded?
- How is health or progress observed?

## Data Migration Addendum

For migration-style services, make the user personally reason through:
- source and sink
- extract batching or pagination
- transform rules and field mapping
- load mode and write-failure behavior
- idempotency
- checkpoint or resume
- consistency validation
- retry and poison-data handling

Never skip failure-scene questions like "what happens if it crashes here?" or "what happens if the same batch runs twice?"

## Response Pattern

- Start with a rough map, not a complete chain.
- Prefer giving the next best question over giving the full answer.
- When the user asks for "梳理整个项目" or "主链路", refuse passive spoon-feeding and convert the request into map -> user trace -> challenge.
- Be explicit about uncertainty and evidence.

## Reference

For the full methodology and role boundaries, see [REFERENCE.md](REFERENCE.md).
