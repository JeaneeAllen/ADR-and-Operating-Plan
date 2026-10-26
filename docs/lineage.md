
# Aurora Nutrition — Data Lineage

## Data Sources

The project uses synthetic data generated in Python.

| Source | Records | Purpose |
|---|---:|---|
| customers.csv | 100 | Customer identifiers, signup dates, and consent |
| subscriptions.csv | 100 | Subscription plans and statuses |
| billing.csv | 100 | Simulated payment information |
| transcripts.csv | 30 | Fictional customer-service interactions |

## Data Flow

customers.csv
       |
       v
subscriptions.csv
       |
       v
billing.csv
       |
       v
Python Transformation (transform.py)
       |
       v
subscription_health.csv
       |
       v
Python Governance Checks (validate.py)
       |
       v
Retention Reporting / ML Feature Consumer

## Transformation Logic

1. Load the customer, subscription, and billing records.
2. Join the datasets using customer_id and subscription_id.
3. Calculate subscription tenure.
4. Create cancellation and latest-payment failure indicators.
5. Exclude customer email addresses from the published dataset.
6. Save the Subscription Health dataset.
7. Run governance validation checks.

## Governance Rules

- Subscription IDs must be unique.
- Subscription statuses must be valid.
- Prohibited PII columns must not appear in the published dataset.

## Validation Evidence

- Initial valid dataset: PASS
- Deliberately invalid subscription status: FAIL
- Corrected dataset: PASS

Evidence Type: Own Testing

## Limitations

- All records are synthetic.
- The sample includes 100 customers, not Aurora's projected 250,000 subscribers.
- The cancellation indicator is not a monthly churn rate or a trained churn prediction.
- The billing dataset has one simulated payment record per subscription.
- The current local validator checks the output after transformation; it does not yet block publication.
- Customer-service transcripts are not loaded into a vector database.
