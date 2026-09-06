# Source Policy

Use the highest available evidence tier that fits the task.

## Default Evidence Order

1. Official docs, official tutorials, RFCs, design docs.
2. Official repository source, tests, issues, PRs, releases.
3. Maintainer/team/company engineering blogs and vendor developer communities when the author is an official product/team account.
4. Papers and official implementations.
5. Conference talks and complete technical writeups.
6. High-quality personal series with code, version context, and trade-offs.
7. Zhihu, Juejin, WeChat, 博客园, Tencent Cloud Developer, Alibaba Cloud Developer, Volcengine Developer Community, and similar community articles.
8. Reposts, SEO pages, summaries without original evidence.

## Rules

- Prefer Chinese material when it does not weaken evidence quality.
- Use Chinese community articles for recall, explanations, and practice signals; do not let them override first-party docs, source, or papers.
- Treat vendor developer communities as public web sources unless the local source registry lists a gateway adapter. Rank each article by author identity: official/team posts can be Tier 3, ordinary community posts stay Tier 7.
- When checking whether something already exists, search GitHub, package registries, Hugging Face, papers, issues/discussions, and Chinese articles. One keyword search is insufficient.
- Do not convert absence of results into evidence of absence unless multiple independent source classes were searched and failures are reported.
- For time-sensitive platform/API claims, verify official docs or live behavior in the current turn.
