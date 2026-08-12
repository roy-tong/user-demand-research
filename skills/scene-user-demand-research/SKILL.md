---
name: scene-user-demand-research
description: Run auditable user research and demand discovery with the SURE protocol. Use for user-demand research, customer discovery, voice-of-customer analysis, review or forum mining, Jobs-to-be-Done evidence, cross-platform feedback synthesis, anti-survivorship-bias sampling, evidence grading, opportunity validation, willingness-to-pay analysis, or auditing whether a dataset supports product decisions. Connects user roles, scenes, tasks, substitutes, frictions, consequences, and E0–E5 evidence. 中文触发：用户研究、需求研究、场景研究、评论挖掘、行业研究、证据分级、机会验证。
license: MIT
compatibility: Works with Agent Skills hosts. Internet access is required only when collecting public or user-authorized sources.
---

# Scene–User–Demand Research

Turn heterogeneous feedback into an auditable evidence chain. Treat collection volume as an input constraint, not as proof of demand.

## Choose the operating mode

- **Design**: create the research contract, scenario universe, sampling matrix, schema, and acceptance gates.
- **Execute**: implement or run collectors, normalization, deduplication, balanced views, labeling, and audit jobs.
- **Audit**: inspect an existing corpus and state exactly which claims it can and cannot support.
- **Synthesize**: produce opportunity theses, counter-evidence, validation queues, and product decisions from an audited corpus.

For an end-to-end study, read [references/research-protocol.md](references/research-protocol.md). When creating tables or collectors, also read [references/data-contract.md](references/data-contract.md). Copy and complete [assets/research-contract-template.md](assets/research-contract-template.md) at the start of a new study; use [assets/opportunity-card-template.md](assets/opportunity-card-template.md) for final synthesis.

## Apply the SURE model

Use this analysis key for every important observation:

`User role × Scene/trigger × Task/outcome × Current substitute × Friction/cost × Consequence × Evidence level`

Do not reduce “need” to a mentioned feature. Reconstruct the job, current behavior, and consequence before proposing a solution.

Grade the strongest evidence in each record:

- `E0` — activity or scene context only.
- `E1` — explicit unmet task, desired outcome, or pain.
- `E2` — substitute, workaround, failure, or switching cost.
- `E3` — explicit acceptance or preference for the studied solution.
- `E4+` — price anchor, purchase intent, or willingness to pay.
- `E4-` — rejection, cancellation, return, or abandonment.
- `E5` — paid ownership, deployment, retained use, repeat behavior, or expansion.

Require three linked chains before calling an opportunity validated: problem (`E1/E2`), solution acceptance (`E3`), and commercial/behavioral evidence (`E4/E5`). Allow strong `E0-E2` clusters to generate interview hypotheses, not product-demand claims.

## Follow the workflow

1. **Write a decision contract.** State the decision this research will change, target markets, time window, unit of observation, prohibited inferences, and stopping rules.
2. **Map the scene universe.** Combine product/category, ecosystem, task, substitute, rejector/churn, and event sampling frames. Keep user labels multi-valued.
3. **Design by evidence role.** Set quotas for direct solution feedback, open-scene discovery, substitute/rejector evidence, post-purchase/support evidence, and a mainstream/control stratum. Do not mistake many platforms from one source family for diversity.
4. **Freeze the data contract.** Preserve full text, source URL, source time, collection route, sampling frame, known bias flags, privacy-safe author hash, record ID, and normalized-text hash before scaling collection.
5. **Pilot first.** Probe reachability, date precision, content completeness, duplicate rate, relevance yield, platform restrictions, and critical-stratum yield. Change the sampling plan when a channel is low-yield or blocked; never silently replace a missing evidence role with easy volume.
6. **Collect lawfully and reproducibly.** Use public pages, permitted APIs, research datasets, or user-authorized exports. Respect access controls and stop at login walls, CAPTCHAs, 403/429 responses, robots restrictions, or explicit platform challenges unless a compliant user-authorized route exists.
7. **Keep data layers separate.** Preserve raw normalized records, a strict deduplicated master, balanced analysis views, labels, and audits as distinct artifacts. Never overwrite the full corpus with a capped analysis sample.
8. **Discover before fixing the taxonomy.** Extract open-vocabulary candidates from unique threads and rank by cross-source and cross-time persistence. Review examples before promoting a term or segment into the codebook.
9. **Code and calibrate.** Apply rules or LLM labels only as discovery aids. Build a stratified human gold set for critical fields, double-code a subset, and revise the codebook until agreement is acceptable.
10. **Audit before inference.** Check volume after filtering, source-family concentration, time continuity, event spikes, evidence-role coverage, rejector coverage, language/market context, duplicate leakage, missing fields, and claim eligibility.
11. **Synthesize with counter-evidence.** For each opportunity, show supporting records, negative cases, satisfactory substitutes, confidence, gaps, and the next cheapest falsification test.

## Enforce claim discipline

- Call rows **feedback records**, **observations**, or **evidence records** unless unique people were actually resolved with a lawful method.
- Treat platform, interface language, query locale, and search region as sampling context—not verified residence.
- Treat design weights and capped views as balance mechanisms—not population weights.
- Report raw, strict-primary, and balanced-view counts separately.
- Do not infer prevalence, market share, or demand percentages from convenience samples.
- Do not let likes, rankings, repeated replies, or launch-week bursts create a segment by themselves.
- Do not describe open-scene data as preference for the proposed product.
- Do not rank opportunities using frequency alone; combine severity, frequency, workaround cost, consequence, evidence strength, cross-source consistency, persistence, and strategic fit.
- Include explicit limitations and failed/blocked source routes in every formal deliverable.

## Produce the minimum artifact set

For full studies, create:

1. research contract and question map;
2. source/evidence-role matrix with quotas and access status;
3. raw normalized JSONL plus collection manifests;
4. strict master dataset and balanced analysis view;
5. schema and codebook;
6. machine-readable and human-readable quality audits;
7. evidence ledger with representative records and counterexamples;
8. opportunity cards and a prioritized validation backlog;
9. limitations, data gaps, and prohibited-inference statement.

When the evidence gates fail, deliver a research-status report and remediation plan instead of a confident market conclusion.
