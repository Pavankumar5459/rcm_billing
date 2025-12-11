import streamlit as st

st.set_page_config(
    page_title="Hanvion Health – RCM Education Platform",
    layout="wide"
)

# -------------------------------------------------
# REMOVE SIDEBAR COMPLETELY (STRONG CSS OVERRIDE)
# -------------------------------------------------
st.markdown("""
<style>
    /* hide sidebar and hamburger */
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="stSidebarNav"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}

    /* remove space where sidebar was */
    .block-container {padding-left: 2rem !important; padding-right: 2rem !important;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #0EA5E9, #2563EB);
    padding: 28px;
    border-radius: 10px;
    margin-bottom: 20px;">
    <h1 style="color: white; margin-bottom: 4px;">
        Hanvion Health – RCM Education Platform
    </h1>
    <p style="color: white; font-size: 16px;">
        Interactive training modules explaining the full patient access and reimbursement pathway.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------
st.subheader("Educational Modules")

col1, col2 = st.columns(2)

# modules data (NO Coding Basics anymore)
modules = [
    ("RCM Overview", "Learn the end-to-end revenue cycle workflow.", "pages/1_RCM_Overview.py"),
    ("Coverage & Eligibility", "Understand payer benefits, benefit checks, and patient responsibility.", "pages/2_Coverage_and_Eligibility.py"),
    ("Prior Authorization", "Learn authorization workflows, requirements, and payer criteria.", "pages/3_Prior_Authorization.py"),
    ("Claims Lifecycle", "Understand how claims move from submission to adjudication.", "pages/4_Claims_Lifecycle.py"),
    ("Denials Management", "Identify denial causes and strategies to prevent revenue loss.", "pages/6_Denials_Management.py"),
    ("Out-of-Pocket Cost Education", "Explain deductibles, copays, and coinsurance to patients.", "pages/7_OOP_Cost_Education.py"),
    ("RCM Timeline Simulator", "Walk through each step of the revenue cycle interactively.", "pages/8_RCM_Timeline_Simulator.py"),
    ("Patient Access Journey Simulator", "Guided simulator from eligibility → PA → claims → appeals.", "pages/9_RCM_Access_Simulator.py")
]

for idx, (title, desc, path) in enumerate(modules):
    with (col1 if idx % 2 == 0 else col2):
        st.markdown(f"""
        <div style="border: 1px solid #E5E7EB; padding: 18px; border-radius: 10px;
                    background: #FFFFFF; margin-bottom: 20px;">
            <h3 style="margin: 0 0 6px 0;">{title}</h3>
            <p style="margin: 0 0 12px 0; color: #475569;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

        st.page_link(path, label="Open Module", icon="➡️")  # Most reliable navigation


st.markdown("---")
st.write("Use the buttons above to navigate to any RCM education module.")
