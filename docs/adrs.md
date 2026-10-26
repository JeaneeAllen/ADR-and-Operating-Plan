
# Aurora Nutrition — Architecture Decision Records

## ADR-001: Warehouse-Centric Storage

**Status:** Proposed  
**Door Type:** Difficult to reverse

### Context
Aurora Nutrition expects to grow from 40,000 to 250,000 subscribers. The company needs reliable subscription reporting and a consistent dataset for churn analysis.

### Options Considered
- Option A: Warehouse-centric storage for structured analytics.
- Option B: Lakehouse architecture supporting structured and unstructured data.

### Decision
Choose a warehouse-centric architecture for the initial Subscription Health product.

### Consequences
- Pros: Centralized reporting, simpler data management, and a manageable starting architecture.
- Cons: Less flexibility for future unstructured data workloads and possible migration costs.

### Human-Review Gate
The VP of Engineering must approve major storage migrations and changes affecting sensitive customer information.

### Evidence
- Own Testing: Our Python project successfully combines 100 synthetic customer, subscription, and billing records.
- Limitation: This test does not benchmark a warehouse or lakehouse.

### Reconsideration Trigger
Reevaluate if the proposed warehouse cannot meet the agreed freshness SLA for three consecutive reporting cycles.

---

## ADR-002: Orchestration and Agentic AI

**Status:** Proposed  
**Door Type:** Mostly reversible

### Context
As Aurora grows, the company will need dependable scheduling, monitoring, and recovery procedures. AI could assist developers, but production changes require oversight.

### Options Considered
- Option A: Managed orchestration with AI-assisted pull requests.
- Option B: Self-hosted orchestration with manually authored changes.

### Decision
Use managed orchestration and permit AI to draft code changes and open pull requests, subject to human approval.

### Consequences
- Pros: Less infrastructure management and potential development efficiency.
- Cons: Ongoing service costs, AI-generated code errors, and additional review responsibilities.

### Human-Review Gate
An authorized engineer must approve AI-generated changes before merging or deployment. Changes involving PII or customer identifiers require security review.

### Evidence
- Vendor Documentation (Vendor-Provided): GitHub documents required pull request reviews and status checks.
- Own Testing: Our local Python validator identified an invalid subscription status.
- Limitation: We have not tested AI-generated pull requests or a managed orchestration service.

### Reconsideration Trigger
Suspend AI-generated production changes following any confirmed critical incident caused by AI-authored code.

---

## ADR-003: Micro-Batch Subscription Processing

**Status:** Proposed  
**Door Type:** Reversible, with migration effort

### Context
Aurora needs timely subscription and billing information but has not established a requirement for immediate, real-time processing.

### Options Considered
- Option A: Continuous streaming as events occur.
- Option B: Micro-batch processing every five minutes.

### Decision
Choose five-minute micro-batch ingestion for the initial architecture.

### Consequences
- Pros: Simpler processing, scheduling, and recovery.
- Cons: Data arrives with a delay, which may affect time-sensitive decisions.

### Human-Review Gate
Engineering and the retention data owner must approve changes to the processing schedule or freshness SLA.

### Evidence
- Practitioner Framework Documentation: Apache Airflow explains scheduled workflows, task dependencies, and retries.
- Own Testing: Our Python project processed a small synthetic dataset.
- Limitation: We have not benchmarked streaming against micro-batching.

### Reconsideration Trigger
Reevaluate the decision if 95% of subscription events cannot become available within 10 minutes for three consecutive business days.

---

## ADR-004: Customer Transcript Vector Storage

**Status:** Proposed  
**Door Type:** Difficult to fully reverse after sensitive-data exposure

### Context
Aurora wants to improve customer experience through AI-powered retrieval. However, the company has not established that the benefits of storing customer transcripts in a vector database justify the additional privacy risks and costs.

### Options Considered
- Option A: Implement vector retrieval now with privacy controls.
- Option B: Defer implementation and use structured complaint categories.
- Option C: Avoid transcript-based vector retrieval entirely.

### Decision
Choose Option B. Defer production vector storage while preserving the option for future implementation.

### Consequences
- Pros: Reduced additional privacy exposure, infrastructure costs, and governance complexity.
- Cons: Delayed semantic search capabilities and potentially valuable AI-assisted customer insights.

### Human-Review Gate
The Security/Privacy Lead and VP of Engineering must approve transcript ingestion, embedding, retention policies, and production retrieval access before deployment.

### Evidence
- Practitioner Security Guidance: OWASP identifies unauthorized retrieval and information leakage as vector-related risks.
- Own Testing: Our synthetic transcript records are marked as not approved for retrieval.
- Limitation: We have not tested a vector database or measured its potential business value.

### Reconsideration Trigger
Reevaluate when Aurora reaches 5,000 customer-service interactions per month for three consecutive months.

The trigger initiates a review of business value, consent, privacy, and cost. It does not automatically approve implementation.


---

# Evidence Sources and Grading

## Source 1: GitHub Protected Branches
URL: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

Evidence Type: Vendor documentation (vendor-provided evidence)

Supports: Required human reviews and automated status checks.

Limitation: Documents available controls but does not prove AI-generated code is safe.

## Source 2: Apache Airflow DAG Documentation
URL: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html

Evidence Type: Project documentation (implementation guidance)

Supports: Scheduled tasks, dependencies, and workflow orchestration.

Limitation: Does not benchmark micro-batching against continuous streaming.

## Source 3: OWASP Vector and Embedding Weaknesses
URL: https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/

Evidence Type: Practitioner security guidance

Supports: Potential unauthorized retrieval and sensitive-data exposure in vector retrieval systems.

Limitation: Does not quantify Aurora Nutrition's specific risk.

## Source 4: Aurora Python Demonstration
Source: src/generate_data.py, src/transform.py,
src/validate.py, and validation screenshots

Evidence Type: Own Testing

Results:
- 100 synthetic Subscription Health records
- 14 canceled subscriptions
- 11 latest-payment failures
- Valid dataset passed all three governance checks
- Invalid subscription status triggered a validation failure
- Corrected dataset passed validation again

Limitation: This is a small local demonstration,
not a production-scale performance benchmark.

## Overall Evidence Assessment

The strongest evidence for our working prototype is
our own testing because the results were observed directly.

However, our testing does not prove that the proposed
production architecture will scale to 250,000 subscribers.

Vendor-provided documentation is weaker evidence
for claims about production performance and cost.

Before production approval, Aurora should conduct
representative workload testing and a privacy review.
