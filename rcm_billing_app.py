import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Hanvion Health – RCM Education Platform",
    layout="wide",
)

# Custom CSS
css_path = Path("styles/hanvion_theme.css")
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div style="background: linear-gradient(90deg, #0EA5E9, #2563EB); 
            padding: 36px; border-radius: 12px; margin-bottom: 30px;">
    <h1 style="color:white; margin:0;">Hanvion Health – Revenue Cycle Management Education Platform</h1>
    <p style="color:white; font-size:18px; margin:4px 0 0;">
        Learn the healthcare revenue cycle through structured educational modules 
        and explore Medicare provider and geographic analytics.
    </p>
</div>
""", unsafe_allow_html=True)

# Two CTA Buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Start Learning RCM"):
        st.switch_page("pages/1_RCM_Overview.py")

with col2:
    if st.button("Explore Medicare Analytics"):
        st.switch_page("pages/9_Medicare_Provider_Analytics.py")

st.write("")
st.markdown("---")
st.write("")

# Section Title: Education
st.subheader("Revenue Cycle Education Modules")

education_cards = [
    ("Revenue Cycle Overview", "1_RCM_Overview.py",
     "Understand the full lifecycle of patient encounters, billing, and reimbursement."),
    ("Coverage & Eligibility", "2_Coverage_and_Eligibility.py",
     "Learn insurance verification, coverage rules, documentation standards, and eligibility checks."),
    ("Prior Authorization", "3_Prior_Authorization.py",
     "Explore authorization workflows, common denial causes, required clinical documentation, and optimization strategies."),
    ("Claims Submission Lifecycle", "4_Claims_Lifecycle.py",
     "Understand CMS-1500 fields, claim routing, clearinghouses, adjudication, and remittance."),
    ("Coding Basics (ICD-10, CPT, HCPCS)", "5_Coding_Basics.py",
     "Learn diagnostic and procedural coding essentials used in reimbursement."),
    ("Denials & Prevention", "6_Denials_Management.py",
     "Review denial categories, root causes, appeals, and process improvements."),
    ("Out-of-Pocket Cost Education", "7_OOP_Cost_Education.py",
     "Learn deductibles, copays, coinsurance, and real-world billing scenarios."),
    ("RCM Timeline Simulator", "8_RCM_Timeline_Simulator.py",
     "Step-by-step simulation of a claim from scheduling to payment resolution."),
]

# Display education cards
edu_cols = st.columns(2)
for idx, (title, page, desc) in enumerate(education_cards):
    with edu_cols[idx % 2]:
        st.markdown(f"""
            <div style="border:1px solid #E5E7EB; padding:18px; 
                        border-radius:12px; margin-bottom:18px; background:#FFFFFF;">
                <h3 style="margin-bottom:6px;">{title}</h3>
                <p style="color:#475569; font-size:15px; margin-bottom:8px;">{desc}</p>
                <a href="pages/{page}" target="_self">
                    <button style="padding:8px 15px; border-radius:6px; 
                                   background:#2563EB; color:white; border:none;">
                        Open Module
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Medicare Analytics")

analytics_cards = [
    ("Provider Utilization Analytics", "9_Medicare_Provider_Analytics.py",
     "Analyze Medicare provider-level spending, HCPCS utilization, and reimbursement patterns."),
    ("Geographic Reimbursement Explorer", "10_Medicare_Geographic_Analytics.py",
     "Explore state-level variation in Medicare allowed amounts and beneficiary distribution."),
]

# Display analytics cards
an_cols = st.columns(2)
for idx, (title, page, desc) in enumerate(analytics_cards):
    with an_cols[idx % 2]:
        st.markdown(f"""
            <div style="border:1px solid #E5E7EB; padding:18px; 
                        border-radius:12px; margin-bottom:18px; background:#FFFFFF;">
                <h3 style="margin-bottom:6px;">{title}</h3>
                <p style="color:#475569; font-size:15px; margin-bottom:8px;">{desc}</p>
                <a href="pages/{page}" target="_self">
                    <button style="padding:8px 15px; border-radius:6px; 
                                   background:#2563EB; color:white; border:none;">
                        Open Analytics
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
