
import pandas as pd
from pathlib import Path

# ------------------------------------------
# 1. Set file locations
# ------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------
# 2. Load synthetic CSV files
# ------------------------------------------

customers = pd.read_csv(RAW_DIR / "customers.csv")
subscriptions = pd.read_csv(RAW_DIR / "subscriptions.csv")
billing = pd.read_csv(RAW_DIR / "billing.csv")

print("Original records:")
print(f"Customers: {len(customers)}")
print(f"Subscriptions: {len(subscriptions)}")
print(f"Billing: {len(billing)}")

# ------------------------------------------
# 3. Combine customer and subscription data
# ------------------------------------------

health = subscriptions.merge(
    customers,
    on="customer_id",
    how="left",
    validate="one_to_one"
)

# ------------------------------------------
# 4. Add billing information
# ------------------------------------------

health = health.merge(
    billing[["subscription_id", "payment_status"]],
    on="subscription_id",
    how="left",
    validate="one_to_one"
)

# ------------------------------------------
# 5. Create subscription health features
# ------------------------------------------

# Convert signup date to datetime
health["signup_date"] = pd.to_datetime(health["signup_date"])

# Use a fixed snapshot date for reproducibility
snapshot_date = pd.Timestamp("2026-10-25")

health["tenure_days"] = (
    snapshot_date - health["signup_date"]
).dt.days

# Historical cancellation indicator
health["canceled"] = (
    health["subscription_status"] == "Canceled"
).astype(int)

# Latest-payment failure indicator
health["payment_failed"] = (
    health["payment_status"] == "Failed"
).astype(int)

# ------------------------------------------
# 6. Select columns for the published dataset
# ------------------------------------------

# Exclude email and consent fields from analytics output
health = health[
    [
        "customer_id",
        "subscription_id",
        "plan",
        "subscription_status",
        "payment_status",
        "tenure_days",
        "canceled",
        "payment_failed"
    ]
]

# ------------------------------------------
# 7. Save final dataset
# ------------------------------------------

output_file = OUTPUT_DIR / "subscription_health.csv"

health.to_csv(output_file, index=False)

print("\nSubscription Health Dataset Created!")
print(f"Total records: {len(health)}")
print(f"Canceled subscriptions: {health['canceled'].sum()}")
print(f"Failed latest payments: {health['payment_failed'].sum()}")

print("\nPreview:")
print(health.head())

print(f"\nSaved to: {output_file}")
