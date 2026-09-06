# Query Templates

Start with entity disambiguation, then generate 6-12 focused queries.

## Entity Expansion

Include:

- English name and Chinese name.
- Repo/org names.
- Component names.
- Old names and adjacent project names.
- API names, config keys, and error text.
- Content type words: `源码解析`, `工程实践`, `设计`, `原理`, `benchmark`, `case study`, `tutorial`, `implementation`, `issue`, `RFC`.

## Intent Routes

`learn_technology`:

```text
{project} quickstart
{project} official docs architecture
{project} tutorial
{project} 原理
{project} 源码解析
{project} 工程实践
```

`engineering_practice`:

```text
{project/component} engineering blog
{project/component} production
{project/component} case study
{project/component} 实践
{project/component} 线上
{project/component} 性能优化
```

`implementation_discovery`:

```text
{capability} GitHub
{capability} library
{capability} package
{capability} paper implementation
{capability} Hugging Face
{capability} 替代方案
```

`troubleshooting`:

```text
"{exact error}"
{project} {exact error}
{project} GitHub issue {error_keyword}
{project} FAQ {error_keyword}
{project} 报错 {error_keyword}
```

## LLM Serving / KV Cache Seeds

```text
Mooncake KVCache
kvcache-ai Mooncake
Mooncake Store
Mooncake Transfer Engine
Mooncake PD disaggregation
Mooncake vLLM
Mooncake SGLang
SGLang HiCache Mooncake
LMCache Mooncake connector
KV Cache offload engineering practice
GPU CPU KV transfer
LLM serving PD separation
Agent tool gap KV cache
```
