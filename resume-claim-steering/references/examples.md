# Worked example

Illustration only. Apply the same shape to the user's real facts; do not copy metrics or ownership.

## Raw fact

In a serving team, the candidate wrote the local NVMe offload path for prefix KV. Prefix match used the engine's existing hash. They used io_uring and a page-first layout. A layer-wise POSIX dump was tried and rolled back. Scheduler was not theirs. TTFT dropped on a shared 8K prefix, measured on one machine.

## Position

- 稳妥：熟悉推理 KV 的本机卸载路径，能从页布局和 IO 通路解释前缀复用。
- 进取：做过 HBM→NVMe 的换入换出，并用非常规 IO 路径打满顺序读。缺：跨机池化、PD 传输证据。

## Ledger (abridged)

| id | type | intensity | source_fact | status |
|---|---|---|---|---|
| c1 | architecture | safe | 把可复用前缀从 HBM 卸到本机 NVMe | 已确认 |
| c2 | ownership | safe | 负责卸载数据通路和页布局；匹配器用引擎已有模块 | 已确认 |
| c3 | technical | ambitious | page-first + io_uring registered buffer，替代 POSIX 按层读 | 已确认 |
| c4 | metric | safe | 共享 8K 前缀二次请求 TTFT 从 A 到 B，单机对比关卸载 | 待确认（数字） |
| c5 | result | safe | 按层落盘因小 IO 打不满 SSD 被回滚 | 已确认 |

c3 hook: conventional=`POSIX 按层 pread + cudaMemcpy`；chosen=`page-first + io_uring`；constraint=`不改计算图、热路径不走 FUSE`；fatal=`80 层变成 80 次小 IO`。

c4 stays `待确认` until A/B and method are confirmed. Resume uses qualitative result until then.

## Resume block (safe + one hook)

> **前缀 KV 本机卸载与复用 | 推理引擎侧**  
> 长上下文共享前缀使 HBM 装不下工作集；在不改模型计算、热路径不走 FUSE 的前提下，把可复用前缀卸到本机 NVMe。

- 目标是减少重复 prefill。我负责卸载数据通路和页布局，前缀匹配沿用引擎已有 hash/radix。
- 用 page-first 把分层小块收成对齐页，再用 io_uring registered buffer 批量读，替代 POSIX 按层拷；避开 FUSE 额外拷贝和单队列。
- 共享前缀的二次请求 TTFT 明显下降（口径：单机、固定 prompt、对比关闭卸载）。【待补：A→B 数字】未做跨机池化和 PD 传输。
- 灰度时回滚过按层直接落盘：实现简单，但层数变成多次小 IO，SSD 带宽打不满。

## Tree for c3 (ambitious)

```text
Claim c3（technical / ambitious）
Q：为什么不用 POSIX 按层读？
考察：替代方案、约束、IO 放大
回答应覆盖：常规路径拷贝次数、page-first 如何合并 IO、FUSE 为何排除、回滚证据
下一层：不对齐时发生什么？registered buffer 钉的是什么？
```

Do not paste the full ten directions into the resume. Keep them in the tree for `grill`.
