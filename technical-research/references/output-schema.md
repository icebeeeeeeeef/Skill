# Gateway Output Schema

The `cn-article-search` gateway returns JSON. Treat it as evidence metadata, not final truth.

## Tools

```python
search_articles(
    query: str,
    sources: list[str] | None = None,
    time_range: str | None = None,
    limit: int = 20,
    require_full_text: bool = False,
) -> SearchResponse
```

```python
fetch_article(url: str, force_refresh: bool = False) -> ArticleResponse
```

```python
source_health() -> HealthResponse
```

## Result Fields

Important fields:

- `title`, `url`, `source`, `resource_type`
- `author`, `account`, `published_at`, `updated_at`
- `snippet`
- `content_markdown`
- `discovery_method`
- `fetch_method`
- `auth_level`
- `discovery_status`
- `fetch_status`
- `evidence_level`
- `quality_signals`
- `content_hash`
- `fetched_at`

## Status Rules

- `snippet` is not article text.
- `content_markdown: null` means full text was not fetched.
- `fetch_status: full_text` means a parser/browser/cache returned article body.
- `fetch_status: metadata_only` means only search metadata is available.
- `fetch_status: blocked` means the source refused or challenged the fetch.
- Check `source_status` before judging coverage.

Expected statuses include:

```text
success
partial
metadata_only
cache_hit
empty
login_required
reauth_required
captcha_required
sms_verification_required
token_required
rate_limited
blocked
content_truncated
redirect_resolution_failed
source_unavailable
fetch_failed
```
