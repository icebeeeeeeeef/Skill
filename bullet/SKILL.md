---
name: bullet
description: >
  将候选人真实完成或参与的软件工程项目、实习产出、性能优化、系统设计、
  故障治理与基础设施工作，转化为面向目标岗位、便于快速扫描且能经受技术追问的
  简历 bullet。适用于已有事实材料的提炼、重写和审查；不用于创造经历、补写
  未验证指标或夸大个人 ownership。
---

# Project Experience to Defensible Resume Bullets

## Goal

把真实工程事实压缩成一组让招聘者快速判断、让面试官自然追问的证据。

优化顺序是：

1. 事实与 attribution 正确；
2. 与目标岗位相关；
3. 快速读懂问题、个人动作和结果；
4. 暴露一个候选人真正理解的技术决策、约束或失败模式；
5. 语言精炼。

“面试 hook”只能来自可验证事实。不得故意省略关键上下文制造悬念，也不得为了触发追问添加 buzzword、数字或虚假的决策权。

## Boundaries

- 不创造事实、规模、指标、技术栈、用户影响或 ownership。
- 不把 `roadmap`、原型、实验、局部验证、上线和生产效果混成同一 claim state。
- 不把团队或上游结果全部归因于个人。
- 不因 JD 出现关键词而把无关经历重命名成目标领域项目。
- 不泄露 NDA、内部机密或无法公开的精确数字；必要时使用经确认的范围或定性证据。

若材料不足，先提出最少量的事实问题；仍未知的内容标记为：

`UNKNOWN`、`NOT MEASURED`、`TEAM-OWNED`、`UPSTREAM`、`EXPERIMENTAL`、`PLANNED`。

## Workflow

### 1. Establish the claim ledger

不要直接润色。先为每个候选 claim 确认：

- `Problem / Why`：解决了什么问题，谁因此受益；
- `My action`：本人实现、设计、诊断、推动或评估了什么；
- `Boundary`：团队、Tech Lead、上游系统分别负责什么；
- `Constraint / Decision`：真正影响方案的约束、替代方案或关键判断；
- `Evidence`：交付事实、采用范围、规模、可靠性或 before/after 结果；
- `Measurement`：指标口径、baseline、workload、时间窗口和数据来源；
- `Claim state`：shipped、production-observed、experimentally validated、prototype、planned 等。

只收录本人能解释证据来源和归因链的 claim。详细 intake 模板见 [references/intake-and-review.md](references/intake-and-review.md)。

### 2. Select evidence for the target role

从全部真实工作点中选择 2–4 个最能证明目标岗位能力的点，而不是复述模块清单或耗时最多的工作。

优先选择：

- 有意义的问题或结果；
- 清晰的个人 ownership；
- 非平凡约束、故障或技术判断；
- 可解释的验证方法；
- 与目标岗位直接相关的技术对象。

同一项目的 bullets 应形成组合，而不是每条都塞满全部信号。常见组合是：

- outcome / scope；
- technical decision / constraint；
- validation / reliability / rollout。

### 3. Write one causal spine per bullet

默认结构：

`personal action + object/context + decision or mechanism + defensible evidence`

根据事实删减其中不重要的项。每条只保留一条主线，通常控制在简历中的 1–2 行；不要为了套模板牺牲可读性或事实边界。

写作规则：

- 用与真实 ownership 匹配的动词开头；
- 把关键技术词放在具体动作、决策或故障语境中；
- 有指标时优先写 baseline、结果、单位和必要的 workload；
- 没有指标时，使用真实的交付、采用、规模、SLO、故障消除、迁移完成或能力解锁证据；
- 把最强、最相关的 bullet 放在最前；
- 删除职责描述、技术栈清单、形容词和重复背景。

不要强迫每条 bullet 同时拥有数字、trade-off 和 hook。数字不是结果的替代品，复杂度也不是技术数量。

### 4. Run the two-reader check

先模拟招聘者快速扫描：

- 能否迅速看出项目对象、本人动作、结果或规模、岗位相关性？
- 最强信息是否出现在句首和首条 bullet？
- 是否存在只有作者自己懂的内部名词？

再模拟技术面试官深挖：

- 为什么做、为什么这样做、有哪些替代方案？
- 个人贡献与团队边界是什么？
- 数据流、瓶颈、失败处理或 rollout 如何工作？
- 指标怎么测，结果如何归因，有什么代价或边界？

自然 follow-up 是筛选通过后的附加价值，不是替代清晰度的目标。

### 5. Apply admission gates

每条最终 bullet 必须全部通过：

1. `Truth`：所有名词、动词、数字和完成状态都可核验；
2. `Attribution`：个人动作和团队结果没有混淆；
3. `Relevance`：证明目标岗位关心的能力；
4. `Comprehension`：脱离项目文档仍能快速读懂；
5. `Evidence`：至少有一种可解释证据，而非形容词；
6. `Defensibility`：候选人能解释问题、机制、验证和边界，并能坦诚说出不知道或未负责的部分。

任一硬门槛失败：降级 claim、补证据或删除，不使用总分抵消。

## Ownership language

动词必须匹配事实：

- `Owned / Designed / Architected / Drove`：本人承担相应决策权和结果责任；
- `Implemented / Built / Delivered`：本人完成具体实现或交付，但不暗示方案归属；
- `Diagnosed / Evaluated / Measured`：本人完成定位或验证；
- `Contributed / Integrated`：本人参与其中一个明确部分。

避免空泛的 `Responsible for`、`Participated in`。如果精确范围更有信号，直接写范围。

## Evidence and metrics

指标只有在候选人能解释以下内容时才进入 bullet：

- 指标定义和单位；
- baseline 与结果；
- workload / 时间窗口 / 实验或 dashboard 来源；
- 个人工作到结果之间的合理归因；
- 已知回归、代价或适用边界。

若数字属于团队或全链路，只描述本人影响链，不把整体结果改写成个人结果。无法确认的数字删除或改成真实的 scope；不得让模型“估一个合理数字”。

如果指标被同版本的其他改动、流量变化或团队工作严重混杂，不要在成稿 bullet 中加入冗长的 attribution caveat。优先省略该指标，保留可归因的交付、故障、验证或规模证据，并在 `Claim and ownership risks` 中说明该团队指标为何不能作为个人 impact。

## Output modes

默认输出：

1. `Recommended wording`：必要时给一句项目定位，加 2–4 条按重要性排序的 bullets；
2. `Claim and ownership risks`：只列会改变措辞或需要确认的风险；
3. `Missing evidence`：只列能显著增强 claim 的少量事实或测量项。

如果用户要求面试准备，再补充：

4. `Natural follow-up map`：每个旗舰 bullet 的 3–5 个高概率追问；
5. `Defensibility notes`：baseline、替代方案、失败、trade-off、本人/团队边界；
6. `Weak-point drill`：最可能击穿 claim 的一个问题及诚实回答边界。

如果用户只要求简历成稿，不默认输出长篇评分解释或完整追问树。

## Final principle

写的不是“最像高手”的 bullet，而是：

> 对目标岗位最有信号、在快速扫描中最清楚，并且在深度追问下仍然成立的最短真实表述。
