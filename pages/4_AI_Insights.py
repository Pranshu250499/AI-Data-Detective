import streamlit as st
import pandas as pd
import plotly.express as px

from utils.insights import (
    generate_basic_insights,
    get_top_numeric_columns
)


# =========================================================
# PREMIUM AI INSIGHTS UI
# =========================================================

st.html("""
<style>

    /* =====================================================
       APP BACKGROUND
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 229, 255, 0.08),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(76, 110, 245, 0.08),
                transparent 25%
            ),
            linear-gradient(
                135deg,
                #07111f 0%,
                #0b1628 50%,
                #07101d 100%
            );

        color: #f1f5f9;
    }


    /* =====================================================
       STREAMLIT HEADER
       Keep Deploy visible
       ===================================================== */

    [data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
    }

    [data-testid="stToolbar"] {
        background: transparent !important;
    }


    /* =====================================================
       STREAMLIT DECORATION
       ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* =====================================================
       MAIN CONTENT
       ===================================================== */

    .block-container {
        max-width: 1450px;

        /* Important:
           Keeps content below Streamlit header */
        padding-top: 4.8rem !important;

        padding-bottom: 3rem !important;
    }


    /* =====================================================
       HERO
       ===================================================== */

    .ai-hero {
        padding: 30px 34px;

        margin-top: 0 !important;
        margin-bottom: 24px !important;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(17, 37, 65, 0.96),
                rgba(9, 25, 44, 0.92)
            );

        border: 1px solid rgba(56, 189, 248, 0.20);

        box-shadow:
            0 20px 60px rgba(0,0,0,0.30),
            inset 0 1px 0 rgba(255,255,255,0.04);
    }


    .ai-badge {
        display: inline-block;

        padding: 7px 15px;

        border-radius: 999px;

        background:
            rgba(34,211,238,0.10);

        border:
            1px solid rgba(34,211,238,0.25);

        color: #67e8f9;

        font-size: 13px;

        font-weight: 800;

        letter-spacing: 0.5px;

        margin-bottom: 12px;
    }


    .ai-title {
        margin: 0;

        font-size: 35px;

        font-weight: 850;

        color: #f8fafc;
    }


    .ai-title span {
        color: #38bdf8;
    }


    .ai-description {
        margin-top: 9px;

        color: #94a3b8;

        font-size: 15px;

        line-height: 1.6;

        max-width: 950px;
    }


    /* =====================================================
       DATASET STATUS
       ===================================================== */

    .dataset-status {
        padding: 15px 19px;

        border-radius: 15px;

        background:
            linear-gradient(
                135deg,
                rgba(16,185,129,0.10),
                rgba(6,78,59,0.10)
            );

        border:
            1px solid rgba(16,185,129,0.20);

        color: #a7f3d0;

        margin-bottom: 25px;
    }


    /* =====================================================
       SECTION
       ===================================================== */

    .section-title {
        font-size: 21px;

        font-weight: 800;

        color: #e2e8f0;

        margin-top: 25px;

        margin-bottom: 6px;
    }


    .section-description {
        color: #64748b;

        font-size: 13px;

        margin-bottom: 17px;
    }


    /* =====================================================
       PROFILE CARDS
       ===================================================== */

    .profile-card {
        padding: 20px;

        min-height: 120px;

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                rgba(15,35,61,0.92),
                rgba(9,25,43,0.82)
            );

        border:
            1px solid rgba(56,189,248,0.12);

        box-shadow:
            0 10px 30px rgba(0,0,0,0.16);
    }


    .profile-icon {
        font-size: 25px;

        margin-bottom: 7px;
    }


    .profile-label {
        color: #94a3b8;

        font-size: 12px;

        text-transform: uppercase;

        letter-spacing: 0.7px;
    }


    .profile-value {
        color: #38bdf8;

        font-size: 26px;

        font-weight: 800;

        margin-top: 4px;
    }


    /* =====================================================
       AI PIPELINE
       ===================================================== */

    .pipeline-card {
        padding: 18px;

        min-height: 125px;

        border-radius: 17px;

        background:
            rgba(15,28,47,0.80);

        border:
            1px solid rgba(148,163,184,0.12);
    }


    .pipeline-number {
        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 1px;
    }


    .pipeline-title {
        color: #e2e8f0;

        font-weight: 750;

        font-size: 15px;

        margin-top: 6px;
    }


    .pipeline-text {
        color: #64748b;

        font-size: 12px;

        line-height: 1.5;

        margin-top: 6px;
    }


    /* =====================================================
       INSIGHT CARDS
       ===================================================== */

    .insight-card {
        padding: 18px 20px;

        border-radius: 17px;

        background:
            linear-gradient(
                145deg,
                rgba(15,35,61,0.92),
                rgba(9,25,43,0.84)
            );

        border:
            1px solid rgba(56,189,248,0.13);

        margin-bottom: 12px;

        box-shadow:
            0 10px 30px rgba(0,0,0,0.15);
    }


    .insight-text {
        color: #cbd5e1;

        font-size: 14px;

        line-height: 1.65;
    }


    /* =====================================================
       QUALITY SCORE
       ===================================================== */

    .quality-card {
        padding: 24px;

        border-radius: 20px;

        text-align: center;

        background:
            linear-gradient(
                145deg,
                rgba(15,35,61,0.95),
                rgba(8,24,43,0.90)
            );

        border:
            1px solid rgba(56,189,248,0.15);

        box-shadow:
            0 15px 40px rgba(0,0,0,0.20);
    }


    .quality-label {
        color: #94a3b8;

        font-size: 12px;

        text-transform: uppercase;

        letter-spacing: 1px;
    }


    .quality-value {
        color: #38bdf8;

        font-size: 42px;

        font-weight: 850;

        margin-top: 5px;
    }


    /* =====================================================
       CORRELATION CARD
       ===================================================== */

    .correlation-card {
        padding: 20px;

        border-radius: 19px;

        background:
            rgba(15,28,47,0.76);

        border:
            1px solid rgba(148,163,184,0.11);

        margin-bottom: 15px;
    }


    .correlation-title {
        color: #bae6fd;

        font-size: 16px;

        font-weight: 750;
    }


    .correlation-text {
        color: #64748b;

        font-size: 12px;

        margin-top: 5px;
    }


    /* =====================================================
       DATAFRAME
       ===================================================== */

    [data-testid="stDataFrame"] {
        border-radius: 15px;

        overflow: hidden;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .app-footer {
        margin-top: 40px;

        padding: 20px;

        text-align: center;

        border-top:
            1px solid rgba(148,163,184,0.10);

        color: #475569;

        font-size: 12px;
    }

</style>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="ai-hero">

    <div class="ai-badge">
        🧠 AI INVESTIGATION CENTER
    </div>

    <h1 class="ai-title">
        AI <span>Insights</span>
    </h1>

    <div class="ai-description">
        Automatically investigate your dataset, discover
        important patterns, identify quality issues and
        turn statistical analysis into meaningful findings.
    </div>

</div>
""")


# =========================================================
# DATASET CHECK
# =========================================================

if "df" not in st.session_state:

    st.warning(
        "⚠️ Please upload a dataset first."
    )

    st.info(
        "Go to 📤 Upload Data from the sidebar, "
        "upload your CSV or Excel file, then return here."
    )

    st.stop()


df = st.session_state["df"]

file_name = st.session_state.get(
    "file_name",
    "Dataset"
)


# =========================================================
# DATASET STATUS
# =========================================================

st.html(f"""
<div class="dataset-status">

    🟢 <strong>AI investigation active</strong>

    &nbsp; • &nbsp;

    {file_name}

    &nbsp; • &nbsp;

    {df.shape[0]:,} rows

    &nbsp; • &nbsp;

    {df.shape[1]:,} columns

</div>
""")


# =========================================================
# DATA PROFILE
# =========================================================

st.html("""
<div class="section-title">
    🔎 Dataset Intelligence
</div>

<div class="section-description">
    Quick profile of the dataset currently being investigated.
</div>
""")


numeric_columns = (
    df
    .select_dtypes(include="number")
    .columns
    .tolist()
)


categorical_columns = (
    df
    .select_dtypes(exclude="number")
    .columns
    .tolist()
)


missing_cells = int(
    df.isnull().sum().sum()
)


duplicate_rows = int(
    df.duplicated().sum()
)


p1, p2, p3, p4 = st.columns(4)


with p1:

    st.html(f"""
    <div class="profile-card">

        <div class="profile-icon">
            📊
        </div>

        <div class="profile-label">
            Total Rows
        </div>

        <div class="profile-value">
            {df.shape[0]:,}
        </div>

    </div>
    """)


with p2:

    st.html(f"""
    <div class="profile-card">

        <div class="profile-icon">
            🧩
        </div>

        <div class="profile-label">
            Total Columns
        </div>

        <div class="profile-value">
            {df.shape[1]:,}
        </div>

    </div>
    """)


with p3:

    st.html(f"""
    <div class="profile-card">

        <div class="profile-icon">
            🔢
        </div>

        <div class="profile-label">
            Numeric Fields
        </div>

        <div class="profile-value">
            {len(numeric_columns):,}
        </div>

    </div>
    """)


with p4:

    st.html(f"""
    <div class="profile-card">

        <div class="profile-icon">
            🔤
        </div>

        <div class="profile-label">
            Categorical Fields
        </div>

        <div class="profile-value">
            {len(categorical_columns):,}
        </div>

    </div>
    """)


# =========================================================
# AI PIPELINE
# =========================================================

st.html("""
<div class="section-title">
    ⚙️ AI Investigation Pipeline
</div>

<div class="section-description">
    Multiple analytical stages are used to understand your dataset.
</div>
""")


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            01 / PROFILE
        </div>

        <div class="pipeline-title">
            Dataset Structure
        </div>

        <div class="pipeline-text">
            Examines rows, columns and data types.
        </div>

    </div>
    """)


with a2:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            02 / QUALITY
        </div>

        <div class="pipeline-title">
            Data Quality
        </div>

        <div class="pipeline-text">
            Searches for missing values and duplicates.
        </div>

    </div>
    """)


with a3:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            03 / PATTERNS
        </div>

        <div class="pipeline-title">
            Pattern Detection
        </div>

        <div class="pipeline-text">
            Examines numerical characteristics and relationships.
        </div>

    </div>
    """)


with a4:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            04 / FINDINGS
        </div>

        <div class="pipeline-title">
            AI Findings
        </div>

        <div class="pipeline-text">
            Converts analysis into understandable observations.
        </div>

    </div>
    """)


# =========================================================
# KEY FINDINGS
# =========================================================

st.html("""
<div class="section-title">
    💡 Key Findings
</div>

<div class="section-description">
    Automatically generated observations from your dataset.
</div>
""")


insights = generate_basic_insights(df)


if insights:

    for insight in insights:

        st.html(f"""
        <div class="insight-card">

            <div class="insight-text">
                🔍 {insight}
            </div>

        </div>
        """)

else:

    st.info(
        "No automatic insights were generated for this dataset."
    )


# =========================================================
# DATA QUALITY
# =========================================================

st.html("""
<div class="section-title">
    🛡️ Data Quality Assessment
</div>

<div class="section-description">
    Evaluate missing data and duplicate records.
</div>
""")


total_cells = (
    df.shape[0] *
    df.shape[1]
)


if total_cells > 0:

    missing_score = (
        missing_cells /
        total_cells
    ) * 100

else:

    missing_score = 0


if len(df) > 0:

    duplicate_score = (
        duplicate_rows /
        len(df)
    ) * 100

else:

    duplicate_score = 0


quality_score = max(
    0,
    100 -
    missing_score -
    duplicate_score
)


q1, q2, q3 = st.columns(3)


with q1:

    st.html(f"""
    <div class="quality-card">

        <div class="quality-label">
            Overall Data Quality
        </div>

        <div class="quality-value">
            {quality_score:.1f}%
        </div>

    </div>
    """)


with q2:

    st.metric(
        "⚠️ Missing Cells",
        f"{missing_cells:,}"
    )


with q3:

    st.metric(
        "♻️ Duplicate Rows",
        f"{duplicate_rows:,}"
    )


if quality_score >= 90:

    st.success(
        "🟢 Excellent data quality — very little cleaning appears necessary."
    )

elif quality_score >= 70:

    st.warning(
        "🟡 Moderate data quality — some cleaning may be beneficial."
    )

else:

    st.error(
        "🔴 Data quality needs attention before deeper analysis."
    )


# =========================================================
# NUMERIC INTELLIGENCE
# =========================================================

st.html("""
<div class="section-title">
    📈 Numeric Intelligence
</div>

<div class="section-description">
    Summary of the most important numerical fields.
</div>
""")


top_columns = get_top_numeric_columns(df)


if top_columns.empty:

    st.info(
        "No numeric columns were found in this dataset."
    )

else:

    numeric_table = (
        top_columns
        .rename("Average Value")
        .to_frame()
    )

    st.dataframe(
        numeric_table,
        use_container_width=True
    )


# =========================================================
# CORRELATION ANALYSIS
# =========================================================

st.html("""
<div class="section-title">
    🔗 Relationship Intelligence
</div>

<div class="section-description">
    Explore relationships between numerical variables.
</div>
""")


numeric_df = df.select_dtypes(
    include="number"
)


if numeric_df.shape[1] >= 2:

    correlation = numeric_df.corr()


    st.html("""
    <div class="correlation-card">

        <div class="correlation-title">
            🔗 Correlation Matrix
        </div>

        <div class="correlation-text">
            Values closer to +1 indicate a positive relationship,
            while values closer to -1 indicate a negative relationship.
        </div>

    </div>
    """)


    fig = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        title="Variable Correlation Matrix"
    )


    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(7,17,31,0.75)",

        font=dict(
            color="#cbd5e1"
        ),

        title_font=dict(
            size=20
        ),

        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


else:

    st.info(
        "At least two numeric columns are required "
        "for correlation analysis."
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="app-footer">

    🧠 AI Data Detective
    &nbsp; • &nbsp;
    Intelligent Dataset Investigation Engine

</div>
""")