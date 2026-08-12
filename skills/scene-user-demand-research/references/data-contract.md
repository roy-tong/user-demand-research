# Canonical data contract

Use JSONL for full records and CSV/Parquet only as analysis projections. Preserve full text in the master JSONL.

## Provenance and identity

| Field | Type | Purpose |
| --- | --- | --- |
| `record_id` | string | Stable source-prefixed identifier. |
| `source_platform` | string | Named platform/site. |
| `source_family` | string | Forum, social, ecommerce, support, Q&A, video comments, etc. |
| `source_channel` | string/null | Community, product, repository, board, channel, or listing. |
| `source_url` | string/null | Traceable public or authorized source. |
| `parent_id` / `thread_id` | string/null | Prevent one long thread from masquerading as broad support. |
| `source_query` | string/null | Query or route that selected the record. |
| `sampling_frame` | string | Product, ecosystem, task, substitute, rejector, event, chronological, export, etc. |
| `sampling_bias_flags` | array | Ranking, logged-out, owner community, active-thread, search, highlighted-review, or other known limitations. |
| `created_at` | ISO string/null | Source time. |
| `date_precision` | string | Exact, day, month, year, approximate, unknown. |
| `collected_at` | ISO string | Collection time. |
| `author_hash` | string/null | Salted hash if needed for dedup; avoid raw identifiers by default. |

## Content and quality

| Field | Type | Purpose |
| --- | --- | --- |
| `text` | string | Complete feedback text; do not truncate the master. |
| `language` | string/null | Detected or source-provided language. |
| `market_sampling_context` | string/null | Query locale/platform market, not verified residence. |
| `rating` / `score` / `reply_count` | number/null | Source metadata; do not use as demand by itself. |
| `quality_score` | number | Versioned and explainable screening score. |
| `quality_flags` | array | Deleted, duplicate, too short, spam, off-topic, approximate date, etc. |
| `normalized_text_hash` | string | Cross-source exact/near dedup key. |
| `primary_sample_eligible` | boolean | Meets declared date, access, content, quality, and relevance rules. |

## Research design

| Field | Type | Purpose |
| --- | --- | --- |
| `corpus_role` | string | Direct solution, open scene, substitute/rejector, post-purchase/support, control. |
| `month_bucket` | YYYY-MM/null | Time stratum. |
| `scene_labels` | array | Multi-valued activity context. |
| `user_role_labels` | array | Multi-valued role/state. |
| `task_labels` | array | Desired job or outcome. |
| `substitute_labels` | array | Current solution, workaround, or non-consumption. |
| `friction_labels` | array | Time, cost, cognition, comfort, integration, maintenance, risk, etc. |
| `consequence_labels` | array | Rework, loss, error, delay, abandonment, safety, or missed outcome. |
| `solution_response` | string/null | Accept, reject, conditional, neutral, unknown. |
| `demand_evidence_level` | string | `E0`, `E1`, `E2`, `E3`, `E4+`, `E4-`, or `E5`. |
| `evidence_basis` | string | Short explanation or matched rule for the assigned level. |
| `analysis_weight` | number/null | Design weight only. |
| `analysis_weight_basis` | string/null | Exact balancing rule; explicitly not a population weight. |

## Coding provenance

| Field | Type | Purpose |
| --- | --- | --- |
| `codebook_version` | string | Version of definitions used. |
| `coding_method` | string | Rule, LLM, human, or adjudicated. |
| `coder_or_model_version` | string/null | Reproducibility. |
| `coding_confidence` | number/null | Supports review queues, not truth claims. |
| `human_review_status` | string | Unreviewed, sampled, agreed, adjudicated, rejected. |

## Required derived views

Generate without mutating the strict master:

- counts by raw/strict/balanced layer;
- records and unique threads/products by source family and platform;
- monthly/quarterly/half-year distributions;
- evidence-role and evidence-level distributions;
- rejector/returner and paid/deployed coverage;
- scene × role × task × substitute × evidence pivots;
- missingness and approximate-date rates;
- duplicate and near-duplicate removals;
- blocked/failed collection routes;
- high-confidence claim-eligible subsets.

## Audit assertions

Parameterize thresholds in a study config. Test at least:

- strict record count after all filters;
- continuous or explicitly justified time coverage;
- maximum share for one month/event window;
- maximum share for one source family/platform/channel/thread;
- minimum independent source families;
- minimum open-scene, substitute/rejector, and post-purchase/support coverage;
- exact and normalized-text duplicate leakage;
- full-text, source URL, timestamp, and corpus-role completeness;
- language/market-stratum coverage;
- approximate-date cap;
- gold-set agreement and rare-label performance;
- representative positive and negative examples for every published claim.
