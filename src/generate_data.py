
import pandas as pd
import numpy as np
from pathlib import Path

# Make results reproducible
rng = np.random.default_rng(42)

# Locate the project folder
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Set the number of fictional customers
NUM_CUSTOMERS = 100

# -------------------------------------------------
# 1. Generate customer records
# -------------------------------------------------

customers = pd.DataFrame({
    "customer_id": [f"C{i:05d}" for i in range(1, NUM_CUSTOMERS + 1)],
    "email": [f"customer{i}@example.com" for i in range(1, NUM_CUSTOMERS + 1)],
    "signup_date": (
        pd.Timestamp("2025-01-01")
        + pd.to_timedelta(rng.integers(0, 600, NUM_CUSTOMERS), unit="D")
    ),
    "consent_flag": rng.choice(
        [True, False],
        size=NUM_CUSTOMERS,
        p=[0.85, 0.15]
    )
})

# -------------------------------------------------
# 2. Generate subscription records
# -------------------------------------------------

subscriptions = pd.DataFrame({
    "subscription_id": [f"S{i:05d}" for i in range(1, NUM_CUSTOMERS + 1)],
    "customer_id": customers["customer_id"],
    "plan": rng.choice(
        ["Basic", "Standard", "Premium"],
        size=NUM_CUSTOMERS
    ),
    "subscription_status": rng.choice(
        ["Active", "Paused", "Canceled"],
        size=NUM_CUSTOMERS,
        p=[0.75, 0.10, 0.15]
    ),
    "start_date": customers["signup_date"]
})

# -------------------------------------------------
# 3. Generate billing records
# -------------------------------------------------

billing = pd.DataFrame({
    "payment_id": [f"P{i:05d}" for i in range(1, NUM_CUSTOMERS + 1)],
    "subscription_id": subscriptions["subscription_id"],
    "amount": rng.choice(
        [19.99, 39.99, 59.99],
        size=NUM_CUSTOMERS
    ),
    "payment_status": rng.choice(
        ["Paid", "Failed"],
        size=NUM_CUSTOMERS,
        p=[0.90, 0.10]
    )
})

# -------------------------------------------------
# 4. Generate fictional support transcripts
# -------------------------------------------------

categories = [
    "Billing Issue",
    "Delivery Delay",
    "Product Question",
    "Cancellation Request"
]

sample_messages = {
    "Billing Issue": "I have a question about my recent charge.",
    "Delivery Delay": "My supplement order has not arrived yet.",
    "Product Question": "Can you explain the difference between the plans?",
    "Cancellation Request": "I would like to cancel my subscription."
}

transcript_count = 30

transcript_categories = rng.choice(
    categories,
    size=transcript_count
)

transcripts = pd.DataFrame({
    "transcript_id": [f"T{i:05d}" for i in range(1, transcript_count + 1)],
    "customer_id": rng.choice(
        customers["customer_id"].to_numpy(),
        size=transcript_count
    ),
    "category": transcript_categories,
    "transcript_text": [
        sample_messages[category] for category in transcript_categories
    ]
})

# Explicitly do not authorize any transcripts for vector retrieval
transcripts["retrieval_approved"] = False

# -------------------------------------------------
# 5. Save datasets
# -------------------------------------------------

datasets = {
    "customers": customers,
    "subscriptions": subscriptions,
    "billing": billing,
    "transcripts": transcripts
}

for name, df in datasets.items():
    file_path = RAW_DIR / f"{name}.csv"
    df.to_csv(file_path, index=False)
    print(f"Saved {name}.csv: {len(df):,} rows")

print("\nSynthetic data generation complete!")
