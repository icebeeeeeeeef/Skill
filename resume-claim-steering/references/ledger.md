# Claim ledger

Single source of truth for facts, wording, and interview depth. Do not duplicate this schema in SKILL.md.

## Claim types

| Type | Triggers | Must be grillable on |
|---|---|---|
| `ownership` | 主导 / Owner / 独立负责 / 核心开发 / 0→1 | 你负责的模块、你做的决策、别人做什么 |
| `metric` | 提升 / 降低 / P99 / 命中率 / QPS | baseline、分母、窗口、来源、个人 vs 团队 |
| `technical` | 具体技术名 | 在项目中的输入输出、你做的部分、选型原因 |
| `architecture` | 多级 / 拆分 / 池化 / 解耦 | 组件、数据流、边界、失败路径、扩展限制 |
| `result` | 上线 / 被采用 / 降本 / 支撑 | 谁在用、如何衡量、你的动作如何导致该结果 |

## Status

| Status | May enter |
|---|---|
| `已确认` | 正式简历 |
| `待确认` | 审计稿，必须带 `【待补】` |
| `不采用` | 仅复盘，不对外 |

Conflict between sources → keep one record, list sources, set `待确认`. Never confirm the prettier number.

## Responsibility levels

`参与` < `负责模块` < `主导方案或交付` < `项目负责人`

Upgrade a level only with evidence of decision or delivery, not effort.

## Record fields

Required: `id`, `type`, `source_fact`, `candidate_wording`, `intensity`, `responsibility_level`, `boundary`, `verification_status`.

Optional: `sources`, `hook`, `interview_details`, `risk_notes`, `allowed_uses`.

`source_fact` is never rewritten for style. Change `candidate_wording`, not the fact.

`intensity`:

- `safe` — 扫描层，结果 + 边界，无非常规对比
- `ambitious` — 含钩子或强动词；必须填 `hook` + `interview_details`

## Hook object

```yaml
hook:
  conventional: 常规方案
  chosen: 实际方案
  constraint: 为何这次不能走常规
  fatal_flaw_of_conventional: 常规方案在此约束下的致命点
```

If any of these four is empty, the claim cannot stay `ambitious`.

## Interview details

```yaml
interview_details:
  decision: 为什么这样选
  alternative: 为什么不用另一种
  failure: 失败 / 回滚 / 异常
  metric_method: 指标怎么测
  cost: 方案牺牲了什么
  redo: 再做一次会改什么
```

Ambitious claims need at least `alternative`, `failure`, `metric_method`, and `boundary`.

## Table form (chat)

When not writing a file, present:

| id | type | intensity | source_fact | candidate_wording | boundary | status |
|---|---|---|---|---|---|---|

Put hook and interview_details under the table, grouped by id.
