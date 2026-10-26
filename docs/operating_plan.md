
# Aurora Nutrition — Cost-Aware Operating Plan

## 1. Purpose

This plan estimates the monthly cost of operating
Aurora Nutrition's Subscription Health data product
at its projected size of 250,000 subscribers.

The estimates are hypothetical planning assumptions,
not actual vendor quotes or production expenses.

## 2. Operating Assumptions

| Assumption | Value |
|---|---:|
| Current subscribers | 40,000 |
| Projected subscribers | 250,000 |
| Subscription/billing events per subscriber per day | 2 |
| Days per month | 30 |
| Estimated monthly events | 15,000,000 |
| Ingestion frequency | Every 5 minutes |
| Estimated analytical storage | 500 GB |
| Production vector retrieval | Deferred |

Monthly event calculation:

250,000 subscribers × 2 events × 30 days
= 15,000,000 events per month.

These volumes are modeling assumptions and do
not represent measured Aurora activity.

## 3. Estimated Monthly Infrastructure Costs

| Cost Category | Monthly Estimate |
|---|---:|
| Data storage (500 GB × $0.025) | $12.50 |
| Compute ($20 per day × 30 days) | $600.00 |
| Orchestration and monitoring | $200.00 |
| Security, logging, and backups | $120.00 |
| Production vector retrieval | $0.00 |
| **Total Estimated Monthly Cost** | **$932.50** |

Estimated cost per subscriber:

$932.50 / 250,000 = $0.00373 per subscriber/month.

All costs are illustrative assumptions, not
verified provider pricing.

These estimates exclude employee labor,
one-time implementation, ML model serving,
and other company-wide technology expenses.

## 4. Cost-Control Strategies

### Micro-Batch Processing
Process subscription events every five minutes
instead of maintaining an unnecessarily complex
streaming architecture.

### Incremental Processing
Process new or changed records rather than
rebuilding the full historical dataset.

### Data Partitioning
Organize large datasets by date to reduce
unnecessary data scanning.

### Retention Management
Archive or delete records according to
approved retention schedules.

### Deferred Vector Storage
Avoid additional embedding, vector indexing,
and AI retrieval expenses until Aurora
demonstrates a business need.

## 5. KPIs and Service Expectations

Business KPIs:
- Subscription cancellation trends
- Retention rate
- Retention campaign effectiveness

Pipeline Health Metrics:
- Pipeline success rate
- Data freshness
- Validation failures
- Duplicate records

Proposed SLA:
Subscription reporting data available by
7:00 a.m. local time on at least 99% of
business days.

Escalation:
Data Engineering investigates missed SLA
targets and notifies the data product owner.

The owner communicates material reporting
delays to affected consumers.

## 6. Scaling Considerations

The 100-customer Python demonstration proves
basic transformation and validation behavior.

It does not establish performance at
250,000 subscribers.

Before scaling to production, Aurora should:

- Test realistic subscription event volumes.
- Measure processing latency and compute costs.
- Confirm warehouse capacity.
- Validate recovery and backfill procedures.
- Review privacy and access controls.
- Reevaluate costs using actual provider pricing.

## 7. Operating Recommendation

Aurora should begin with a manageable,
warehouse-centric architecture supported by
micro-batch processing and automated data
quality checks.

Human approval should remain required for
sensitive infrastructure and AI-generated changes.

Production customer-transcript vector storage
should remain deferred until business demand
and appropriate governance controls justify it.

## 8. Evidence Classification

Evidence Type: Own Testing
- The local Python demonstration processed
  100 synthetic subscriptions.
- Validation passed on valid records.
- An invalid subscription status caused
  the governance validator to fail.

Evidence Type: Planning Assumptions
- Subscriber event volumes
- Storage requirements
- Compute expenses
- Monthly operating costs

Limitation:
The cost model is illustrative and has
not been validated against actual cloud
provider prices or production workloads.
