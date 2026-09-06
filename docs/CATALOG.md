# 本地 Skills 清单

盘点日期：2026-09-07。个人目录共 94 个条目，去重后 92 个，收录 90 个。

这是保存与迁移清单，不是对每个技能的效果或外部服务可用性的背书。保留完整目录和原有说明；重叠但有独立使用场景的技能作为可选项保存。

## 已收录

### 工程执行与工具

| 技能 | 用途（来自本地声明） |
|---|---|
| [MAW](../MAW/SKILL.md) | Use only when the user explicitly invokes this named skill for a controlled multi-agent investigation of a difficult analysis, diagnosis, review, proof, or research task. |
| [caveman](../caveman/SKILL.md) | Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", or invokes /caveman. |
| [diagnose](../diagnose/SKILL.md) | Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression. |
| [dispatching-parallel-agents](../dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| [executing-plans](../executing-plans/SKILL.md) | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| [find-skills](../find-skills/SKILL.md) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill. |
| [finishing-a-development-branch](../finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| [grok-build-cli](../grok-build-cli/SKILL.md) | Invoke the locally installed Grok Build CLI from Codex and return Grok's response. Use whenever the user asks Codex to call, consult, run, or delegate a prompt to Grok or Grok Build, including Grok web/X searches and agentic Grok tasks. This Skill covers only the invocation mechanism, process monitoring, and response capture; it does not prescribe the task itself. |
| [handoff](../handoff/SKILL.md) | Compact the current conversation into a handoff document for another agent to pick up. |
| [migrate-to-codex](../migrate-to-codex/SKILL.md) | Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files. |
| [playwright](../playwright/SKILL.md) | Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script. |
| [ponytail](../ponytail/SKILL.md) | Forces the laziest solution that actually works, simplest, shortest, most minimal. Channels a senior dev who has seen everything: question whether the task needs to exist at all (YAGNI), reach for the standard library before custom code, native platform features before dependencies, one line before fifty. Supports intensity levels: lite, full (default), ultra. Use on ANY coding task: writing, adding, refactoring, fixing, reviewing, or designing code, and choosing libraries or dependencies. Also use whenever the user says "ponytail", "be lazy", "lazy mode", "simplest solution", "minimal solution", "yagni", "do less", or "shortest path", or complains about over-engineering, bloat, boilerplate, or unnecessary dependencies. Do NOT use for non-coding requests (general knowledge, prose, translation, summaries, recipes). |
| [ponytail-audit](../ponytail-audit/SKILL.md) | Whole-repo audit for over-engineering. Like ponytail-review, but scans the entire codebase instead of a diff: a ranked list of what to delete, simplify, or replace with stdlib/native equivalents. Use when the user says "audit this codebase", "audit for over-engineering", "what can I delete from this repo", "find bloat", "ponytail-audit", or "/ponytail-audit". One-shot report, does not apply fixes. |
| [ponytail-debt](../ponytail-debt/SKILL.md) | Harvest every `ponytail:` comment in the codebase into a debt ledger, so the deliberate shortcuts and deferrals ponytail leaves behind get tracked instead of rotting into "later means never". Use when the user says "ponytail debt", "/ponytail-debt", "what did ponytail defer", "list the shortcuts", "ponytail ledger", or "what did we mark to do later". One-shot report, changes nothing. |
| [ponytail-gain](../ponytail-gain/SKILL.md) | Show ponytail's measured impact as a compact scoreboard: less code, less cost, more speed, from the benchmark medians. One-shot display, not a persistent mode, and not a per-repo number. Trigger: /ponytail-gain, "ponytail gain", "what does ponytail save", "show ponytail impact", "ponytail scoreboard". |
| [ponytail-help](../ponytail-help/SKILL.md) | Quick-reference card for all ponytail modes, skills, and commands. One-shot display, not a persistent mode. Trigger: /ponytail-help, "ponytail help", "what ponytail commands", "how do I use ponytail". |
| [ponytail-review](../ponytail-review/SKILL.md) | Code review focused exclusively on over-engineering. Finds what to delete: reinvented standard library, unneeded dependencies, speculative abstractions, dead flexibility. One line per finding: location, what to cut, what replaces it. Use when the user says "review for over-engineering", "what can we delete", "is this over-engineered", "simplify review", or invokes /ponytail-review. Complements correctness-focused review, this one only hunts complexity. |
| [proofloop](../proofloop/SKILL.md) | Use for engineering tasks that intend persistent repository changes, including features, bug fixes, behavior or configuration changes, refactors, migrations, dependency upgrades, and test changes. Do not use by default for a single source fact, code explanation, pure review, or a small read-only investigation. |
| [proofloop-guardrails](../proofloop-guardrails/SKILL.md) | Use when a persistent engineering change or independent review may match a recurring, cross-repository AI failure pattern, when proofloop requests a portable guardrail check, or when the user asks to add, revise, merge, or remove a guardrail. Do not use as a substitute for repository-specific rules or deterministic gates. |
| [proofloop-test-matrix](../proofloop-test-matrix/SKILL.md) | Use when the user explicitly asks to create or update a test matrix or counterexample matrix, or when current evidence could pass while a credible implementation still violates the accepted behavior. Do not use merely because a task writes tests, fixes a bug, or changes several files. |
| [receiving-code-review](../receiving-code-review/SKILL.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| [requesting-code-review](../requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| [subagent-driven-development](../subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session |
| [systematic-debugging](../systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| [tdd](../tdd/SKILL.md) | Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development. |
| [test-driven-development](../test-driven-development/SKILL.md) | Use when implementing any feature or bugfix, before writing implementation code |
| [using-git-worktrees](../using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback |
| [using-superpowers](../using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| [verification-before-completion](../verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |
| [write-a-skill](../write-a-skill/SKILL.md) | Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill. |
| [writing-plans](../writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code |
| [writing-skills](../writing-skills/SKILL.md) | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

### 理解、设计与规划

| 技能 | 用途（来自本地声明） |
|---|---|
| [codebase-design](../codebase-design/SKILL.md) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary. |
| [codebase-onboarding](../codebase-onboarding/SKILL.md) | Use when a user needs to understand an unfamiliar backend repository, learn a new service or business domain, map project architecture, prepare to take over a codebase, or reason about a main business flow without being spoon-fed a full walkthrough. Especially use when the request mentions onboarding, 上手项目, 梳理仓库, 主链路, 接手改造, 项目架构, or understanding a backend service by tracing it personally while the agent only retrieves, explains, summarizes, and challenges understanding. |
| [domain-modeling](../domain-modeling/SKILL.md) | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, or when another skill needs to maintain the domain model. |
| [grill-me](../grill-me/SKILL.md) | A relentless interview to sharpen a plan or design. |
| [grill-with-docs](../grill-with-docs/SKILL.md) | Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions. |
| [grilling](../grilling/SKILL.md) | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| [improve-codebase-architecture](../improve-codebase-architecture/SKILL.md) | Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable. |
| [prototype](../prototype/SKILL.md) | Build a throwaway prototype to flesh out a design before committing to it. Routes between two branches — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route. Use when the user wants to prototype, sanity-check a data model or state machine, mock up a UI, explore design options, or says "prototype this", "let me play with it", "try a few designs". |
| [setup-matt-pocock-skills](../setup-matt-pocock-skills/SKILL.md) | Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Run before first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs. |
| [steelman](../steelman/SKILL.md) | Strengthen an idea into its best defensible form before criticizing it, then expand the design space, attack the strongest variants, and synthesize the smallest high-value direction worth pursuing. Use for technical brainstorming, research ideas, system design, project selection, architecture proposals, and other situations where premature rejection or shallow idea generation would be costly. |
| [to-issues](../to-issues/SKILL.md) | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues. |
| [to-prd](../to-prd/SKILL.md) | Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context. |
| [triage](../triage/SKILL.md) | Triage issues through a state machine driven by triage roles. Use when user wants to create an issue, triage issues, review incoming bugs or feature requests, prepare issues for an AFK agent, or manage issue workflow. |
| [wayfinder](../wayfinder/SKILL.md) | Plan a huge chunk of work — more than one agent session can hold — as a shared map of investigation tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. |

### 检索与研究

| 技能 | 用途（来自本地声明） |
|---|---|
| [global-search](../global-search/SKILL.md) | 搜索全网内容，返回脚本整理后的结构化结果（标题、链接、作者、摘要等） |
| [hot-list](../hot-list/SKILL.md) | 获取知乎热榜列表，返回脚本整理后的结构化结果（标题、链接、缩略图、摘要） |
| [research](../research/SKILL.md) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent. |
| [technical-research](../technical-research/SKILL.md) | Use when investigating technologies, source analyses, engineering practice, implementation discovery, troubleshooting, wheel-reinvention checks, or technical comparisons, especially for AI Infra, LLM Serving, KV Cache, vLLM, SGLang, Mooncake, LMCache, backend/storage/scheduling, and Chinese long-form evidence. |
| [zhida](../zhida/SKILL.md) | 调用知乎开放平台的 zhida 接口，返回结构化回答结果 |
| [zhihu-search](../zhihu-search/SKILL.md) | 搜索知乎站内内容，返回脚本整理后的结构化结果（标题、链接、作者、摘要等） |

### 学习、解释与可视化

| 技能 | 用途（来自本地声明） |
|---|---|
| [explain-concepts](../explain-concepts/SKILL.md) | Explains difficult concepts using master teaching methodologies (Feynman, Socratic, Cognitive Load, Dual Coding). Use when user asks to explain a concept, "I don't understand X", ELI5 requests, "what is X", "how does X work". |
| [html-writer](../html-writer/SKILL.md) | Create high-readability local HTML documents for long or complex technical output. Use when Codex should turn codebase/project understanding, deep technical teaching, technical proposals, architecture reviews, bug investigations, or debugging records into a navigable HTML report with diagrams, collapsible evidence, readable styling, and local browser-friendly interaction. Also use when the user explicitly asks for HTML output, a readable local report, expandable/collapsible sections, diagrams, timelines, or a more polished alternative to Markdown for technical material. |
| [interactive-mindmap](../interactive-mindmap/SKILL.md) | Use when creating XMind-like interactive mind maps from notes, PDFs, outlines, Markdown, Mermaid mindmap blocks, study summaries, or hierarchical content. Produces collapsible, zoomable local HTML mind maps with Markmap, and can optionally advise when real Xmind MCP or Xmind export is needed. |
| [show-me](../show-me/SKILL.md) | 用低术语密度、自然且有主线的语言解释概念、评审技术方案或总结调研结论。适用于读者需要理解原因、取舍和结论的场景；不用于命令、参数、配置等速查内容。 |
| [teach](../teach/SKILL.md) | Teach the user a new skill or concept, within this workspace. |
| [zoom-out](../zoom-out/SKILL.md) | Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar with a section of code or need to understand how it fits into the bigger picture. |

### 求职与项目表达

| 技能 | 用途（来自本地声明） |
|---|---|
| [51mee-position-parse](../51mee-position-parse/SKILL.md) | 职位解析。触发场景：用户提供职位描述要求解析；用户想分析JD的核心要求。 |
| [bullet](../bullet/SKILL.md) | 将候选人真实完成或参与的软件工程项目、实习产出、性能优化、系统设计、 故障治理与基础设施工作，转化为面向目标岗位、便于快速扫描且能经受技术追问的 简历 bullet。适用于已有事实材料的提炼、重写和审查；不用于创造经历、补写 未验证指标或夸大个人 ownership。 |
| [evaluating-career-projects](../evaluating-career-projects/SKILL.md) | Use when selecting, comparing, scoping, reviewing, or packaging an engineering project for recruiting; deriving a project from JDs; deciding whether to add fashionable technologies; or checking resume and interview claims against actual implementation evidence. |
| [jobhound](../jobhound/SKILL.md) | 求职陪跑全流程助手——覆盖简历解析、岗位发现与评估、定制简历生成、 面试全阶段准备（自我介绍/JD拆解、岗位背景调研、面试押题、模拟面试、 笔试准备）、面试复盘、Offer评估与薪资谈判、投递跟踪管理。 适用于中国校招/实习市场（牛客网、实习僧、BOSS直聘、拉勾等）， 也适配其他地区。覆盖产品经理、运营、市场、技术、设计等各岗位方向。 当用户提到以下意图时触发：找工作、搜实习、简历匹配、岗位筛选、 面试准备、自我介绍、模拟面试、笔试准备、面试复盘、Offer评估、投递跟踪、 "帮我找工作"、"有哪些实习机会"、"准备面试"、"帮我看下这个offer"。 |
| [resume-claim-steering](../resume-claim-steering/SKILL.md) | Turns real project facts into a target-role resume (project spine + bullets) and a grillable interview question tree, gated by a claim-evidence ledger so wording cannot outrun facts. Use when the user wants to 写简历, 改写项目, 包装经历, 酥化, 写 bullet, 生成面试题, 话题树, 主张账本, 问穿简历, 模拟面试, 准备技术面, or runs /resume-claim-steering. Also use when discussing a project in order to produce resume text and interview prep together. |
| [resume-optimization](../resume-optimization/SKILL.md) | 基于目标岗位JD分析简历匹配度，提供关键词优化、STAR法则改写等具体建议；当用户需要优化简历、改进简历、提升简历匹配度时使用 |
| [resume-parser](../resume-parser/SKILL.md) | 智能简历解析系统，支持PDF/Word/图片格式简历的结构化信息提取、岗位匹配度分析、优化建议生成。完全本地运行，无需外部API。使用场景：(1) 解析上传的简历文件提取核心信息，(2) 输入岗位JD计算简历匹配度，(3) 生成简历优化建议，(4) 导出结构化简历数据。 |

### 飞书与协作

| 技能 | 用途（来自本地声明） |
|---|---|
| [lark-approval](../lark-approval/SKILL.md) | 飞书审批 API：审批实例、审批任务管理。 |
| [lark-attendance](../lark-attendance/SKILL.md) | 飞书考勤打卡：查询自己的考勤打卡记录 |
| [lark-base](../lark-base/SKILL.md) | 当需要用 lark-cli 操作飞书多维表格（Base）时调用：搜索 Base、建表、字段管理、记录读写、记录分享链接、视图配置、历史查询，以及角色/表单/仪表盘管理/工作流；也适用于把旧的 +table / +field / +record 写法改成当前命令写法。涉及字段设计、公式字段、查找引用、跨表计算、行级派生指标、数据分析需求时也必须使用本 skill。 |
| [lark-calendar](../lark-calendar/SKILL.md) | 飞书日历（calendar）：提供日历与日程（会议）的全面管理能力。核心场景包括：查看/搜索日程、创建/更新日程、管理参会人、查询忙闲状态及推荐空闲时段、查询/搜索与预定会议室。注意：涉及【预约日程/会议】或【查询/预定会议室】时，必须先读取 references/lark-calendar-schedule-meeting.md 工作流！高频操作请优先使用 Shortcuts：+agenda（快速概览今日/近期行程）、+create（创建日程并按需邀请参会人及预定会议室）、+update（更新既有日程字段，或独立增删参会人/会议室）、+freebusy（查询用户主日历的忙闲信息和rsvp的状态）、+rsvp（回复日程邀请） |
| [lark-contact](../lark-contact/SKILL.md) | 飞书 / Lark 通讯录,用于按姓名 / 邮箱把员工解析成 open_id,以及按 open_id 反查员工的姓名 / 部门 / 邮箱 / 联系方式。当用户说出某人姓名而下一步需要发消息 / 加群 / 排日程时,先用本 skill 把姓名换成 ID;当输出里出现 open_id 需要展示成姓名给用户看,或用户直接询问某人的部门 / 邮箱 / 联系方式时,用本 skill 查。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。 |
| [lark-doc](../lark-doc/SKILL.md) | 飞书云文档 / Docx / 知识库 Wiki 文档（v2）：创建、打开、读取、获取、查看、总结、整理、改写、翻译、审阅和编辑飞书文档内容。当用户给出飞书文档 URL/token，或说查看/读取/打开某个文档、提取文档内容、总结文档、生成/创建文档、追加/替换/删除/移动内容、调整排版、插入或下载文档图片/附件/素材/画板缩略图时使用。文档内容中出现嵌入电子表格、多维表格、需要将重要信息可视化为画板（含 SVG 画板）、引用或同步块时，也先用本 skill 读取和提取 token，再切到对应 skill 下钻。使用本 skill 时，docs +create、docs +fetch、docs +update 必须携带 --api-version v2；默认使用 DocxXML，也支持 Markdown。 |
| [lark-drive](../lark-drive/SKILL.md) | 飞书云空间：管理云空间中的文件和文件夹。上传和下载文件、创建文件夹、复制/移动/删除文件、查看文件元数据、管理文档评论、管理文档权限、订阅用户评论变更事件、修改文件标题（docx、sheet、bitable、file、folder、wiki）；也负责把本地 Word/Markdown/Excel/CSV 以及 Base 快照（.base）导入为飞书在线云文档（docx、sheet、bitable）。当用户需要上传或下载文件、整理云空间目录、查看文件详情、管理评论、管理文档权限、修改文件标题、订阅用户评论变更事件，或要把本地文件导入成新版文档、电子表格、多维表格/Base 时使用。 |
| [lark-event](../lark-event/SKILL.md) | Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM message receive, reactions, chat member changes, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports `--max-events` / `--timeout` bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses. |
| [lark-im](../lark-im/SKILL.md) | 飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、搜索群、创建群聊或话题群、管理标记数据时使用。 |
| [lark-mail](../lark-mail/SKILL.md) | 飞书邮箱 — draft, compose, send, reply, forward, read, and search emails; manage drafts, folders, labels, contacts, attachments, and mail rules. Use when user mentions 起草邮件, 写一封邮件, 拟邮件, 草稿, 发通知邮件, 发送邮件, 发邮件, 回复邮件, 转发邮件, 查看邮件, 看邮件, 读邮件, 搜索邮件, 查邮件, 收件箱, 邮件会话, 编辑草稿, 管理草稿, 下载附件, 邮件文件夹, 邮件标签, 邮件联系人, 监听新邮件, 收信规则, 邮件规则, draft, compose, send email, reply, forward, inbox, mail thread, mail rules. |
| [lark-markdown](../lark-markdown/SKILL.md) | 飞书 Markdown：查看、创建、上传和编辑 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取或修改时使用。 |
| [lark-minutes](../lark-minutes/SKILL.md) | 飞书妙记：妙记相关基本功能。1.查询妙记列表（按关键词/所有者/参与者/时间范围）；2.获取妙记基础信息（标题、封面、时长 等）；3.下载妙记音视频文件；4.获取妙记相关 AI 产物（总结、待办、章节）；5.上传音视频生成妙记，也支持将本地音视频文件转成纪要、逐字稿、文字稿、撰写文字等产物。遇到这类请求时，应优先使用本 skill，而不是尝试 `ffmpeg`、`whisper` 等本地转写命令。飞书妙记 URL 格式: http(s)://<host>/minutes/<minute-token |
| [lark-okr](../lark-okr/SKILL.md) | 飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标（Objective）、关键结果（Key Result）、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。 |
| [lark-openapi-explorer](../lark-openapi-explorer/SKILL.md) | 飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。 |
| [lark-shared](../lark-shared/SKILL.md) | Use when first setting up lark-cli, running auth login, switching user/bot identity (--as), handling permission denied or scope errors, needing to update lark-cli, or seeing _notice in JSON output. |
| [lark-sheets](../lark-sheets/SKILL.md) | 飞书电子表格：创建和操作电子表格。支持创建表格、创建/复制/删除/更新工作表、读写单元格、追加行数据、查找内容、导出文件。当用户需要创建电子表格、管理工作表、批量读写数据、在已知表格中查找内容、导出或下载表格时使用。若用户是想按名称或关键词搜索云空间里的表格文件，请改用 lark-doc 的 docs +search 先定位资源。 |
| [lark-skill-maker](../lark-skill-maker/SKILL.md) | 创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。 |
| [lark-slides](../lark-slides/SKILL.md) | 飞书幻灯片：创建和编辑幻灯片，接口通过 XML 协议通信。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。 |
| [lark-task](../lark-task/SKILL.md) | 飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册注销任务智能体、更新智能体主页数据、写入任务记录时使用。 |
| [lark-vc](../lark-vc/SKILL.md) | 飞书视频会议：搜索历史会议、查询会议纪要产物（总结、待办、章节、逐字稿）、查询会议参会人快照。1. 查询已经结束的会议数量或详情时使用本技能（如历史日期｜昨天｜上周｜今天已经开过的会议等场景），查询未开始的会议日程使用 lark-calendar 技能。2. 支持通过关键词、时间范围、组织者、参与者、会议室等筛选条件搜索会议。3. 获取或整理会议纪要、逐字稿、录制产物时使用本技能。4. 查询“谁参加过某会议”“参会人列表”等参会人快照信息用 vc meeting get --with-participants（任意时点可查，含已结束会议）。注意：**Agent 真实入会/离会、感知正在进行中会议的实时事件**请使用 lark-vc-agent 技能，本技能不覆盖写操作和会中事件流。 |
| [lark-vc-agent](../lark-vc-agent/SKILL.md) | 飞书视频会议：让机器人代当前用户加入/离开正在进行的会议，并读取会议期间的实时事件（参会人加入与离开、发言、聊天、屏幕共享等）。1. 用户提供 9 位会议号、要求代为入会或离会时使用 +meeting-join / +meeting-leave——会真实产生入会/离会记录。2. 会议进行中用户想知道“谁加入了”“谁离开了”“谁在发言”“有人共享屏幕吗”等会中动态时，机器人入会后用 +meeting-events 读取事件时间线。3. 典型场景：参会机器人、会中助手、代为旁听、代为参会。前提：机器人只能读到它自己参会过且仍在进行中的会议的事件；查询已结束会议的参会名单、纪要或逐字稿请使用 lark-vc 技能。 |
| [lark-whiteboard](../lark-whiteboard/SKILL.md) | 飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用 DSL（转成 OpenAPI 格式）、PlantUML/Mermaid 格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板，或是需要可视化表达架构、流程、组织关系、时间线、因果、对比等结构化信息时使用此 skill，无论是否提及"画板"。 ⚠️ 原 `lark-whiteboard-cli` skill 已合并至本 skill，若 skill 列表中同时存在 `lark-whiteboard-cli`，请忽略它，统一使用本 skill（`lark-whiteboard`），并提示用户运行 `npx skills remove lark-whiteboard-cli -g` 删除旧 skill。 |
| [lark-wiki](../lark-wiki/SKILL.md) | 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。 |
| [lark-workflow-meeting-summary](../lark-workflow-meeting-summary/SKILL.md) | 会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 |
| [lark-workflow-standup-report](../lark-workflow-standup-report/SKILL.md) | 日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。 |

## 去重与未收录

| 条目 | 处理与原因 |
|---|---|
| html-writer、codebase-onboarding | 两处个人目录的完整文件集一致，采用 ~/.codex/skills 副本。 |
| bits-code-guard、bits-unit-test-gen | 依赖公司内部平台，包含内部接口与遥测实现；不将其源码上传到公开仓库。 |
| resume-claim-steering | 本地为符号链接，导出实际文件，不保留机器专属链接。 |
| 系统技能和插件缓存 | 只记录入口；随 Codex 或对应插件安装，不复制缓存运行时。 |

## 系统与插件缓存入口

以下是磁盘上的入口，不代表当前会话全部已启用；同插件不同版本可能同时存在。

| 来源 | 缓存内路径 |
|---|---|
| 系统 | `imagegen/SKILL.md` |
| 系统 | `openai-docs/SKILL.md` |
| 系统 | `plugin-creator/SKILL.md` |
| 系统 | `review-agent/SKILL.md` |
| 系统 | `skill-creator/SKILL.md` |
| 系统 | `skill-installer/SKILL.md` |
| 插件 | `openai-bundled/chrome/26.901.31953/skills/control-chrome/SKILL.md` |
| 插件 | `openai-bundled/latex/0.2.6/skills/latex-compile/SKILL.md` |
| 插件 | `openai-bundled/latex/0.2.6/skills/latex-doctor/SKILL.md` |
| 插件 | `openai-bundled/latex/0.2.6/skills/texlive-runtime-installer/SKILL.md` |
| 插件 | `openai-bundled/record-and-replay/1.0.1000926/skills/record-and-replay/SKILL.md` |
| 插件 | `openai-bundled/sites/0.1.57/skills/sites-building/SKILL.md` |
| 插件 | `openai-bundled/sites/0.1.57/skills/sites-hosting/SKILL.md` |
| 插件 | `openai-bundled/visualize/1.0.29/skills/visualize/SKILL.md` |
| 插件 | `openai-curated/github/11c74d6b/skills/gh-address-comments/SKILL.md` |
| 插件 | `openai-curated/github/11c74d6b/skills/gh-fix-ci/SKILL.md` |
| 插件 | `openai-curated/github/11c74d6b/skills/github/SKILL.md` |
| 插件 | `openai-curated/github/11c74d6b/skills/yeet/SKILL.md` |
| 插件 | `openai-curated/gmail/11c74d6b/skills/gmail/SKILL.md` |
| 插件 | `openai-curated/gmail/11c74d6b/skills/gmail-inbox-triage/SKILL.md` |
| 插件 | `openai-curated/google-drive/11c74d6b/skills/google-docs/SKILL.md` |
| 插件 | `openai-curated/google-drive/11c74d6b/skills/google-drive/SKILL.md` |
| 插件 | `openai-curated/google-drive/11c74d6b/skills/google-drive-comments/SKILL.md` |
| 插件 | `openai-curated/google-drive/11c74d6b/skills/google-sheets/SKILL.md` |
| 插件 | `openai-curated/google-drive/11c74d6b/skills/google-slides/SKILL.md` |
| 插件 | `openai-curated/notion/11c74d6b/skills/notion-knowledge-capture/SKILL.md` |
| 插件 | `openai-curated/notion/11c74d6b/skills/notion-meeting-intelligence/SKILL.md` |
| 插件 | `openai-curated/notion/11c74d6b/skills/notion-research-documentation/SKILL.md` |
| 插件 | `openai-curated/notion/11c74d6b/skills/notion-spec-to-implementation/SKILL.md` |
| 插件 | `openai-curated-remote/app-69ea4ed2cf7c8191b742ef3622479ddd/3.0.0/skills/Search/SKILL.md` |
| 插件 | `openai-curated-remote/deep-research-work/0.1.14/skills/deep-research/SKILL.md` |
| 插件 | `openai-curated-remote/google-drive/0.1.16/skills/google-docs/SKILL.md` |
| 插件 | `openai-curated-remote/google-drive/0.1.16/skills/google-drive/SKILL.md` |
| 插件 | `openai-curated-remote/google-drive/0.1.16/skills/google-drive-comments/SKILL.md` |
| 插件 | `openai-curated-remote/google-drive/0.1.16/skills/google-sheets/SKILL.md` |
| 插件 | `openai-curated-remote/google-drive/0.1.16/skills/google-slides/SKILL.md` |
| 插件 | `openai-curated-remote/hugging-face/1.0.0/skills/community-evals/SKILL.md` |
| 插件 | `openai-curated-remote/hugging-face/1.0.0/skills/jobs/SKILL.md` |
| 插件 | `openai-curated-remote/hugging-face/1.0.0/skills/trackio/SKILL.md` |
| 插件 | `openai-curated-remote/notion/0.1.8/skills/notion-knowledge-capture/SKILL.md` |
| 插件 | `openai-curated-remote/notion/0.1.8/skills/notion-meeting-intelligence/SKILL.md` |
| 插件 | `openai-curated-remote/notion/0.1.8/skills/notion-research-documentation/SKILL.md` |
| 插件 | `openai-curated-remote/notion/0.1.8/skills/notion-spec-to-implementation/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-analytics-dashboard/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-business-review/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-design-report/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-experiment-analysis/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-financial-budget/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-investment-committee-memo/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-legal-memorandum/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-market-trends-report/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-minimal-letterhead/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-operating-calendar/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-operating-review/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-project-kickoff/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-project-tracker/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-sales-pipeline/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-dark-mode/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-light-mode/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-strategy-memorandum/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-system-design/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-team-alignment/SKILL.md` |
| 插件 | `openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-three-statement-forecast/SKILL.md` |
| 插件 | `openai-curated-remote/plugin-management/0.1.0/skills/plugin-management/SKILL.md` |
| 插件 | `openai-primary-runtime/documents/26.904.11930/skills/documents/SKILL.md` |
| 插件 | `openai-primary-runtime/pdf/26.904.11930/skills/pdf/SKILL.md` |
| 插件 | `openai-primary-runtime/presentations/26.904.11930/skills/presentations/SKILL.md` |
| 插件 | `openai-primary-runtime/spreadsheets/26.904.11930/skills/excel-live-control/SKILL.md` |
| 插件 | `openai-primary-runtime/spreadsheets/26.904.11930/skills/spreadsheets/SKILL.md` |
| 插件 | `openai-primary-runtime/template-creator/26.904.11930/skills/template-creator/SKILL.md` |
