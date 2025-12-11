import pandas as pd
import numpy as np

# --------------------------------------------------
# Compute KPIs from provider dataset
# --------------------------------------------------

def compute_claim_volume(df):
    """Return total service/claim count."""
    if "line_count" in df:
        return int(df["line_count"].sum())
    if "service_count" in df:
        return int(df["service_count"].sum())
    return 0


def compute_avg_allowed(df):
    """Average Medicare allowed amount."""
    if "allowed_amount" not in df:
        return None
    return round(df["allowed_amount"].mean(), 2)


def compute_payment_rate(df):
    """First-pass payment rate (FPR)."""
    if "payment_amount" not in df:
        return None
    return round((df["payment_amount"] > 0).mean() * 100, 2)


def compute_denial_rate(df):
    """Denial rate = 100 - FPR."""
    pr = compute_payment_rate(df)
    if pr is None:
        return None
    return round(100 - pr, 2)


def compute_top_states(df, n=10):
    """Return top N states by claim volume."""
    if "provider_state" not in df:
        return None
    return (
        df.groupby("provider_state")["line_count"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def compute_top_services(df, n=10):
    """Return top CPT/HCPCS codes by volume."""
    if "cpt_code" not in df:
        return None
    return (
        df.groupby("cpt_code")["line_count"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def compute_geo_summary(df):
    """Summaries for geography dataset."""
    if df is None or df.empty:
        return None

    cols = [c for c in df.columns if "bene" in c.lower() or "srv" in c.lower()]
    return df[cols].sum().to_dict()


def compute_allowed_vs_paid(df):
    """Difference between allowed and actual Medicare payment."""
    if "allowed_amount" not in df or "payment_amount" not in df:
        return None
    diff = df["allowed_amount"].sum() - df["payment_amount"].sum()
    return round(diff, 2)
