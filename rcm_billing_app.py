import streamlit as st
from utils.navigation import show_navbar

# Load the global top navigation bar
show_navbar()

# Page configuration
st.set_page_config(
    page_title="Hanvion Health – RCM Education Platform",
    layout="wide",
)

# Title Section
st.title("Hanvion Health – RCM Education Platform")
st.write("Interactive training modules explaining the full patient access and reimbursement pathway.")

st.markdown("---")

# -------- MODULE DEFINITIONS (DO NOT CHANGE FILENAMES) -------- #
modules = [
    ("RCM Overview", "1_RCM_Overview.py", "Learn the end-to-end revenue cycle workflow."),
    ("Coverage & Eligibility", "2_Coverage_and_Eligibility.py", "Understand benefit checks and patient responsibility."),
    ("Prior Authorization", "3_Prior_Authorization.py", "Learn authorization workflows and payer requirements."),
    ("Claims Lifecycle", "4_Claims_Lifecycle.py", "Understand how claims are created, submitted, and adjudicated."),
    ("Denials Management", "5_Denials_Management.py", "Learn denial categories, root causes, and appeals."),
    ("Out-of-Pocket Cost Education", "6_OOP_Cost_Education.py", "Explain deductibles, coinsurance, and patient liability."),
    ("RCM Timeline Simulator", "7_RCM_Timeline_Simulator.py", "Simulate a step-by-step patient access journey."),
    ("Access Simulator", "8_RCM_Access_Simulator.py", "Walk through benefits verification to claim submission."),
    ("Billing & Denials Insights", "9_Billing_and_Denials_Insights.py", "Visualize trends in denials and billing outcomes."),
    ("KPI Dashboard", "10_RCM_KPI_Dashboard.py", "Track operational performance and revenue metrics."),
    ("AR Aging Dashboard", "11_AR_Aging_Dashboard.py", "Analyze outstanding AR buckets and trends."),
    ("Denials Dashboard", "12_Denials_Dashboard.py", "Review denial types and actionable root causes."),
    ("Provider Performance", "13_Provider_Performance.py", "Compare provider utilization and efficiency."),
    ("PA Outcome Simulator", "14_PA_Outcome_Simulator.py", "Predict approval vs denial based on rules."),
    ("Claims Adjudication Simulator", "15_Claims_Adjudication_Simulator.py", "Understand how payers adjudicate claims."),
]

# -------- FRONT-END MODULE DISPLAY -------- #
st.header("Educational Modules")

# Display in a grid layout
cols_per_row = 2
for i in range(0, len(modules), cols_per_row):
    row_modules = modules[i:i + cols_per_row]
    cols = st.columns(cols_per_row)

    for col, (title, file, desc) in zip(cols, row_modules):
        with col:
            st.subheader(title)
            st.write(desc)
            st.page_link(f"pages/{file}", label="Open Module")
            st.markdown("---")
