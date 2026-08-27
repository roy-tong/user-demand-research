# Changelog

## 1.9.0 — 2026-08-27

- Added unnamed-experience research (命名前研究) for frontier products without settled vocabulary, with the grounding reference covering edge-language mining, substitute-behavior archaeology (E2 demand fossils), psychophysical dimension mapping, cross-domain literature anchors, and first-principles derivation.
- Added `sure.py plan --mode unnamed-experience`: copies lexicon and experience-space templates, adds Phase 0 grounding tasks, and records a 3–5× raw-to-clean intake estimate alongside the sample target.
- Added `sure.py lexicon`: per-term and per-grounding-path yield, acceptance-association proxy, demand-fossil count, zero-yield terms, and a stock-corpus sufficiency verdict (`--min-per-term`; exit 1 = insufficient, a collection instruction).
- Added the `lexicon_grounding` design gate: at least 5 retained terms across at least 2 grounding paths; experience-space.csv required when the psychophysical path is used.
- Evidence records gained optional `lexicon_terms` and `grounding_path` fields; the report gained a 命名前研究信号 section; MCP gained the `sure_lexicon` tool.

## 1.8.0 — 2026-08-27

- Added agent-discovery layer: repository `llms.txt` (stable raw index for agents) and `AGENTS.md` (working rules for coding agents inside the repo).
- Added `instructions` to the MCP initialize response so MCP clients receive the plan → check → collect → signals → report workflow, exit-code semantics, and hard boundaries without reading the repo first.
- Added an "Agent 接入速查" block at the top of the README with one-line capability framing and the four machine-readable entry points.
- Expanded the Skill description triggers (研究计划生成、调研报告、批量反馈挖掘).

## 1.7.0 — 2026-08-27

- Added `scripts/sure_mcp.py`: a standard-library-only MCP stdio server exposing `sure_plan`, `sure_init`, `sure_check`, `sure_signals`, `sure_report`, `sure_connectors`, and `sure_platform_map` as MCP tools for MCP-first clients (Claude Code, ZCode, Cursor, Cline, and similar).
- Tool results embed the CLI exit codes so agents can distinguish success, a failed gate (1), and no-feasible-platform (3) from usage errors (2).
- Documented the three integration paths (Skill for judgment, CLI for scripting, MCP for tool-native agents) with registration snippets for common clients.
- Added MCP protocol tests (initialize, tools/list, tools/call, invalid-params handling); 22 tests total.

## 1.6.0 — 2026-08-27

- Added `sure.py plan`: turns a research goal, region, sample size, and platform types into a study workspace with platform feasibility, sample quotas, scaled route targets, a feasibility report, and a collection task list; exits visibly when no requested platform has an enabled connector.
- Added `assets/platform-map.json` mapping regions (cn/overseas/global) and platform types to concrete platforms resolved against the connector registry.
- Added `sure.py signals`: deterministic corpus signals (level/role distributions, role × level matrix, source-family concentration, duplicate rate, time spread, chain readiness, gate deltas) written to `04-findings/signals.json`.
- Added `sure.py report`: assembles a Chinese research-status report into `06-report/report.md` from the study contract, source plan, manifests, signals, judgments, and blocked routes, keeping a visible failure banner until the full check passes.
- Added `06-report/` to the study template and documented the plan → collect → signals → report pipeline in the Skill, runbook, and README.

## 1.5.0 — 2026-08-27

- Replaced commercial research providers and seller/merchant APIs with a machine-readable registry of reviewed GitHub open-source connectors.
- Added separate code-license, platform-access, data-rights, and research-eligibility gates; a permissive repository license no longer implies a usable data route.
- Added supported official-API clients for Reddit (PRAW), X (Tweepy), and YouTube (Google API Python Client), plus a historical-only Amazon Reviews 2023 route.
- Preserved `snscrape`, `twikit`, unofficial YouTube downloaders, JD/Taobao scrapers, and KSInsights as blocked negative reviews with pinned commits and reasons.
- Added `sure.py connectors`, connector selection validation, run/connector provenance in platform evidence, and a standard collection-manifest contract.
- Recorded Reddit's 2026 public Data API transition: existing apps must register by 2026-09-30, new self-service access is closed, and the Devvit migration sets a `recheck_by` date on the PRAW entry.
- Added Amazon, JD, Taobao/Tmall, and Kickstarter route templates and audits; unsupported live routes now fail visibly instead of switching to a commercial or authenticated workaround.

## 1.3.0 — 2026-08-27

- Added the first platform-neutral social-media adapter layer with runbooks and route templates for Reddit, X, and YouTube.
- This release's broad tool-market survey was removed and superseded by the OSS-only connector registry in 1.5.0.
- Added optional CLI gates for Reddit subreddit/thread concentration, X conversation/day/repost concentration, and YouTube channel/video concentration, comment hierarchy, content status, and refresh deadlines.
- Added platform-specific access, policy-review, retention, original-source, and AI-summary controls to the starter study contract.
- Added repeatable `sure.py init --platform reddit|x|youtube` flags that enable adapters and copy editable route matrices into a new study.
- Documented that X reposts are E0 distribution signals, YouTube comment-thread responses may omit replies, and platform engagement metrics do not raise evidence levels.

## 1.2.0 — 2026-08-26

- Split the public material into a human learning path, an installable Agent Skill, and a deterministic local CLI while keeping one evidence model.
- Added `sure.py init` and stage-specific `design`, `evidence`, and `full` checks with JSON and Markdown audit reports.
- Added a standard study directory, machine-readable source plan, evidence index, codebook, demand judgments, and inter-Agent handoff contract.
- Replaced the translated “opportunity card” wording with demand judgments and explicit status/evidence gates.
- Expanded the synthetic sample into all five corpus roles with problem, solution, commercial/behavioral, and counter-evidence.
- Added tests for initialization, non-overwrite behavior, duplicate evidence, false validation, report generation, and the legacy validator wrapper.

## 1.1.0 — 2026-08-14

- Renamed the repository-facing product to `User Demand Research` and the canonical Skill to `user-demand-research`; SURE now expands clearly to Structured User Research with Evidence.
- Added a no-network synthetic sample study and deterministic validator for research contracts, evidence records, opportunity cards, and three-chain validation.
- Rebuilt the README around the task, first success, evidence gates, and explicit inference boundaries.
- Added CI tests for both a passing study and a false validation claim.

## 1.0.1 — 2026-08-12

- Separated untrusted source content from Agent control instructions.
- Added explicit prompt-injection handling for comments, transcripts, exports, and other third-party research data.

## 1.0.0 — 2026-08-12

- Published SURE in the standard `skills/scene-user-demand-research` layout for cross-agent discovery.
- Aligned the public README with the Skill's actual E0–E5 evidence model.
- Added direct `gh skill` and skills.sh installation paths, an Agent input/output contract, and privacy-safe measurement boundaries.
