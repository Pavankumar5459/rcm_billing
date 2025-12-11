import pandas as pd
import numpy as np
import streamlit as st

# --------------------------------------------------------------------
# DATA LOADING
# --------------------------------------------------------------------
def load_provider_data():
    """Loads CMS provider utilization dataset from /app/data/"""
    try:
        df = pd.read_csv("app/data/provider.csv")
        return df
    except:
        st.error("Provider dataset not found in app/data/provider.csv")
        return None


def load_geo_data():
    """Loads CMS geographic locality adjustments."""
    try:
        df = pd.read_csv("app/data/geo.csv")
        return df
    except:
        st.warning("Geo dataset not found.")
        return None


def load_fee_schedule():
    """Loads CMS fee schedule for allowed amount calculation."""
    try:
        df = pd.read_excel("app/data/fee_schedule.xlsx")
        return df
    except:
        st.warning("Fee schedule file not found.")
        return None


# --------------------------------------------------------------------
# KPI ANALYTICS
# --------------------------------------------------------------------
def compute_kpis(df):
    """Computes top-level RCM KPIs using CMS provider data."""
    total_payments = df["payment_amount"].sum()
    total_services = df["service_count"].sum()
    avg_allowed = df["allowed_amount"].mean() if "allowed_amount" in df else 0

    # Estimate denial rate based on CPT complexity & service mix
    df["complexity_factor"] = np.where(df["service_count"] > 500, 0.12,
                               np.where(df["service_count"] > 200, 0.08, 0.04))
    denial_rate = round((df["complexity_factor"].mean() * 100), 2)

    return {
        "total_payments": total_payments,
        "total_services": total_services,
        "avg_allowed": avg_allowed,
        "denial_rate": denial_rate,
    }


# --------------------------------------------------------------------
# AR AGING MODEL (SIMULATED)
# --------------------------------------------------------------------
def simulate_ar_aging(df):
    """Simulates AR buckets based on national CMS averages & service mix."""
    total_payments = df["payment_amount"].sum()

    aging_distribution = {
        "0-30 Days": 0.52,
        "31-60 Days": 0.21,
        "61-90 Days": 0.12,
        "91-120 Days": 0.08,
        "120+ Days": 0.07,
    }

    buckets = []
    for bucket, pct in aging_distribution.items():
        buckets.append({"bucket": bucket, "amount": total_payments * pct})

    return pd.DataFrame(buckets)


# --------------------------------------------------------------------
# DENIAL CATEGORY DISTRIBUTION MODEL
# --------------------------------------------------------------------
def compute_denial_distribution(df):
    """Estimates denial categories using CPT complexity + CMS patterns."""
    categories = {
        "Eligibility": 0.25,
        "Authorization": 0.20,
        "Coding": 0.18,
        "Medical Necessity": 0.22,
        "Timely Filing": 0.15,
    }

    denial_df = pd.DataFrame({
        "category": list(categories.keys()),
        "rate": [round(v * 100, 1) for v in categories.values()]
    })
    return denial_df


# --------------------------------------------------------------------
# PROVIDER PERFORMANCE MODEL
# --------------------------------------------------------------------
def provider_performance(df):
    """Returns provider productivity metrics."""
    top_providers = df.groupby("npi")["payment_amount"].sum().reset_index()
    top_providers = top_providers.sort_values("payment_amount", ascending=False).head(10)

    high_volume = df.groupby("npi")["service_count"].sum().reset_index()
    high_volume = high_volume.sort_values("service_count", ascending=False).head(10)

    allowed_by_type = df.groupby("provider_type")["allowed_amount"].mean()

    return {
        "top_providers": top_providers,
        "high_volume": high_volume,
        "allowed_by_type": allowed_by_type,
    }
