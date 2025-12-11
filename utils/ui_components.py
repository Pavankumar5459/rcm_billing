import streamlit as st

def kpi_card(label, value):
    st.markdown(
        f"""
        <div style="
            background-color:#F2F7FF;
            padding:18px;
            border-radius:10px;
            border-left:6px solid #0047AB;
            margin-bottom:12px;">
            <h3 style="margin:0; color:#0047AB;">{value}</h3>
            <p style="margin:0; color:#333;">{label}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def section_header(text):
    st.markdown(f"<h2 style='color:#0047AB;'>{text}</h2>", unsafe_allow_html=True)
