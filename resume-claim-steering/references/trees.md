# Question trees

Trees are generated from ledger Claims, not from generic interview banks. Every question carries a `claim id`.

## Ten directions

For each claim, consider:

```text
背景   为什么要做
职责   你具体负责哪部分
结构   组件、数据流、边界
实现   关键流程如何落地
决策   为什么这样选
替代   为什么不用另一种方案
失败   哪里失败过，如何处理
指标   如何证明有效
代价   方案牺牲了什么
复盘   重新做一次会改什么
```

Do not emit all ten if the claim is `safe` and thin. Minimum:

- `safe`: 职责 + 实现 + 指标口径
- `ambitious`: 以上 + 替代 + 失败 + 代价 + 边界

## Predict output

```text
Claim [id]（type / intensity）
Q：……
考察：……
回答应覆盖：……
下一层：……
```

Sort by risk × relevance to the JD. Ownership, metric-without-method, and hooks go first.

## Grill protocol

1. Pick the highest-risk unvalidated claim.
2. Ask **one** question.
3. After the answer, score only current evidence: 正确性 / 具体性 / 个人边界 / 深度 / 证据 / 与简历一致性。
4. If fuzzy, go one layer down on the same claim. Do not switch claims until this branch has enough evidence or the user asks to move on.
5. Do not supply a recitable model answer before the user tries. A small hint or “先答职责再答实现” is allowed.

Fuzzy signals that require a follow-up:

- 负责 / 优化 / 提升 而无动作
- 有数字而无 baseline 和口径
- 主导 / Owner 而划不清边界
- 只会 happy path
- 会背术语，说不清在项目中的作用
- 只讲结果，不讲实现或 trade-off
- 与简历或上一轮回答矛盾

## Review output

```text
## Resume Mastery Review

### 已验证
- Claim：…… 证据：……

### 高风险
- Claim：…… 风险：…… 依据：……

### 面试前行动
1. ……

### 简历表述建议
- 原表述：……
- 稳妥表述：……
- 仍需确认：……
```

If the user has not answered enough, state the sample is insufficient. Never invent a fake score.

## After grill

Three options only: 补事实、补知识、降低简历强度。Do not fabricate missing implementation so the ambitious wording can survive.
