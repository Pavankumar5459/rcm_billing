import streamlit as st

st.title("❌ Denial Resolver")

denial = st.selectbox("Select Denial Type:", [
    "Missing ICD-10",
    "Insufficient Medical Necessity",
    "No Prior Authorization",
    "Incorrect Site of Care",
    "Non-Covered Service"
])

if denial == "Missing ICD-10":
    st.write("→ Add correct ICD-10 & resubmit.")
elif denial == "Insufficient Medical Necessity":
    st.write("→ Attach detailed provider notes & labs.")
elif denial == "No Prior Authorization":
    st.write("→ Submit PA retroactively if allowed.")
elif denial == "Incorrect Site of Care":
    st.write("→ Verify SOC eligibility with payer.")
else:
    st.write("→ Review coverage policy, submit appeal.")
