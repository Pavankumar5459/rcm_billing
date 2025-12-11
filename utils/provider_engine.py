import pandas as pd

def provider_score(df):
    """
    Creates a composite score for provider efficiency.
    Medical groups use similar logic.
    """

    df = df.copy()

    df["efficiency"] = (
        (df.get("payment_amount", 0) / df.get("allowed_amount", 1)) * 0.6 +
        (df.get("line_count", 0) / (df.get("service_count", 1) + 1)) * 0.4
    )

    df["efficiency"] = df["efficiency"].clip(lower=0, upper=1)

    return df.sort_values("efficiency", ascending=False)


def provider_summary(df, n=10):
    """Return the top 10 providers by total payments."""
    if "payment_amount" not in df:
        return None

    grouped = (
        df.groupby("provider_type")["payment_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
    return grouped
