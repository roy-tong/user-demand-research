# Changelog

## 0.3.0 — 2026-08-13

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
