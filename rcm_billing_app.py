import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, module_card_with_button

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(
    page_title="Hanvion Health – RCM Education Platform",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Sidebar Completely
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Inject Hanvion Blue Theme
with open("app/styles/hanvion_theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------
# NAVIGATION BAR
# -----------------------------------------------------------
show_navbar()

# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------
st.markdown("""
<div class="hanvion-header">
    <h1>Hanvion Health – Revenue Cycle Intelligence Platform</h1>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# INTRO SECTION
# -----------------------------------------------------------
st.write("""
Welcome to the **Hanvion RCM Education Platform** – an interactive, modern training
and analytics experience designed to help providers, payers, students, and healthcare
professionals understand the **entire revenue cycle** from eligibility to payment posting.

Use the modules below to explore:
- Revenue Cycle Education  
- Denial Prevention & Appeals  
- Prior Authorization  
- Payer Rules  
- CMS-based Analytics  
- Realistic RCM Simulators  
""")

st.write("---")

# -----------------------------------------------------------
# EDUCATIONAL MODULES
# -----------------------------------------------------------
st.subheader("📘 Educational Modules")

module_card_with_button(
    "RCM Overview",
    "Learn the end-to-end revenue cycle workflow, from scheduling to collections.",
    "Open Module",
    "pages/1_RCM_Overview.py",
)

module_card_with_button(
    "Coverage & Eligibility",
    "Understand insurance benefits, patient responsibility, and verification workflows.",
    "Open Module",
    "pages/2_Coverage_and_Eligibility.py",
)

module_card_with_button(
    "Prior Authorization",
    "Explore authorization requirements, workflows, and common denial causes.",
    "Open Module",
    "pages/3_Prior_Authorization.py",
)

module_card_with_button(
    "Claims Lifecycle",
    "Learn how claims move through creation, submission, adjudication, and payment.",
    "Open Module",
    "pages/4_Claims_Lifecycle.py",
)

module_card_with_button(
    "Denials Management",
    "Master denial categories, root causes, and successful appeal strategies.",
    "Open Module",
    "pages/5_Denials_Management.py",
)

module_card_with_button(
    "Out-of-Pocket Cost Education",
    "Understand copays, deductibles, coinsurance, and patient financial responsibility.",
    "Open Module",
    "pages/6_OOP_Cost_Education.py",
)

st.write("---")

# -----------------------------------------------------------
# ANALYTICS MODULES
# -----------------------------------------------------------
st.subheader("📊 Analytics & Dashboards")

module_card_with_button(
    "KPI Dashboard",
    "Track denial rate, clean claim rate, payer mix, and provider performance indicators.",
    "Open Dashboard",
    "pages/10_RCM_KPI_Dashboard.py",
)

module_card_with_button(
    "AR Aging Dashboard",
    "View AR buckets, collection probability, and payment lag distributions.",
    "Open Dashboard",
    "pages/11_AR_Aging_Dashboard.py",
)

module_card_with_button(
    "Provider Performance",
    "Analyze nationally benchmarked CMS provider performance using real datasets.",
    "Open Dashboard",
    "pages/13_Provider_Performance.py",
)

st.write("---")

# -----------------------------------------------------------
# SIMULATORS
# -----------------------------------------------------------
st.subheader("🧩 Interactive RCM Simulators")

module_card_with_button(
    "RCM Timeline Simulator",
    "Simulate a patient's full journey through the revenue cycle, step-by-step.",
    "Launch Simulator",
    "pages/7_RCM_Timeline_Simulator.py",
)

module_card_with_button(
    "Access Simulator",
    "Simulate eligibility checks, documentation completeness, and payer approval likelihood.",
    "Launch Simulator",
    "pages/8_RCM_Access_Simulator.py",
)

module_card_with_button(
    "PA Outcome Simulator",
    "Predict authorization outcomes based on payer rules and clinical documentation.",
    "Launch Simulator",
    "pages/14_PA_Outcome_Simulator.py",
)

module_card_with_button(
    "Claims Adjudication Simulator",
    "Simulate claim approvals, denials, appeal stages, and payment posting.",
    "Launch Simulator",
    "pages/15_Claims_Adjudication_Simulator.py",
)

st.write("---")

# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------
st.markdown("""
<div class="footer">
Hanvion Health © 2025 • Revenue Cycle Education & Intelligence Platform
</div>
""", unsafe_allow_html=True)
