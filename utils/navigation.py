import streamlit as st

def show_navbar():
    st.markdown("""
        <style>
        .topnav {
            background-color: #0A1E3A;
            overflow: hidden;
            padding: 14px;
            border-radius: 6px;
            margin-bottom: 25px;
        }
        .topnav a {
            float: left;
            color: #ffffff;
            padding: 10px 16px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
        }
        .topnav a:hover {
            color: #4BB4FF;
        }
        </style>

        <div class="topnav">
            <a href="/?page=1_RCM_Overview">RCM Overview</a>
            <a href="/?page=2_Coverage_and_Eligibility">Coverage</a>
            <a href="/?page=3_Prior_Authorization">PA</a>
            <a href="/?page=4_Claims_Lifecycle">Claims</a>
            <a href="/?page=5_Denials_Management">Denials</a>
            <a href="/?page=10_RCM_KPI_Dashboard">KPI Dashboard</a>
            <a href="/?page=11_AR_Aging_Dashboard">AR Aging</a>
            <a href="/?page=12_Provider_Performance">Provider Performance</a>
            <a href="/?page=7_RCM_Timeline_Simulator">Simulators</a>
        </div>
    """, unsafe_allow_html=True)
