# Provenance and Design Rationale

## Purpose and reading boundary

This file is for design review only. Do not load it during normal execution. The runtime contract is `../SKILL.md`; detailed mechanics live in the phase references.

Each entry separates a **source fact** from a **derived rule**. A source fact reports only what the linked source directly supports. A derived rule is this Skill's local engineering policy, not a claim that an external source mandates it.

All links below were accessed on **2026-08-13**. Product documentation and preprints can change; re-check them before relying on a time-sensitive claim.

## Source register

### Codex Skills

**Primary source:** [OpenAI, Build skills](https://learn.chatgpt.com/docs/build-skills) (accessed 2026-08-13).

**Source facts:** The documentation defines a skill as a directory with `SKILL.md` and optional scripts/references. It describes progressive disclosure: Codex begins with skill metadata and loads `SKILL.md` after choosing the skill. It documents both explicit invocation and implicit selection from a matching description. It also documents `agents/openai.yaml` and `policy.allow_implicit_invocation: false`.

**Derived rules:** Keep a thin `SKILL.md`, route detailed mechanics lazily, and use `agents/openai.yaml` plus an explicit runtime rule to make this Skill opt-in only.

### Codex native subagents

**Primary source:** [OpenAI, Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) (accessed 2026-08-13).

**Source facts:** The documentation describes Codex delegating bounded work to parallel subagents and returning summaries to the main thread. Local Codex delegates when directly asked or when applicable `AGENTS.md` or Skill instructions require it. It warns that parallel write-heavy work can create conflicts, and states that subagents inherit the parent sandbox and permission mode.

**Derived rules:** V1 uses only native Codex subagents, prefers independent read-heavy branches, constrains workers with BranchSpecs, and lets host safety rules outrank this Skill.

### LLM-owned and code-owned orchestration

**Primary source:** [OpenAI Agents SDK, Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/) (accessed 2026-08-13).

**Source facts:** The SDK documentation distinguishes LLM-directed orchestration from code-directed orchestration and says they can be combined. It describes code-directed flow as more deterministic and predictable in speed, cost, and performance.

**Derived rule:** V1 keeps stable policy in the Skill and lets Main adapt topology inside a user-approved envelope. It deliberately does not add a workflow runtime; any later externalization needs execution evidence for a specific failed control boundary.

### Anthropic workflow and research case studies

**Primary sources:**

- [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), published 2024-12-19; accessed 2026-08-13.
- [Anthropic, How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), published 2025-06-13; accessed 2026-08-13.

**Source facts:** The first article distinguishes predefined-code workflows from LLM-directed agents and describes an orchestrator-worker pattern in which a central LLM dynamically delegates and synthesizes. The second is an engineering case study of Anthropic's Research product: it describes a lead agent that plans, launches parallel specialist subagents, and synthesizes their results. It is not a general comparative proof for all agent systems.

**Derived rules:** Use adaptive branch/wave topology only when a distinct uncertainty or evidence source can change the decision; choose the smallest topology that preserves useful independence and human control.

### Debugging, root-cause, and performance preprints

**Primary sources:**

- [Debug2Fix](https://arxiv.org/abs/2602.18571), submitted 2026-02-20; accessed 2026-08-13.
- [RCLAgent: Adaptive Root Cause Localization](https://arxiv.org/abs/2508.20370), submitted 2025-08-28; accessed 2026-08-13.
- [RCLAgent: Towards In-Depth Root Cause Localization](https://arxiv.org/abs/2605.14866), submitted 2026-05-14; accessed 2026-08-13.
- [PerfAgent](https://arxiv.org/abs/2607.19653), submitted 2026-07-22; accessed 2026-08-13.

**Source facts:** These are author-published preprints, not a single independently validated result. Debug2Fix proposes an interactive-debugging subagent architecture. The 2026 RCLAgent paper describes per-span agents and parallel trace-graph organization; it must not be conflated with the 2025 paper. PerfAgent proposes profiler-guided, verifier-in-the-loop repository optimization. Their reported evaluations apply only to their named settings and should not be generalized as broad guarantees.

**Derived rules:** Specialize a branch by evidence, uncertainty, or capability rather than persona. For runtime and performance claims, prefer observations that can discriminate the hypothesis—such as traces, controlled tests, or profiles—over additional opinion branches.

### Generator–verifier and debate

**Primary sources:**

- [Rethlas repository](https://github.com/frenzymath/Rethlas) (project README; accessed 2026-08-13).
- [Du et al., Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://openreview.net/pdf?id=zj7YuTE4t8), ICML 2024; [permanent preprint](https://arxiv.org/abs/2305.14325), submitted 2023-05-23; accessed 2026-08-13.

**Source facts:** Rethlas's README describes a project-specific two-agent proof-and-repair loop with generation and verification roles; it is not independent validation of general proof-system performance. Du et al. study multiple language models proposing, criticizing, and revising answers over debate rounds, and report results on their evaluated tasks. Neither source establishes that debate is universally beneficial or cost-effective.

**Derived rules:** A verifier should test or attack a candidate rather than silently become a second generator. Debate is optional and only fits a persistent disagreement without a more direct oracle; consensus never establishes correctness by itself.

### Framework guidance

**Primary source:** [LangChain, Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent/index) (framework documentation; accessed 2026-08-13).

**Source facts:** The page describes subagent, handoff, skills, router, and custom-workflow patterns. It also says not every complex task needs a multi-agent system; a single agent with suitable tools and prompting can sometimes be sufficient. This is framework guidance, not empirical evidence.

**Derived rule:** Optimize for information gain, evidence quality, verification strength, and control—not agent count.

## Local control decisions

The following are deliberate local policies. They are not asserted as requirements of the sources above:

- explicit invocation only, followed by a Phase-1 Human Review Plan and USER GATE;
- an approved execution envelope that grants bounded Main autonomy rather than blanket permission;
- one Main-owned investigation state, with a frozen Phase-3 projection rather than a second state machine;
- workers constrained by inherited/declared evidence sources, exact tools/resources, and side-effect boundary;
- branch admission, merge, pruning, and replacement inside the envelope without gate churn;
- a material-deviation test based on user-visible strategy and aggregate breadth/depth/verification use, resources, side effects, scope, goal, and success criteria—not merely the number of waves;
- Phase 3 focused on load-bearing claims and Phase 4 constrained to verification dispositions;
- selecting a verifier by claim type and oracle fit rather than a strict total ordering.

## V1 boundary

V1 consists of this methodology Skill, lazy references, an explicit user approval gate, Main-owned transient state, and Codex native subagents. It does **not** implement an external workflow engine, persistent database, fixed agent pool, agent-to-agent network, automatic activation, automatic budget expansion, or complete reasoning-transcript storage.

These are scope limits, not claims that such components are never useful. Reconsider one only after repeated, reviewable execution evidence identifies the exact control boundary that fails without it.

## Sources to reverify

The prior provenance draft contained unverified conversational citation markers and claims about specific dynamic-workflow, proof, and research systems. Those markers and the claims that depended on them were removed rather than backfilled from memory. In particular, any intended use of the FrenzyMath technical report or claims about a separate “Dynamic Workflows” product must be revalidated from a stable primary source before being reintroduced.

## Review rule

When revising this Skill:

1. Keep source facts and derived rules separate.
2. Re-check product behavior, source versions, and empirical claims that may have changed.
3. State whether a paper is a preprint, a case study, framework guidance, or independent evidence.
4. Do not generalize reported results beyond their evaluated scope.
5. Preserve the V1 boundary unless a concrete, repeated failure supplies a reason to expand it.
