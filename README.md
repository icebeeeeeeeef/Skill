# Skills

个人 Codex 技能集：保存可复用的工作方法、脚本、模板和参考资料。

本次整理收录 **90 个技能**，完整分类和本地系统/插件入口见 [技能清单](docs/CATALOG.md)，来源及文件校验值见 [导出清单](docs/manifest.json)。沿用仓库原有的根目录布局。

## 从哪些开始

- 日常工程：`proofloop`、`codebase-onboarding`、`codebase-design`、`domain-modeling`。
- 方案讨论：`steelman`、`ponytail-review`；复杂任务按需选 `wayfinder`。
- 研究和解释：`research`、`technical-research`、`show-me`、`html-writer`。
- 求职表达：`evaluating-career-projects`、`bullet`、`resume-claim-steering`。
- 飞书工作：按用途选择 `lark-*`，同时保留 `lark-shared`。

其他技能作为可选工具保留。`proofloop`、Superpowers 流程、TDD 和多智能体技能的触发规则有重叠，建议按需安装，不把所有流程叠加为默认要求。`MAW` 是显式调用的受控多智能体方法。

## 安装

将选中的整个技能目录复制到 `~/.agents/skills/` 或 `~/.codex/skills/`，不要只复制 `SKILL.md`。两处不要重复安装同名技能。

例如，在本仓库目录运行以下命令安装一个尚未安装的技能；若已存在则先比较内容：

```bash
mkdir -p "$HOME/.agents/skills"
if [ ! -e "$HOME/.agents/skills/steelman" ]; then
  cp -R steelman "$HOME/.agents/skills/steelman"
fi
```

重新开启会话后检查技能是否被发现。技能目录内 `agents/openai.yaml` 是附带元数据；仓库根部 `agents/proofloop-matrix-reviewer.toml` 是已有的 reviewer 配置，需要单独按运行环境配置。

## 外部依赖与边界

| 技能 | 需要另外准备的能力 |
|---|---|
| `lark-*` | `lark-cli`、登录授权和对应 API 权限；CLI 本身不在仓库中。 |
| `zhihu-search`、`global-search`、`hot-list`、`zhida` | Python 3 和技能说明中的知乎环境变量；密钥不在仓库中。 |
| `technical-research` | 可选 `cn-article-search` 独立运行时；缺失时使用公开搜索并说明覆盖范围。source-registry 是历史快照。 |
| `grok-build-cli` | 单独安装、登录 Grok CLI。 |
| `playwright` | Node.js、npm/npx 与浏览器环境，按技能说明安装。 |
| `resume-parser` | 按脚本准备 PDF/Word/OCR 依赖；OCR 需要 Tesseract。 |
| `html-writer`、`interactive-mindmap` 等 | 部分模板通过 CDN 加载 JS/CSS，完整渲染可能需要网络。 |
| issue、PR 与多智能体类技能 | 对应 GitHub/GitLab 工具、任务跟踪和子智能体能力；工具名称可能需按宿主适配。 |

本次做目录完整性、文件校验和脚本语法检查，不会调用外部服务、运行技能中的发布动作，或宣称全部技能已在新机器上端到端验证。

## 来源与许可

这是个人本地技能收藏，包含自定义和第三方材料，并非全部原创。保留各目录已有的 LICENSE、来源链接和署名；没有许可证的目录标记为“本地未附许可”，不对其追加统一许可或宣称已取得额外授权。详见导出清单。

系统技能与插件缓存从原安装渠道恢复；公司内部专用技能不收录。没有导出账户配置、认证文件、个人记忆或浏览器数据。
