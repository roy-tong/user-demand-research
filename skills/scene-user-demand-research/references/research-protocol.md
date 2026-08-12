# Research protocol

## Contents

1. Research contract
2. SURE unit of analysis
3. Scenario-universe construction
4. Sampling by evidence role
5. Collection and data layers
6. Discovery and coding
7. Evidence and opportunity scoring
8. Human validation
9. Stopping rules
10. Failure modes

## 1. Research contract

Define the decision before defining the crawler. Complete these fields:

- decision to change;
- hypotheses to test and what would falsify each one;
- studied solution boundary and adjacent categories;
- target markets and language strata;
- source-time and collection-time windows;
- observation unit;
- outputs and users of the research;
- minimum evidence roles and quality gates;
- claims that are out of scope;
- collection stop and restart rules.

Use a question map with five layers:

1. **Activity**: what is the person trying to do, in what environment and trigger?
2. **Current behavior**: what product, workflow, person, or non-consumption substitutes today?
3. **Cost and consequence**: what time, money, cognitive load, risk, discomfort, rework, or lost outcome follows?
4. **Solution response**: does the person accept, reject, modify, or ignore the proposed solution?
5. **Commercial behavior**: who decides, pays, deploys, retains, returns, renews, or expands?

## 2. SURE unit of analysis

Represent a high-value record as:

`role → trigger/scene → task/outcome → substitute → friction → consequence → solution response → commercial behavior`

Keep roles non-exclusive. In business contexts, separate end user, influencer, purchaser, IT/security reviewer, budget owner, and beneficiary. In consumer contexts, distinguish buyer, owner, active user, lapsed user, returner, and bystander.

Do not force every row to contain every field. Preserve missingness and use it to design the next sampling or interview round.

## 3. Scenario-universe construction

Use six sampling frames together:

1. **Product/category frame**: direct reviews, communities, launches, competitors, and category language.
2. **Ecosystem frame**: software, workflows, repositories, professions, and activity communities where the task occurs without mentioning the product.
3. **Task/scene frame**: moments of creation, understanding, checking, deciding, collaborating, fixing, buying, or abandoning.
4. **Substitute frame**: incumbent products, manual workflows, outsourcing, “good enough” tools, and non-consumption.
5. **Rejector/churn frame**: trial failure, returns, refunds, cancellation, non-adoption, maintenance burden, and people satisfied with alternatives.
6. **Event frame**: releases, price changes, controversies, outages, policy shifts, seasonal demand, and competitor launches. Mark event windows separately.

Build the first scene universe from domain knowledge, adjacent-category research, and open-vocabulary discovery. Treat it as a versioned hypothesis map, not a closed taxonomy.

## 4. Sampling by evidence role

Design quotas around what a record can prove:

| Evidence role | Typical source | What it can support | Common bias |
| --- | --- | --- | --- |
| Direct solution feedback | Product community, launch comments, category reviews | Feature response, acceptance, failure | Owner/enthusiast self-selection |
| Open-scene discovery | Task communities, professional forums, activity channels | Jobs, triggers, substitutes, consequences | Cannot prove solution preference |
| Substitute/rejector | Competitor users, cancellation/return threads, non-user communities | Reasons not to switch, adequate alternatives | Hard to find with product keywords |
| Post-purchase/support | Ecommerce reviews, issues, tickets, support forums | Reliability, integration, maintenance, return | Overweights failures or active owners |
| Mainstream/control | Adjacent mainstream users and non-adopters | Base behavior and non-consumption | Lower direct relevance |

Stratify within roles by source family, platform, time, language/market context, scene, stance, and user state. Define caps for dominant strata. Quotas are a research design, not estimates of real market composition.

Run a pilot before fixing targets. Estimate:

- valid full-text yield;
- strict-primary yield after date/relevance/quality filters;
- duplicates by record ID and normalized text;
- number of unique threads/products;
- critical evidence yield (`E3-E5`, rejectors, post-purchase, enterprise deployment);
- month and source-family concentration;
- access and compliance risk;
- marginal new-theme yield.

## 5. Collection and data layers

Store these layers separately:

1. **Landing/raw normalized**: append-only records from each route, including collection metadata.
2. **Strict master**: valid window, full text, deduplicated, quality/relevance checked, provenance retained.
3. **Balanced analysis views**: capped or weighted by month, platform, source family, scene, or evidence role.
4. **Coded view**: rules/LLM/human labels plus model and codebook versions.
5. **Gold set**: stratified human-coded sample for calibration.
6. **Evidence ledger**: representative positive, negative, contradictory, and edge records used in claims.

Make collectors resumable and idempotent. Save route-level state, request/page manifests, timestamps, error status, and known sampling bias. Prefer reproducible chronological or community frames over ranking pages when possible.

## 6. Discovery and coding

Preserve full feedback before extraction. Use this order:

1. normalize minimally;
2. deduplicate;
3. create strict master;
4. extract open candidates;
5. review candidate examples and counterexamples;
6. version the codebook;
7. rule/LLM code;
8. human calibration;
9. re-code and audit.

Rank open candidates using unique thread/product support, platform/source-family diversity, time persistence, and scene specificity. Avoid raw comment frequency because a single viral thread or argument can dominate it.

Core coding fields should cover role, scene, task, trigger, desired outcome, substitute, friction, consequence, frequency, severity, solution response, price/purchase evidence, user state, collaboration, integration, safety/privacy/compliance, and confidence.

## 7. Evidence and opportunity scoring

Assign the strongest directly observed level:

| Level | Meaning | Permitted claim |
| --- | --- | --- |
| E0 | Scene/activity context | “This activity exists in the corpus.” |
| E1 | Unmet task/pain/outcome | “A problem or desired outcome is expressed.” |
| E2 | Substitute/workaround/failure | “Current behavior and its friction are observed.” |
| E3 | Solution acceptance/preference | “The proposed solution is accepted by this evidence.” |
| E4+ | Price or purchase intent | “Stated commercial intent/anchor exists.” |
| E4- | Rejection/return/abandonment | “Direct negative commercial evidence exists.” |
| E5 | Paid use/deployment/retention/expansion | “Observed behavior supports realized demand.” |

Do not collapse the levels into one undifferentiated count.

Create an opportunity thesis only when the following can be filled with evidence:

> For [role], when [trigger/scene], achieving [outcome] is difficult because [substitute + friction], causing [consequence]. [Solution] is accepted under [conditions], with [commercial evidence] and [counter-evidence].

Score opportunities on separate dimensions rather than hiding judgment in one number:

- task frequency;
- severity/consequence;
- workaround cost;
- evidence strength;
- cross-source consistency;
- time persistence;
- addressability by the product;
- strategic fit;
- negative evidence and substitute adequacy;
- confidence/coverage quality.

Show both the dimension scores and the rationale. If a composite is necessary, publish the weights and sensitivity-check alternative weights.

## 8. Human validation

Build a gold set stratified across source family, month, evidence role, scene, stance, and high/low-confidence records. Double-code critical fields on a subset. Use Cohen’s kappa for two coders or Krippendorff’s alpha for broader settings; target at least 0.70 for decision-critical labels, then inspect class-specific precision/recall because aggregate agreement can hide rare-class failure.

Use LLM coding only on privacy-safe records. Record model, prompt, version/date, temperature or deterministic setting, codebook version, confidence, and adjudication result. Recalibrate after source-mix shifts.

Validate high-priority opportunities with interviews, workflow observation, concept tests, usability tests, price tests, or authorized business data. Large public corpora discover and rank hypotheses; they do not remove the need for direct validation.

## 9. Stopping rules

Stop expansion when all apply:

- strict-primary quality gates pass;
- no critical evidence role or time/language stratum remains empty;
- source-family dominance is within declared limits or explicitly bounded;
- marginal new-theme yield has plateaued across multiple independent strata;
- gold-set accuracy is adequate for decision-critical labels;
- the next decision can be made with stated confidence;
- collection cost exceeds the expected value of reducing the remaining uncertainty.

Restart when a product release, new market, new language, source-mix change, codebook revision, or failed gate materially changes claim eligibility.

## 10. Failure modes

- **Counting rows as people**: report records and, separately, estimated unique authors/threads if lawful and reliable.
- **Twenty thousand or two hundred thousand rows from one source**: treat as scale without representativeness.
- **Keyword-only discovery**: add ecosystem, task, substitute, and rejector frames.
- **Owners only**: add non-buyers, returners, lapsed users, and satisfied substitute users.
- **Recent launch spike**: separate event study from baseline and use balanced time views.
- **Frequency equals priority**: incorporate consequence, workaround, evidence level, and counter-evidence.
- **Open-scene text equals product demand**: keep corpus roles and evidence eligibility explicit.
- **Automatic labels become facts**: retain full text, confidence, versions, and gold-set performance.
- **Missing source silently filled by easy data**: preserve the gap and redesign the route for the same evidence role.
- **Blocked access bypassed**: stop and use a permitted API, user-authorized export, public research dataset, or another source.
