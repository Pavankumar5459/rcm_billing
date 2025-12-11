import streamlit as st
import pandas as pd
import numpy as np
import os
import glob

# Folder where CMS RY25 files live
DATA_FOLDER = "cms_data"

# -------------------------------
# AUTO-DETECTION HELPERS
# -------------------------------

def find_file(pattern):
    """Return first file that matches the pattern in cms_data."""
    files = glob.glob(os.path.join(DATA_FOLDER, pattern), recursive=True)
    if files:
        return files[0]
    return None


def load_csv(pattern):
    """Loads CSV using CMS auto filename detection."""
    file = find_file(pattern)
    if not file:
        st.warning(f"Missing file for pattern: {pattern}")
        return None
    try:
        df = pd.read_csv(file, low_memory=False)
        return df
    except Exception as e:
        st.error(f"Error reading {file}: {e}")
        return None


def load_excel(pattern):
    """Loads Excel file using CMS naming patterns."""
    file = find_file(pattern)
    if not file:
        st.warning(f"Missing file for pattern: {pattern}")
        return None
    try:
        return pd.read_excel(file)
    except Exception as e:
        st.error(f"Error reading {file}: {e}")
        return None


# -------------------------------
# MAIN DATA LOADERS (RY25)
# -------------------------------

def load_provider_data():
    """
    Auto-detect CMS Provider RY25 file.
    Example filenames:
    - MUP_PHY_R25_P05_V20_D23_Prov.csv
    """
    df = load_csv("*Prov*.csv")
    if df is None:
        return None
    df = clean_provider_df(df)
    df = filter_latest_year(df)
    return df


def load_geo_data():
    """Auto-detect CMS Geography or Service-level geo file."""
    df = load_csv("*Geo*.csv")
    return df


def load_pos_data():
    """Auto-detect POS Excel (fee schedule, place of service)."""
    df = load_excel("*POS*.xlsx")
    return df


# -------------------------------
# CLEANING & STANDARDIZATION
# -------------------------------

def clean_provider_df(df):
    """Normalize CMS provider dataset for analytics & dashboards."""
    df.columns = df.columns.str.lower()

    rename_map = {
        "rndrng_prvdr_type": "provider_type",
        "rndrng_prvdr_state_abrvtn": "provider_state",
        "hcpcs_code": "cpt_code",
        "bene_day_srvc_cnt": "service_count",
        "line_srvc_cnt": "line_count",
        "average_submitted_chrg_amt": "submitted_charge",
        "average_medicare_allowed_amt": "allowed_amount",
        "average_medicare_payment_amt": "payment_amount",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    numeric_cols = [
        "submitted_charge", "allowed_amount", "payment_amount",
        "service_count", "line_count"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def filter_latest_year(df):
    """If CMS dataset contains multiple years, keep the most recent."""
    year_cols = [c for c in df.columns if "yr" in c or "year" in c]

    if not year_cols:
        return df  # assume RY25-only file

    col = year_cols[0]
    max_year = df[col].max()
    return df[df[col] == max_year]


# -------------------------------
# KPI METRICS
# -------------------------------

def compute_kpis(df):
    """Compute KPI metrics for dashboard."""
    kpis = {}
    kpis['total_claims'] = int(df["line_count"].sum()) if "line_count" in df else 0

    if "allowed_amount" in df:
        kpis["avg_allowed"] = round(df["allowed_amount"].mean(), 2)
    else:
        kpis["avg_allowed"] = None

    if "payment_amount" in df:
        kpis["fpr_rate"] = round(
            (df["payment_amount"] > 0).mean() * 100, 2
        )
        kpis["denial_rate"] = round(
            100 - kpis["fpr_rate"], 2
        )
    else:
        kpis["fpr_rate"] = None
        kpis["denial_rate"] = None

    kpis["service_volume"] = int(df["service_count"].sum()) if "service_count" in df else 0

    return kpis


# -------------------------------
# AR AGING ESTIMATION
# -------------------------------

def compute_ar_aging(df):
    """Estimate AR aging buckets based on Medicare payment ratios."""
    if "payment_amount" not in df or "allowed_amount" not in df:
        return None

    ratio = df["payment_amount"] / df["allowed_amount"]
    ratio = ratio.replace([np.inf, -np.inf], np.nan).dropna()

    return {
        "0–30 days": round((ratio > 0.90).mean() * 100, 2),
        "31–60 days": round((ratio.between(0.75, 0.90)).mean() * 100, 2),
        "61–90 days": round((ratio.between(0.50, 0.75)).mean() * 100, 2),
        "90–120 days": round((ratio.between(0.25, 0.50)).mean() * 100, 2),
        "120+ days": round((ratio < 0.25).mean() * 100, 2),
    }
