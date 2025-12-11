
import streamlit as st
import pandas as pd

def load_provider(sample=True, upload=None):
    if upload is not None:
        return pd.read_csv(upload)
    if sample:
        return pd.read_csv("sample_data/provider_sample.csv")
    return None

def load_geo(sample=True, upload=None):
    if upload is not None:
        return pd.read_csv(upload)
    if sample:
        return pd.read_csv("sample_data/geo_sample.csv")
    return None
