# Spine and bullets

## Translation chain

Rewrite in this order. Drop a slot only if it would be invented.

`动作 → 系统能力 → 业务价值 → 结果证据 → 个人边界`

- 动作：亲手做了什么
- 系统能力：对目标岗位证明你会什么（不是工具名）
- 业务价值：对系统/用户意味着什么
- 结果证据：怎么证明，带口径
- 个人边界：你 vs 团队

## Spine

One line outsiders can repeat:

`对象 + 硬约束 + 你动了哪条路径`

Bad: 基于 Spring / vLLM / Redis 的 XXX 系统  
Good: 在〔约束〕下，把〔对象〕从〔旧路径〕改到〔新路径〕

Then 2–5 bullets as an arc: 目标 → 职责 → 选择 → 实现 → 证据 →（可选）回滚。

## Sentence patterns

Scan layer (bullet 1):

> 在〔约束〕下，把〔对象〕做成〔结果〕（〔口径〕）；我负责〔边界〕。

Hook layer (at most two):

> 用〔具体方案〕做成〔效果〕；相对〔常规方案〕，避开了〔致命点〕。

Implementation layer:

> 〔技术名词〕+〔动作〕+〔在本项目中的作用〕。

Never: 「使用 RDMA / 熟悉 GDS / 参与性能优化」。

## Intensity ladder

Same fact, three wordings. Ship the highest intensity that still has `已确认` evidence.

| Intensity | Contains | Gate |
|---|---|---|
| 过虚 | 主导架构、大幅提升、业界领先 | `不采用` |
| 稳妥 | 动作 + 边界 + 定性或带口径的结果 | 可上成稿 |
| 进取 | 稳妥 + 非常规对比或强所有权 | 钩子四字段 + 90 秒口述 |

## Hook types

Plant a gap the interviewer will naturally ask. Do not write the full answer on the resume.

| Type | Gap on the page | Likely question |
|---|---|---|
| 非常规选择 | 用 X 而不是常见 Y | 为什么不用 Y |
| 约束 | 不增加组件 / 不能停机 / 不走 FUSE | 为什么有这个限制 |
| 反直觉指标 | P99 从 A 到 B | 怎么做到，瓶颈在哪 |
| 正确性 | 幂等 / 对账 / 一致性 | 失败了怎么办 |
| 所有权 | 我负责某层 | 上下游谁做什么 |
| 明确拒绝 | 没有拆成微服务 / 没有上分布式 | 为什么不 |
| 事故回滚 | 灰度后回滚了某方案 | 出了什么问题 |
| 规模锚点 | 峰值 QPS / 数据量 | 怎么压，热点怎么打散 |

Rules:

- 钩子必须像判断，不像没见过常规方案。要配约束或一次失败过的常规尝试。
- 第一条仍要能被快速扫懂。钩子放第 2–3 条。
- 一个项目 1–2 个深钩子。不要条条 instead of。

## Shipping checklist

A project block may ship only if:

1. 不看公司名也能说出这是什么系统、你解决了什么
2. 每条 bullet 能回指一个 claim id
3. 技术名词后面有动作
4. 有数字则能一句话说清口径
5. 「我」和「团队」已分开
6. 进取钩子能讲 90 秒：替代 / 失败 / 代价
7. 该块在帮目标岗位，而不是无关功能清单
