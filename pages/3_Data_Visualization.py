import streamlit as st
import plotly.express as px


# =========================================================
# CUSTOM UI
# =========================================================

st.html("""
<style>

    /* =====================================================
       GLOBAL APP BACKGROUND
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
       STREAMLIT TOP HEADER
       
       IMPORTANT:
       Do NOT hide the header.
       Keep Deploy visible but remove black appearance.
       ===================================================== */

    [data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
        backdrop-filter: none !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
    }

    [data-testid="stToolbar"] {
        background: transparent !important;
    }


    /* =====================================================
       HIDE ONLY STREAMLIT DECORATIONS
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
    padding-top: 4.8rem !important;
    padding-bottom: 3rem !important;
}


    /* =====================================================
       HERO
       ===================================================== */

    .hero {
        padding: 28px 32px;
        margin-top: 0 !important;
        margin-bottom: 24px !important;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(15, 35, 61, 0.96),
                rgba(8, 24, 43, 0.92)
            );

        border: 1px solid rgba(56, 189, 248, 0.20);

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.30),
            inset 0 1px 0 rgba(255,255,255,0.04);
    }


    .hero-badge {
        display: inline-block;

        padding: 7px 14px;

        border-radius: 999px;

        background: rgba(34, 211, 238, 0.10);

        border: 1px solid rgba(34, 211, 238, 0.25);

        color: #67e8f9;

        font-size: 13px;

        font-weight: 700;

        letter-spacing: 0.5px;

        margin-bottom: 12px;
    }


    .hero-title {
        font-size: 34px;

        font-weight: 800;

        margin: 0;

        color: #f8fafc;
    }


    .hero-title span {
        color: #38bdf8;
    }


    .hero-subtitle {
        color: #94a3b8;

        font-size: 15px;

        margin-top: 8px;

        line-height: 1.6;
    }


    /* =====================================================
       DATASET STATUS
       ===================================================== */

    .dataset-status {
        padding: 14px 18px;

        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                rgba(16, 185, 129, 0.10),
                rgba(6, 78, 59, 0.10)
            );

        border: 1px solid rgba(16, 185, 129, 0.20);

        color: #a7f3d0;

        margin-bottom: 24px;
    }


    /* =====================================================
       SECTION TITLES
       ===================================================== */

    .section-title {
        font-size: 21px;

        font-weight: 750;

        color: #e2e8f0;

        margin-top: 24px;

        margin-bottom: 8px;
    }


    .section-subtitle {
        color: #64748b;

        font-size: 13px;

        margin-top: 0;

        margin-bottom: 16px;
    }


    /* =====================================================
       VISUALIZATION INFO CARDS
       ===================================================== */

    .info-card {
        padding: 18px;

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                rgba(15, 35, 61, 0.92),
                rgba(10, 25, 43, 0.82)
            );

        border: 1px solid rgba(56, 189, 248, 0.12);

        min-height: 110px;

        box-shadow:
            0 10px 30px rgba(0,0,0,0.15);
    }


    .info-icon {
        font-size: 25px;

        margin-bottom: 6px;
    }


    .info-title {
        color: #e2e8f0;

        font-size: 15px;

        font-weight: 700;
    }


    .info-text {
        color: #64748b;

        font-size: 12px;

        margin-top: 5px;

        line-height: 1.5;
    }


    /* =====================================================
       SETTINGS CARD
       ===================================================== */

    .settings-card {
        padding: 22px;

        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                rgba(15, 28, 47, 0.90),
                rgba(8, 21, 37, 0.82)
            );

        border: 1px solid rgba(148, 163, 184, 0.12);

        box-shadow:
            0 15px 45px rgba(0,0,0,0.20);

        margin-bottom: 18px;
    }


    .settings-title {
        font-size: 16px;

        font-weight: 700;

        color: #bae6fd;

        margin-bottom: 4px;
    }


    .settings-description {
        font-size: 13px;

        color: #64748b;
    }


    /* =====================================================
       STREAMLIT SELECT BOX
       ===================================================== */

    div[data-baseweb="select"] > div {
        background-color: #101d31 !important;

        border-color:
            rgba(56, 189, 248, 0.18) !important;

        border-radius: 10px !important;
    }


    div[data-baseweb="select"] span {
        color: #e2e8f0 !important;
    }


    label {
        color: #cbd5e1 !important;

        font-weight: 600 !important;
    }


    /* =====================================================
       PLOTLY
       ===================================================== */

    .js-plotly-plot {
        border-radius: 18px;

        overflow: hidden;

        margin-top: 10px;
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
<div class="hero">

    <div class="hero-badge">
        📈 VISUAL INTELLIGENCE CENTER
    </div>

    <h1 class="hero-title">
        Data <span>Visualization</span>
    </h1>

    <div class="hero-subtitle">
        Transform raw dataset information into interactive
        visual insights. Explore patterns, trends,
        distributions and relationships.
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
        "upload your CSV or Excel file, "
        "then return to Data Visualization."
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

    🟢 <strong>Dataset connected:</strong>
    {file_name}

    &nbsp; • &nbsp;

    {df.shape[0]:,} rows

    &nbsp; • &nbsp;

    {df.shape[1]:,} columns

</div>
""")


# =========================================================
# QUICK VISUALIZATION GUIDE
# =========================================================

st.html("""
<div class="section-title">
    🎯 Choose Your Visualization
</div>

<div class="section-subtitle">
    Select the chart that best explains the pattern
    you're investigating.
</div>
""")


info1, info2, info3, info4 = st.columns(4)


with info1:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            📊
        </div>

        <div class="info-title">
            Compare
        </div>

        <div class="info-text">
            Compare values across categories.
        </div>

    </div>
    """)


with info2:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            📈
        </div>

        <div class="info-title">
            Track Trends
        </div>

        <div class="info-text">
            Discover how values change over time.
        </div>

    </div>
    """)


with info3:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            🔬
        </div>

        <div class="info-title">
            Explore
        </div>

        <div class="info-text">
            Examine relationships between variables.
        </div>

    </div>
    """)


with info4:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            📐
        </div>

        <div class="info-title">
            Distributions
        </div>

        <div class="info-text">
            Understand spread, outliers and frequency.
        </div>

    </div>
    """)


# =========================================================
# CHART SETTINGS
# =========================================================

st.html("""
<div class="section-title">
    ⚙️ Visualization Controls
</div>

<div class="section-subtitle">
    Configure the chart using your dataset columns.
</div>
""")


st.html("""
<div class="settings-card">

    <div class="settings-title">
        🎛️ Chart Configuration
    </div>

    <div class="settings-description">
        Choose a visualization type and configure
        its parameters below.
    </div>

</div>
""")


columns = df.columns.tolist()


chart_type = st.selectbox(
    "📌 Select Visualization Type",
    [
        "Bar Chart",
        "Line Chart",
        "Scatter Plot",
        "Histogram",
        "Box Plot",
        "Pie Chart"
    ]
)


# =========================================================
# PLOTLY TEMPLATE
# =========================================================

plot_template = "plotly_dark"


# =========================================================
# BAR / LINE / SCATTER
# =========================================================

if chart_type in [
    "Bar Chart",
    "Line Chart",
    "Scatter Plot"
]:

    col1, col2 = st.columns(2)


    with col1:

        x_column = st.selectbox(
            "🔹 X-axis",
            columns
        )


    with col2:

        y_column = st.selectbox(
            "🔹 Y-axis",
            columns
        )


    if chart_type == "Bar Chart":

        fig = px.bar(
            df,
            x=x_column,
            y=y_column,
            title=f"{y_column} by {x_column}",
            template=plot_template
        )


    elif chart_type == "Line Chart":

        fig = px.line(
            df,
            x=x_column,
            y=y_column,
            markers=True,
            title=f"{y_column} over {x_column}",
            template=plot_template
        )


    else:

        fig = px.scatter(
            df,
            x=x_column,
            y=y_column,
            title=f"{y_column} vs {x_column}",
            template=plot_template
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


# =========================================================
# HISTOGRAM
# =========================================================

elif chart_type == "Histogram":

    numeric_columns = (
        df
        .select_dtypes(include="number")
        .columns
        .tolist()
    )


    if not numeric_columns:

        st.warning(
            "⚠️ No numeric columns are available "
            "for a histogram."
        )


    else:

        column = st.selectbox(
            "🔢 Select Numeric Column",
            numeric_columns
        )


        fig = px.histogram(
            df,
            x=column,
            title=f"Distribution of {column}",
            template=plot_template
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


# =========================================================
# BOX PLOT
# =========================================================

elif chart_type == "Box Plot":

    numeric_columns = (
        df
        .select_dtypes(include="number")
        .columns
        .tolist()
    )


    if not numeric_columns:

        st.warning(
            "⚠️ No numeric columns are available "
            "for a box plot."
        )


    else:

        column = st.selectbox(
            "🔢 Select Numeric Column",
            numeric_columns
        )


        fig = px.box(
            df,
            y=column,
            title=f"Box Plot of {column}",
            template=plot_template
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


# =========================================================
# PIE CHART
# =========================================================

elif chart_type == "Pie Chart":

    col1, col2 = st.columns(2)


    with col1:

        category_column = st.selectbox(
            "🏷️ Category",
            columns
        )


    with col2:

        numeric_columns = (
            df
            .select_dtypes(include="number")
            .columns
            .tolist()
        )


        if numeric_columns:

            value_column = st.selectbox(
                "🔢 Value",
                numeric_columns
            )

        else:

            value_column = st.selectbox(
                "🔢 Value",
                columns
            )


    try:

        fig = px.pie(
            df,
            names=category_column,
            values=value_column,
            title=f"{value_column} by {category_column}",
            template=plot_template
        )


        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

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


    except Exception:

        st.error(
            "❌ Pie charts require a suitable "
            "categorical column and numeric value column."
        )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="app-footer">

    🔎 AI Data Detective
    &nbsp; • &nbsp;
    Visual Intelligence Engine

</div>
""")