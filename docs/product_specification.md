
# Aurora Nutrition — Subscription Health Data Product

## 1. Product Overview

Product Name: Subscription Health
Status: Proposed
Product Owner: Lead Analytics Engineer

Purpose:
Provide reliable subscription and billing information
for churn monitoring, retention reporting, and future
machine learning applications.

Aurora Nutrition expects to grow from 40,000 to
250,000 subscribers over the next fiscal year.

## 2. Ownership and Consumers

| Role | Responsibility |
|---|---|
| Lead Analytics Engineer | Owns the data product and its quality |
| Data Engineering Team | Maintains pipelines and resolves failures |
| Customer Retention Team | Monitors cancellations and payment issues |
| ML Engineering Team | Uses documented features for churn modeling |
| Customer Support AI Team | Future consumer of approved transcript retrieval |
| Security/Privacy Lead | Reviews access, consent, and privacy controls |

Support Expectations:
- Data Engineering investigates pipeline failures.
- Product owner coordinates incident resolution.
- Consumers are notified of breaking changes.
- Sensitive-data changes require security review.

## 3. Data Sources

| Dataset | Records | Purpose |
|---|---:|---|
| customers.csv | 100 | Customer and signup information |
| subscriptions.csv | 100 | Subscription details |
| billing.csv | 100 | Payment information |
| transcripts.csv | 30 | Fictional customer-service records |

All datasets were generated synthetically in Python.

## 4. Interface Contract

Published Dataset:
data/processed/subscription_health.csv

| Column | Type | Description |
|---|---|---|
| customer_id | String | Unique fictional customer identifier |
| subscription_id | String | Unique subscription identifier |
| plan | String | Basic, Standard, or Premium |
| subscription_status | String | Active, Paused, or Canceled |
| payment_status | String | Latest simulated payment status |
| tenure_days | Integer | Days since signup |
| canceled | Integer | Historical cancellation indicator, 0 or 1 |
| payment_failed | Integer | Latest-payment failure indicator, 0 or 1 |

Contract Requirements:
- Subscription IDs must be unique and non-null.
- Subscription statuses must use approved values.
- Published data must exclude raw customer emails.
- Schema changes require review and documentation.
- Breaking changes require versioning and consumer notification.

Proposed Freshness SLA:
Subscription reporting data available by 7:00 a.m.
local time on at least 99% of business days.

The SLA is a production target, not a measured result
from the current Python demonstration.

## 5. Policy-as-Code Governance

The local Python validator implements three rules.

Rule 1: Unique subscription identifiers

    assert df["subscription_id"].is_unique

Rule 2: Approved subscription statuses

    allowed = ["Active", "Paused", "Canceled"]
    assert df["subscription_status"].isin(allowed).all()

Rule 3: Prohibited PII columns

    prohibited = ["email", "phone", "address", "ssn"]
    assert not any(col in df.columns for col in prohibited)

These rules are implemented in src/validate.py.

Validation Evidence:
- Initial valid dataset: PASS
- Invalid status introduced: FAIL
- Corrected dataset: PASS

The validator currently runs locally after the output
file is created. Production deployment would require
validation before publication.

## 6. MLOps Handoff Checklist

Before the ML team uses this data product:

- [ ] Confirm feature names and definitions.
- [ ] Confirm data types and allowed values.
- [ ] Define churn prediction window and target label.
- [ ] Prevent future information from leaking into training.
- [ ] Use consistent transformations for training and prediction.
- [ ] Document feature owners and data sources.
- [ ] Define model performance monitoring.
- [ ] Establish measurable retraining triggers.
- [ ] Review privacy and access permissions.
- [ ] Document model limitations.

Current Limitation:
The project creates basic features but does not train
or deploy a churn prediction model.

## 7. LLMOps / RAGOps Operating Plan

ADR-004 defers production transcript vector storage.

The following is a proposed future operating plan,
not a deployed RAG system.

Chunking:
Split approved, redacted customer-service transcripts
by conversation turn or topic while preserving
necessary context.

Refresh Cadence:
Perform daily incremental updates after consent and
privacy checks.

Retrieval Evaluation:
Use a test set of customer questions paired with
expected relevant transcript sources.

Retrieval Quality:
Evaluate recall@5 and relevance using a labeled
evaluation dataset.

Drift Monitoring:
Monitor changes in complaint categories, customer
language, and retrieval performance.

Retention and Deletion:
Apply approved retention schedules and ensure
deletions propagate to source records, embeddings,
vector indexes, and associated metadata.

Access Controls:
Restrict retrieval based on authorized user roles.
Do not expose unapproved customer information.

Human-Review Gate:
Security/Privacy and Engineering approval is required
before any production transcript embedding or retrieval.

Reconsideration Trigger:
Review ADR-004 if Aurora reaches 5,000 customer-service
interactions per month for three consecutive months.

Reaching this threshold does not automatically approve
vector database implementation.

## 8. KPIs and SLAs

Business KPIs:
- Subscription cancellation trends
- Retention campaign effectiveness
- Customer retention rate

Pipeline Health Metrics:
- Validation pass rate
- Pipeline success rate
- Data freshness
- Duplicate subscription count

Proposed SLA:
Subscription data available by 7:00 a.m. local time
on at least 99% of business days.

Proposed Quality Target:
Zero known critical validation failures in
published subscription data.

These are proposed operating targets, not
performance results established by the prototype.

## 9. Product Limitations

- All customer records are synthetic.
- The sample contains 100 subscriptions.
- No production warehouse or orchestration is deployed.
- No real-time ingestion is implemented.
- No churn model has been trained.
- No vector database has been deployed.
- The dataset contains one billing record per subscription.
- The canceled indicator is not a monthly churn rate.
- Production-scale reliability has not been tested.

## 10. AI-Assisted Development Disclosure

ChatGPT assisted with project planning, documentation,
architecture explanations, and Python code development.

The Python scripts were executed locally, and
validation results were reviewed during development.

All records are synthetic. No real Aurora Nutrition
customer information was used.
