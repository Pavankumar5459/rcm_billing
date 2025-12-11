import streamlit as st

def show_navbar():
    st.markdown("""
    <style>

    /* MAIN HEADER BAR */
    .hanvion-header {
        background-color: #E8F4FB;
        padding: 14px 28px;
        border-bottom: 1px solid #c7e2f5;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: sticky;
        top: 0;
        z-index: 999;
    }

    .hanvion-title {
        font-size: 22px;
        font-weight: 600;
        color: #003c63;
        margin: 0;
    }

    /* MENU LINKS */
    .menu-link {
        color: #003c63;
        margin-right: 20px;
        cursor: pointer;
        font-size: 16px;
        text-decoration: none;
        font-weight: 500;
    }
    .menu-link:hover {
        color: #2A7FDB;
    }

    /* DROPDOWN WRAPPER */
    .dropdown {
        position: relative;
        display: inline-block;
        margin-right: 20px;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #FFFFFF;
        min-width: 220px;
        box-shadow: 0px 6px 12px rgba(0,0,0,0.1);
        border-radius: 6px;
        z-index: 1;
        border: 1px solid #E2E8F0;
    }

    .dropdown-content a {
        color: #003c63;
        padding: 10px 16px;
        text-decoration: none;
        display: block;
        font-size: 15px;
    }

    .dropdown-content a:hover {
        background-color: #E8F4FB;
        color: #2A7FDB;
    }

    .dropdown:hover .dropdown-content {
        display: block;
    }

    </style>

    <div class="hanvion-header">
        <div class="hanvion-title">Hanvion Health</div>

        <div>
            <!-- EDUCATION MENU -->
            <div class="dropdown">
                <span class="menu-link">Education ▼</span>
                <div class="dropdown-content">
                    <a href="/?page=1_RCM_Overview">RCM Overview</a>
                    <a href="/?page=2_Coverage_and_Eligibility">Coverage & Eligibility</a>
                    <a href="/?page=3_Prior_Authorization">Prior Authorization</a>
                    <a href="/?page=4_Claims_Lifecycle">Claims Lifecycle</a>
                    <a href="/?page=6_Denials_Management">Denials Management</a>
                    <a href="/?page=7_OOP_Cost_Education">Cost Education</a>
                </div>
            </div>

            <!-- SIMULATORS MENU -->
            <div class="dropdown">
                <span class="menu-link">Simulators ▼</span>
                <div class="dropdown-content">
                    <a href="/?page=8_RCM_Timeline_Simulator">RCM Timeline Simulator</a>
                    <a href="/?page=9_RCM_Access_Simulator">Access Journey Simulator</a>
                    <a href="/?page=13_PA_Outcome_Simulator">PA Outcome Simulator</a>
                    <a href="/?page=14_Claims_Adjudication_Simulator">Claims Adjudication Simulator</a>
                </div>
            </div>

            <!-- ANALYTICS MENU -->
            <div class="dropdown">
                <span class="menu-link">Analytics ▼</span>
                <div class="dropdown-content">
                    <a href="/?page=10_Billing_and_Denials_Insights">Billing & Denials Insights</a>
                    <a href="/?page=11_RCM_KPI_Dashboard">RCM KPI Dashboard</a>
                    <a href="/?page=12_AR_Aging_Dashboard">AR Aging Dashboard</a>
                    <a href="/?page=15_Provider_Performance">Provider Performance</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

