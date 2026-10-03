# learnx

学习教练，唯一入口 `/learnx <需求>`。内部是"路由层 + 按需读取的模式文件"：

```
learnx/
├── SKILL.md        路由层：识别需求 → 选模式 → 读对应文件
├── core.md         所有模式共享的规则（先预测再揭晓、反例优先、答案策略三档、事实来源……）
├── storage.md      存储：能连 Notion 就写 Notion，否则写 ~/learnx-data/ 并在之后提示同步
├── modes/          plan · sources · teach · read · code · replay · review · locate · record · rebuild · evolve
├── templates/      问题卡片 · 工程日志 · 重放 issue · 学习计划
└── CHANGELOG.md
```

## 用法示例

- `/learnx 帮我定一下这两周的学习计划`
- `/learnx 我想学 PagedAttention`（加"直接讲"切换为直接讲解）
- `/learnx 精读 DistServe 第 3 节`
- `/learnx 追一下 vLLM 里请求从进入到第一个 token 的路径`
- `/learnx 复习`
- `/learnx 你能做什么`

## 安装（Devin CLI）

把整个 `learnx/` 目录复制到全局 skills 目录，不要只复制 `SKILL.md`：

- Windows：`%APPDATA%\devin\skills\learnx\`
- Linux / macOS：`~/.config/devin/skills/learnx/`

frontmatter 里的 `triggers` 只设了 `user`，不会在普通会话里自动触发。`argument-hint`、`triggers` 是 Devin CLI 的字段，其他宿主可能会忽略。

## 存储

Notion 位置写在 `storage.md`（Kvwall / 知识的学习 / learnx 学习数据）。换了 Notion 工作区时，只需改这一个文件。Notion 不可用时写入 `~/learnx-data/`。
