import streamlit as st

# ------------------------------------------------------------
# CENTERED HEADER
# ------------------------------------------------------------
def centered_header(text):
    st.markdown(
        f"""
        <h1 style="
            text-align: center;
            color: #0047AB;
            font-weight: 700;
            margin-bottom: 25px;">
            {text}
        </h1>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# SECTION HEADER
# ------------------------------------------------------------
def section_title(text):
    st.markdown(
        f"""
        <h2 style="
            color: #0047AB;
            font-weight: 650;
            margin-top: 30px;
            margin-bottom: 12px;">
            {text}
        </h2>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# HANVION CARD (EDUCATION MODULES)
# ------------------------------------------------------------
def module_card(title, description):
    st.markdown(
        f"""
        <div class="hanvion-card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# KPI CARD
# ------------------------------------------------------------
def kpi_card(label, value):
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-value">{value}</div>
            <div class="kpi-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# INFO BLOCK (LIGHT BLUE BOX)
# ------------------------------------------------------------
def info_block(text):
    st.markdown(
        f"""
        <div class="info-block">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# TIMELINE BLOCKS (for PA, Claims Lifecycle, etc.)
# ------------------------------------------------------------
def timeline_step(step_num, title, details):
    st.markdown(
        f"""
        <div style="
            background-color: #F2F6FF;
            border-left: 5px solid #0047AB;
            padding: 16px;
            border-radius: 6px;
            margin-bottom: 14px;">
            <h4 style="color:#0047AB; margin:0 0 6px 0;">
                Step {step_num}: {title}
            </h4>
            <p style="margin:0; color:#333;">{details}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# TWO-COLUMN LAYOUT
# ------------------------------------------------------------
def two_columns(left_content, right_content):
    col1, col2 = st.columns(2)
    with col1:
        left_content()
    with col2:
        right_content()

# ------------------------------------------------------------
# CARD WITH BUTTON (used on home page)
# ------------------------------------------------------------
def module_card_with_button(title, description, button_label, page_path):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(
            f"""
            <div class="hanvion-card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.page_link(page_path, label=button_label, use_container_width=True)
