
# Aurora Nutrition — Security, Privacy, and Compliance Matrix

## Purpose

This matrix identifies privacy and security requirements
for the Subscription Health data product and explains
how Aurora would enforce and verify those requirements.

| Requirement | Technical Control | Verification | Responsible Team |
|---|---|---|---|
| PII Protection | Exclude raw customer emails and other prohibited PII from published analytics tables. | Automated schema validation | Data Engineering |
| Customer Consent | Record customer consent and require appropriate authorization before transcript retrieval. | Consent checks before ingestion | Privacy / Security |
| Data Retention | Apply an approved retention schedule and delete expired records. | Scheduled retention audits | Data Engineering / Privacy |
| Access Controls | Restrict sensitive customer records based on job responsibilities. | Role-based access reviews | Security |
| Data Quality | Require unique subscription IDs and valid status values. | Automated Python validation | Data Engineering |
| AI Human Oversight | Require human approval before AI-generated changes reach production. | Pull request approval records | Engineering |
| Transcript Privacy | Do not publish transcripts to a production vector database until formally approved. | Ingestion configuration review | Security / Engineering |
| Auditability | Maintain logs of pipeline runs, validation results, and approvals. | Audit log reviews | Engineering |

## Regulatory Considerations

Aurora Nutrition is a direct-to-consumer supplements
company, so HIPAA should not automatically be assumed
to apply.

Applicable privacy and consumer-protection requirements
must be determined based on the data collected, customer
locations, intended uses, and business activities.

Aurora should also review relevant federal and state
privacy laws and customer consent agreements before
using transcripts for AI-powered retrieval.

## Retention Policy Assumption

For this proposed architecture, Aurora will use a
24-month analytical data retention period.

This is a planning assumption, not a verified legal
requirement. The final schedule must be reviewed and
approved based on applicable obligations and business
needs.

Customer deletion requests must also be addressed
according to applicable requirements.

## Current Implementation vs. Future Controls

Implemented in the Python demonstration:
- Unique subscription ID validation
- Approved subscription status validation
- Prohibited PII column-name validation

Proposed for production:
- Enforced role-based access
- Automated consent verification
- Scheduled retention enforcement
- Human approval gates
- Audit logging
- Vector retrieval security controls

## Evidence

Evidence Type: Own Testing

The Python validator successfully detected an invalid
subscription status and passed after the issue was
corrected.

Limitation: The demonstration validates selected data
quality and schema rules. It does not establish full
regulatory compliance.
