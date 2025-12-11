
import streamlit as st

st.set_page_config(page_title='Hanvion Health RCM Dashboard', layout='wide')
st.title('Hanvion Health – Revenue Cycle Intelligence Platform')

st.write('''
Welcome to the full RCM + Medicare Analytics Dashboard.
Use the sidebar to navigate across modules including:
- Coverage Engine
- Prior Authorization
- Denial Insights
- OOP Estimator
- Provider Utilization Explorer
- Geographic Reimbursement Explorer
''')
import os
import streamlit as st

st.title("Debug: Check Dataset Paths")

st.write("Current directory:", os.getcwd())

st.write("Listing files:")
st.write(os.listdir())

st.write("Listing sample_data folder:")
try:
    st.write(os.listdir("sample_data"))
except:
    st.error("sample_data folder NOT FOUND")

try:
    import pandas as pd
    df = pd.read_csv("sample_data/provider_sample.csv")
    st.success("provider_sample.csv LOADED SUCCESSFULLY!")
    st.write(df.head())
except Exception as e:
    st.error(f"Failed to load provider_sample.csv: {e}")

