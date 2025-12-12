import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Hanvion Health – RCM Billing Dashboard",
    layout="wide"
)

st.title("Hanvion Health – Revenue Cycle Management (RCM) Dashboard")
st.caption("Demo data for claims, payments, and denials")

st.markdown("""
This dashboard visualizes demo claims data including charges, payments,
denials, and payer mix. In a production system, these would be loaded
from your billing system or data warehouse.
""")

# ---------------- SAMPLE DEMO DATA ----------------

def load_demo_claims():
    data = [
        {
            "claim_id": "C1001",
            "patient": "John Doe",
            "payer": "BlueCross",
            "dos": "2025-01-05",
            "charge_amount": 250.0,
            "paid_amount": 200.0,
            "status": "Paid",
            "denial_reason": "",
            "cpt_code": "99213",
            "icd10_codes": "I10",
            "days_to_payment": 15,
        },
        {
            "claim_id": "C1002",
            "patient": "Mary Smith",
            "payer": "Aetna",
            "dos": "2025-01-06",
            "charge_amount": 400.0,
            "paid_amount": 0.0,
            "status": "Denied",
            "denial_reason": "Medical necessity not documented",
            "cpt_code": "93000",
            "icd10_codes": "R07.9",
            "days_to_payment": None,
        },
        {
            "claim_id": "C1003",
            "patient": "Ali Khan",
            "payer": "Medicare",
            "dos": "2025-01-10",
            "charge_amount": 600.0,
            "paid_amount": 480.0,
            "status": "Paid",
            "denial_reason": "",
            "cpt_code": "99214",
            "icd10_codes": "E11.9",
            "days_to_payment": 21,
        },
        {
            "claim_id": "C1004",
            "patient": "Ravi Patel",
            "payer": "BlueCross",
            "dos": "2025-01-11",
            "charge_amount": 300.0,
            "paid_amount": 0.0,
            "status": "Pending",
            "denial_reason": "",
            "cpt_code": "71046",
            "icd10_codes": "J18.9",
            "days_to_payment": None,
        },
        {
            "claim_id": "C1005",
            "patient": "Sarah Lee",
            "payer": "Medicaid",
            "dos": "2025-01-12",
            "charge_amount": 180.0,
            "paid_amount": 150.0,
            "status": "Paid",
            "denial_reason": "",
            "cpt_code": "99213",
            "icd10_codes": "F41.1",
            "days_to_payment": 18,
        },
    ]
    df = pd.DataFrame(data)
    df["dos"] = pd.to_datetime(df["dos"])
    return df

df = load_demo_claims()

# ---------------- FILTERS ----------------

st.sidebar.header("Filters")

min_date = df["dos"].min().date()
max_date = df["dos"].max().date()

date_range = st.sidebar.date_input(
    "Date of Service Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

selected_payers = st.sidebar.multiselect(
    "Payers",
    options=sorted(df["payer"].unique().tolist()),
    default=sorted(df["payer"].unique().tolist())
)

selected_status = st.sidebar.multiselect(
    "Claim Status",
    options=sorted(df["status"].unique().tolist()),
    default=sorted(df["status"].unique().tolist())
)

# Apply filters
start_date, end_date = date_range
mask = (
    (df["dos"].dt.date >= start_date)
    & (df["dos"].dt.date <= end_date)
    & (df["payer"].isin(selected_payers))
    & (df["status"].isin(selected_status))
)

filtered = df[mask].copy()

# ---------------- KPI METRICS ----------------

total_charges = filtered["charge_amount"].sum()
total_payments = filtered["paid_amount"].sum()
denied_claims = filtered[filtered["status"] == "Denied"]
denial_rate = (len(denied_claims) / len(filtered) * 100) if len(filtered) > 0 else 0.0
collection_rate = (total_payments / total_charges * 100) if total_charges > 0 else 0.0

paid_claims_with_days = filtered[filtered["days_to_payment"].notna()]
avg_days_to_payment = (
    paid_claims_with_days["days_to_payment"].mean()
    if not paid_claims_with_days.empty
    else None
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Charges", f"${total_charges:,.2f}")
c2.metric("Total Payments", f"${total_payments:,.2f}")
c3.metric("Collection Rate", f"{collection_rate:,.1f}%")
c4.metric("Denial Rate", f"{denial_rate:,.1f}%")

if avg_days_to_payment is not None:
    st.caption(f"Average Days to Payment (for paid claims): {avg_days_to_payment:.1f}")
else:
    st.caption("Average Days to Payment: Not enough paid claim data.")

# ---------------- TABLES & BREAKDOWNS ----------------

st.markdown("### Claim Details")
st.dataframe(filtered, use_container_width=True)

st.markdown("### Payer Mix (by Charges)")
payer_group = filtered.groupby("payer")["charge_amount"].sum().reset_index()
if not payer_group.empty:
    st.bar_chart(payer_group.set_index("payer"))
else:
    st.info("No data for selected filters.")

st.markdown("### Denial Reasons")
if not denied_claims.empty:
    denial_counts = denied_claims["denial_reason"].value_counts().reset_index()
    denial_counts.columns = ["Denial Reason", "Count"]
    st.table(denial_counts)
else:
    st.info("No denied claims in current filter.")

# ---------------- NEW CLAIM SIMULATOR ----------------

st.markdown("---")
st.subheader("New Claim – Denial Risk (Demo)")

col_a, col_b = st.columns(2)
with col_a:
    new_payer = st.selectbox("Payer", ["BlueCross", "Aetna", "Medicare", "Medicaid", "Other"])
    new_cpt = st.text_input("CPT Code", value="99213")
    new_icd = st.text_input("Primary ICD-10", value="I10")
    new_charge = st.number_input("Charge Amount ($)", min_value=0.0, value=200.0)

with col_b:
    notes = st.text_area("Clinical / Documentation Notes (free text)", height=80)
    prior_auth = st.checkbox("Prior Authorization Obtained?")
    medical_necessity_doc = st.checkbox("Medical Necessity Clearly Documented?")
    correct_demographics = st.checkbox("Accurate Demographics & Insurance Stored?")

def estimate_denial_risk(payer, prior_auth, med_nec, demo_ok, notes):
    """
    Simple rule-based denial risk estimator.
    """
    score = 0

    if payer in ["Medicaid", "Medicare"]:
        score += 1

    if not prior_auth:
        score += 1

    if not med_nec:
        score += 2

    if not demo_ok:
        score += 1

    notes_lower = notes.lower()
    if "unclear" in notes_lower or "missing" in notes_lower:
        score += 1

    if score <= 1:
        return "Low", score
    elif score <= 3:
        return "Moderate", score
    else:
        return "High", score

if st.button("Estimate Denial Risk"):
    risk_level, risk_score = estimate_denial_risk(
        new_payer, prior_auth, medical_necessity_doc, correct_demographics, notes
    )
    st.write(f"**Denial Risk Level:** {risk_level} (score {risk_score})")

    if risk_level == "Low":
        st.success("Low risk of denial based on the provided information (demo only).")
    elif risk_level == "Moderate":
        st.warning("Moderate risk of denial. Consider strengthening documentation and verifying requirements.")
    else:
        st.error("High risk of denial. Documentation, prior auth, or coding may need review.")

    st.caption("This denial risk is a demo-only heuristic and not a guarantee of payment or denial.")
    import streamlit as st

# -----------------------------
# RCM AT A GLANCE
# -----------------------------
st.subheader("📊 Revenue Cycle Management — At a Glance")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**What**")
    st.write("End-to-end process managing healthcare revenue from patient registration to final payment.")

with col2:
    st.markdown("**Why**")
    st.write("Ensures financial stability, reduces revenue leakage, and improves patient billing experience.")

with col3:
    st.markdown("**Who**")
    st.write("Providers, payers, billing teams, coders, and patients.")

st.divider()

# -----------------------------
# RCM LIFECYCLE (EXPANDABLE)
# -----------------------------
st.subheader("🔄 Revenue Cycle Management Lifecycle")

with st.expander("View RCM Lifecycle Steps"):
    st.markdown("""
    **1️⃣ Patient Scheduling & Registration**  
    Capture accurate patient demographics and insurance details.

    **2️⃣ Insurance Eligibility & Authorization**  
    Verify coverage and obtain prior authorizations before services.

    **3️⃣ Clinical Documentation**  
    Providers document diagnoses and procedures during care delivery.

    **4️⃣ Medical Coding (ICD-10, CPT, HCPCS)**  
    Translate clinical documentation into standardized medical codes.

    **5️⃣ Claim Submission**  
    Submit clean claims to payers for reimbursement.

    **6️⃣ Payer Adjudication**  
    Payers review claims and determine payment responsibility.

    **7️⃣ Denial Management**  
    Identify, correct, and resubmit denied or underpaid claims.

    **8️⃣ Payment Posting**  
    Record payments from insurance and patients.

    **9️⃣ Patient Billing & Collections**  
    Generate patient statements and manage outstanding balances.
    """)

st.divider()

# -----------------------------
# WHY RCM MATTERS
# -----------------------------
st.subheader("🏥 Why Revenue Cycle Management Matters")

st.markdown("""
- Reduces claim denials and payment delays  
- Improves cash flow and financial predictability  
- Prevents revenue leakage  
- Enhances patient trust through transparent billing  
- Supports regulatory compliance and audit readiness  
""")

st.divider()

# -----------------------------
# KEY RCM METRICS (DEMO KPIs)
# -----------------------------
st.subheader("📈 Key RCM Performance Indicators")

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric("Days in A/R", "42 days")
kpi2.metric("Clean Claim Rate", "94%")
kpi3.metric("Denial Rate", "6%")

kpi4, kpi5, kpi6 = st.columns(3)

kpi4.metric("First-Pass Resolution", "88%")
kpi5.metric("Net Collection Rate", "97%")
kpi6.metric("Patient Responsibility %", "18%")

st.caption("⚠️ Metrics shown are demo values for educational purposes only.")

st.divider()

# -----------------------------
# PATIENT EXPERIENCE SECTION
# -----------------------------
st.subheader("👤 RCM & Patient Experience")

st.markdown("""
Modern Revenue Cycle Management focuses on **patient-centered billing** by:
- Providing cost estimates before care  
- Reducing billing surprises  
- Offering transparent statements  
- Enabling flexible payment options  
""")

st.divider()

# -----------------------------
# CAREER PATHWAYS IN RCM
# -----------------------------
st.subheader("💼 Careers in Revenue Cycle Management")

st.markdown("""
- Revenue Cycle Analyst  
- Medical Coder / Auditor  
- Billing & AR Specialist  
- Denial Management Analyst  
- Revenue Integrity Analyst  
- Healthcare Data Analyst  
""")

st.divider()

# -----------------------------
# FUTURE ENHANCEMENTS
# -----------------------------
st.subheader("🚀 Future Enhancements")

st.markdown("""
- Real-time insurance eligibility simulation (270/271)  
- AI-assisted denial prediction  
- Cost-of-care estimation for patients  
- Specialty-specific RCM dashboards  
- Integration with EHR and claims datasets  
""")

st.divider()

# -----------------------------
# REFERENCES
# -----------------------------
st.subheader("📚 References")

st.markdown("""
- Tulane University School of Public Health – Revenue Cycle Management in Healthcare  
- athenahealth – What is Healthcare Revenue Cycle Management?
""")

