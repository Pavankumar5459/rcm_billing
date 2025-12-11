import pandas as pd
import numpy as np
import streamlit as st

# Label for UI
RY_DEFAULT = "2025"


# -----------------------------
# File Loaders
# -----------------------------
def load_provider_data():
    """Load CMS Provider Utilization dataset for Reporting Year 2025."""
    try:
        df = pd.read_csv("app/data/provider_RY25.csv", low_memory=False)
        df = clean_provider_df(df)
        df = filter_latest_year(df)
        return df
    except Exception as e:
        st.error(f"Unable to load provider_RY25.csv: {e}")
        return None


def load_geo_data():
    """Load CMS Geographic dataset for RY25."""
    try:
        df = pd.read_csv("app/data/geo_RY25.csv", low_memory=False)
        return df
    except Exception as e:
        st.warning(f"Unable to load geo_RY25.csv: {e}")
        return None


def load_pos_data():
    """Load POS / fee schedule file for RY25."""
    try:
        df = pd.read_excel("app/data/pos_RY25.xlsx")
        return df
    except Exception as e:
        st.warning(f"Unable to load pos_RY25.xlsx: {e}")
        return None


# -----------------------------
# Data Cleaning
# -----------------------------
def clean_provider_df(df):
    """Standardize provider-level fields so analytics never break."""
    df.columns = df.columns.str.lower()

    rename_map = {
        "hcpcs_code": "cpt_code",
        "rndrng_prvdr_state_abrvtn": "provider_state",
        "rndrng_prvdr_type": "provider_type",
        "average_submitted_chrg_amt": "submitted_charge",
        "average_medicare_allowed_amt": "allowed_amount",
        "average_medicare_payment_amt": "payment_amount",
        "bene_day_srvc_cnt": "service_count",
        "line_srvc_cnt": "line_count",
        "mdcr_pymt_amt": "paid_amount"
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    # Numeric safety conversions
    num_cols = [
        "submitted_charge", "allowed_amount", "payment_amount",
        "service_count", "line_count", "paid_amount"
    ]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def filter_latest_year(df):
    """If dataset contains multiple years, keep the most recent."""
    year_cols = [c for c in df.columns if "year" in c.lower() or "yr" in c.lower()]

    if not year_cols:
        return df  # Already filtered or single-year dataset

    col = year_cols[0]
    latest_year = df[col].max()
    return df[df[col] == latest_year]


# -----------------------------
# KPI Computations
# -----------------------------
def compute_kpis(df):
    """Return a dictionary of KPIs for the dashboard."""

    kpis = {}

    kpis["total_claims"] = int(df["line_count"].sum()) if "line_count" in df else 0

    if "allowed_amount" in df:
        kpis["avg_allowed"] = round(df["allowed_amount"].mean(), 2)
    else:
        kpis["avg_allowed"] = None

    if "payment_amount" in df:
        kpis["fpr_rate"] = round(
            (df["payment_amount"] > 0).mean() * 100, 2
        )
    else:
        kpis["fpr_rate"] = None

    if "allowed_amount" in df and "payment_amount" in df:
        kpis["denial_rate"] = round(
            100 - ((df["payment_amount"] > 0).mean() * 100), 2
        )
    else:
        kpis["denial_rate"] = None

    kpis["service_volume"] = int(df["service_count"].sum()) if "service_count" in df else 0

    return kpis


# -----------------------------
# AR Aging (Synthetic from CMS distribution)
# -----------------------------
def compute_ar_aging(df):
    """CMS does not give AR aging directly, so we estimate using payment lag patterns."""
    if "payment_amount" not in df or "allowed_amount" not in df:
        return None

    ratio = df["payment_amount"] / df["allowed_amount"]
    ratio = ratio.replace([np.inf, -np.inf], np.nan).dropna()

    buckets = {
        "0–30 days": round((ratio > 0.90).mean() * 100, 2),
        "31–60 days": round((ratio.between(0.75, 0.90)).mean() * 100, 2),
        "61–90 days": round((ratio.between(0.50, 0.75)).mean() * 100, 2),
        "90–120 days": round((ratio.between(0.25, 0.50)).mean() * 100, 2),
        "120+ days": round((ratio < 0.25).mean() * 100, 2),
    }

    return buckets
