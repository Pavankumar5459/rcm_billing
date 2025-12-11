import streamlit as st

st.title("💵 Out-of-Pocket Cost Estimator")

allowed = st.number_input("Allowed Amount ($)", min_value=0)
ded = st.number_input("Annual Deductible ($)", min_value=0)
ded_met = st.number_input("Deductible Already Met ($)", min_value=0)
coins = st.slider("Coinsurance (%)", 0, 100, 20)
copay = st.number_input("Visit Copay ($)", min_value=0)

remaining_ded = max(ded - ded_met, 0)
coins_amount = (allowed - remaining_ded) * (coins / 100)

oop = remaining_ded + coins_amount + copay

st.subheader(f"Estimated OOP Cost: **${oop:,.2f}**")
