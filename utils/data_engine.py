import streamlit as st
import pandas as pd
import numpy as np
import requests
import re

# ============================================================
#   GOOGLE DRIVE FOLDER AUTO-LOADER (STREAMLIT SAFE)
# ============================================================

@st.cache_data(show_spinner=True)
def list_drive_files(folder_id):
    """
    Lists all files in a Google Drive folder using the public folder view.
    Works WITHOUT Google API keys.
    """

    url = f"https://drive.google.com/embeddedfolderview?id={folder_id}#list"

    try:
        html = requests.get(url).text
    except Exception as e:
        st.error(f"Failed to read Google Drive folder: {e}")
        return []

    # File pattern extraction
    file_pattern = r"\/file\/d\/([a-zA-Z0-9_-]+)"
    file_ids = re.findall(file_pattern, html)

    files = list(set(file_ids))
    return files


def download_drive_file(file_id):
    """
    Downloads a file from Drive directly using the file ID.
    Works for CSV, Excel, and everything else.
    """

    url = f"https://drive.google.com/uc?id={file_id}&export=download"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        st.error(f"Failed downloading file {file_id}: {e}")
        return None


@st.cache_data(show_spinner=True)
def load_drive_csv(file_id):
    """Loads CSV file from Google Drive."""
    content = download_drive_file(file_id)
    if content is None:
        return None
    try:
        return pd.read_csv(pd.io.common.BytesIO(content), low_memory=False)
    except Exception as e:
        st.error(f"CSV parsing error: {e}")
        return None


@st.cache_data(show_spinner=True)
def load_drive_excel(file_id):
    """Loads Excel file from Google Drive."""
    content = download_drive_file(file_id)
    if content is None:
        return None
    try:
        return pd.read_excel(pd.io.common.BytesIO(content))
    except Exception as e:
        st.error(f"Excel parsing error: {e}")
        return None


# ============================================================
# AUTO DETECT CMS FILES
# ============================================================

def detect_cms_files(folder_id):
    """
    Detects CMS RY25 provider, geo, and POS files automatically
    using keyword pattern matching.
    """

    file_ids = list_drive_files(folder_id)
    provider_file = None
    geo_file = None
    pos_file = None

    for fid in file_ids:
        # Try downloading metadata to inspect filename
        meta_url = f"https://drive.google.com/file/d/{fid}/view"
        filename = meta_url  # used for pattern matching

        # Detect provider dataset
        if "prov" in filename.lower() or "provider" in filename.lower():
            provider_file = fid

        # Detect geography dataset
        if "geo" in filename.lower():
            geo_file = fid

        # Detect POS table
        if "pos" in filename.lower() or filename.lower().endswith(".xlsx"):
            pos_file = fid

    return provider_file, geo_file, pos_file


# ============================================================
#  MAIN LOADER FUNCTIONS
# ============================================================

def load_provider_data(folder_id):
    provider_file, _, _ = detect_cms_files(folder_id)

    if provider_file is None:
        st.error("Provider RY25 dataset not found in Drive folder.")
        return None

    df = load_drive_csv(provider_file)
    if df is None:
        return None

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

    # Clean numeric fields
    numeric_cols = ["submitted_charge", "allowed_amount", "payment_amount",
                    "line_count", "service_count"]

    for col in numeric_cols:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def load_geo_data(folder_id):
    _, geo_file, _ = detect_cms_files(folder_id)
    if geo_file is None:
        st.warning("Geo dataset not found in Drive folder.")
        return None
    return load_drive_csv(geo_file)


def load_pos_data(folder_id):
    _, _, pos_file = detect_cms_files(folder_id)
    if pos_file is None:
        st.warning("POS dataset not found in Drive folder.")
        return None
    return load_drive_excel(pos_file)
