---
name: resume-claim-steering
description: Turns real project facts into a target-role resume (project spine + bullets) and a grillable interview question tree, gated by a claim-evidence ledger so wording cannot outrun facts. Use when the user wants to 写简历, 改写项目, 包装经历, 酥化, 写 bullet, 生成面试题, 话题树, 主张账本, 问穿简历, 模拟面试, 准备技术面, or runs /resume-claim-steering. Also use when discussing a project in order to produce resume text and interview prep together.
---

# Resume Claim Steering

简历是主张账本驱动的面试脚本。酥化是翻译层级（动作 → 系统能力 → 业务价值 → 结果证据 → 个人边界），不是虚构头衔、技术栈或数据。

默认中文输出。字段名、模式名保持英文，便于账本交接。

## Modes

Infer from the user. If they paste a project and a JD, run `full` then stop before `grill` unless they ask to be questioned.

| Mode | Trigger | Deliver |
|---|---|---|
| `pack` | 讨论项目 / 酥化 / 包装 | 定位 + 账本 + 改写稿 |
| `resume` | 写简历 / 改 bullet | 可上简历的项目块 |
| `tree` | 面试题 / 话题树 | 每条 Claim 的问题树 |
| `grill` | 问穿 / 模拟面试 | **每轮只问一个问题** |
| `full` | 默认 | pack + resume + tree |

## Hard rules

1. 不编造 title、公司、时间、技术栈、指标、所有权。缺事实写 `【待补】`，并最多追问 5 个关键缺口。
2. 团队成果不自动变成个人成果。强动词（主导 / Owner / 0→1）必须有决策、交付或评审证据。
3. 技术名词后面必须有动作或结果。禁止技能清单式 bullet。
4. 进取钩子必须填 `interview_details`。讲不清「替代 / 失败 / 口径 / 边界」的钩子不得进入最终简历。
5. 一个项目 2–5 条 bullet；深钩子最多 2 条。第一条是扫描层（结果 + 规模 + 边界）。
6. `grill` 不准一次倒出整棵树，也不准在用户尝试前给可背诵的标准答案。
7. 最终简历只收 `verification_status: 已确认`。`待确认` 可留在审计稿。

## Workflow

Follow in order. Skip a later step only if the user asked for a single mode.

### 1. Intake

Collect: 目标岗位 / JD、原始经历、职责边界、指标口径、公开证据。先写 `source_fact`，再写文案。材料冲突时标 `待确认`，不选更好看的版本。

### 2. Position

Output 稳妥版 and 进取版 one-liners. 进取版必须列出还缺的证据。定位必须是岗位能认的身份，不是技术名词堆砌。

### 3. Ledger

Split the project into Claims. Schema and types: [references/ledger.md](references/ledger.md).  
Every bullet that will ship must point to one claim id.

### 4. Spine + bullets

Project block shape:

```text
[项目名 | 全景：对象 + 约束 + 你动了哪条路径]
  · 背景/目标
  · 个人职责（边界）
  · 关键设计选择（钩子，0–2 条）
  · 硬实现（名词 + 动作）
  · 结果证据（带口径）
  · （可选）回滚/演进
```

Sentence patterns, hook types, intensity ladder: [references/bullets.md](references/bullets.md).

### 5. Hook gate

For each ambitious bullet, the user must be able to speak 90 seconds on: 常规方案、为何不用、代价、失败/回滚、指标口径。不能则降为稳妥版或删除钩子。

### 6. Question tree

Build trees from Claims, not from generic 八股. Structure and grill protocol: [references/trees.md](references/trees.md).

### 7. Output

Always return, in this order:

1. 一句话定位（稳妥 / 进取）
2. Claim 账本（表格或 YAML）
3. 简历项目块（稳妥稿；进取稿单独标明）
4. 话题树（按 claim id）
5. 上简历门禁：可上成稿 / 必须【待补】/ 建议删除
6. 最多 5 个待补问题

Worked example (systems / KV path, as illustration only): [references/examples.md](references/examples.md). Do not force this domain onto unrelated projects.

Template: [assets/claim-ledger-template.yaml](assets/claim-ledger-template.yaml).

## Red flags — stop and rewrite

- 「负责 / 参与 / 使用了 XXX」没有对象、动作、边界
- 百分比没有 baseline、分母、时间窗、数据来源
- 钩子像没见过常规方案，而不是判断
- 功能清单冒充项目主线
- 把计划写成已完成
- `grill` 一次抛出 10 个问题
- 为了钩子补假实现

## Common mistakes

| Failure | Fix |
|---|---|
| 先写漂亮句子再找事实 | 先 ledger 再 wording |
| 条条 instead of | 每项目最多 2 个深钩子 |
| 技能栏有、经历里无 | 删技能或补落地动作 |
| 面试树和简历脱节 | 每道题必须回指 claim id |
| 讲不清仍保留进取表述 | 降强度，不编细节 |
