
import pandas as pd
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "subscription_health.csv"

# Load published dataset
df = pd.read_csv(DATA_FILE)

errors = []

print("\nAURORA NUTRITION — DATA GOVERNANCE CHECKS")
print("-" * 45)

# Rule 1: Subscription IDs must be unique
if df["subscription_id"].is_unique:
    print("PASS: Subscription IDs are unique")
else:
    errors.append("Duplicate subscription IDs found")
    print("FAIL: Duplicate subscription IDs found")

# Rule 2: Subscription status must be valid
valid_statuses = ["Active", "Paused", "Canceled"]

if df["subscription_status"].isin(valid_statuses).all():
    print("PASS: Subscription statuses are valid")
else:
    errors.append("Invalid subscription status found")
    print("FAIL: Invalid subscription status found")

# Rule 3: Customer email must not appear in the output
pii_columns = ["email", "phone", "address", "ssn"]

found_pii = [col for col in pii_columns if col in df.columns]

if not found_pii:
    print("PASS: No prohibited PII columns found")
else:
    errors.append(f"PII columns detected: {found_pii}")
    print(f"FAIL: PII columns detected: {found_pii}")

# Final validation
print("-" * 45)

if errors:
    print(f"VALIDATION FAILED: {len(errors)} rule(s) violated")
    sys.exit(1)
else:
    print("VALIDATION PASSED: All governance checks passed")
    sys.exit(0)
