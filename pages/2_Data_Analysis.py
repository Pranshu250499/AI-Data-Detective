import streamlit as st
import pandas as pd

from utils.preprocessing import (
    get_missing_values,
    get_duplicate_count,
    get_numeric_columns,
    get_categorical_columns
)


# =========================================================
# PAGE STYLING
# =========================================================

st.html("""
<style>

.analysis-hero {
    padding: 32px;
    border-radius: 22px;
    background:
        radial-gradient(
            circle at 90% 20%,
            rgba(59,130,246,0.18),
            transparent 35%
        ),
        linear-gradient(135deg, #111d38, #0c1427);
    border: 1px solid rgba(96,165,250,0.20);
    margin-bottom: 28px;
}

.analysis-label {
    color: #60a5fa;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.analysis-title {
    color: #f8fafc;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 8px;
}

.analysis-description {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.6;
}

.dataset-badge {
    display: inline-block;
    margin-top: 16px;
    padding: 7px 12px;
    border-radius: 999px;
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.18);
    color: #86efac;
    font-size: 12px;
    font-weight: 650;
}

.section-title {
    color: #f8fafc;
    font-size: 23px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 12px;
}

.section-description {
    color: #7f8da3;
    font-size: 13px;
    margin-bottom: 18px;
}

.category-card {
    padding: 22px;
    border-radius: 17px;
    background:
        linear-gradient(
            145deg,
            #18243b,
            #0e1729
        );
    border: 1px solid rgba(148,163,184,0.12);
    min-height: 150px;
}

.category-icon {
    font-size: 25px;
    margin-bottom: 10px;
}

.category-title {
    color: #e2e8f0;
    font-size: 17px;
    font-weight: 750;
    margin-bottom: 10px;
}

.category-count {
    color: #60a5fa;
    font-size: 12px;
    font-weight: 650;
}

.health-good {
    padding: 18px 20px;
    border-radius: 15px;
    background: rgba(34,197,94,0.07);
    border: 1px solid rgba(34,197,94,0.18);
    color: #86efac;
}

.health-warning {
    padding: 18px 20px;
    border-radius: 15px;
    background: rgba(245,158,11,0.07);
    border: 1px solid rgba(245,158,11,0.18);
    color: #fcd34d;
}

</style>
""")


# =========================================================
# CHECK DATASET
# =========================================================

if "df" not in st.session_state:

    st.html("""
    <div class="analysis-hero">

        <div class="analysis-label">
            STEP 02 / INVESTIGATION
        </div>

        <div class="analysis-title">
            📊 Data Analysis
        </div>

        <div class="analysis-description">
            Explore the structure, quality and statistical
            characteristics of your dataset.
        </div>

    </div>
    """)

    st.warning(
        "⚠️ No dataset is currently loaded."
    )

    st.info(
        "📤 Go to Upload Data from the sidebar to begin your investigation."
    )

    st.stop()


# =========================================================
# RETRIEVE DATASET
# =========================================================

df = st.session_state["df"]

file_name = st.session_state.get(
    "file_name",
    "Dataset"
)


# =========================================================
# HERO
# =========================================================

st.html(f"""
<div class="analysis-hero">

    <div class="analysis-label">
        STEP 02 / DATA INVESTIGATION
    </div>

    <div class="analysis-title">
        📊 Analyze your evidence
    </div>

    <div class="analysis-description">
        Examine the structure, quality, patterns and
        statistical profile of your dataset.
    </div>

    <div class="dataset-badge">
        ● Analyzing: {file_name}
    </div>

</div>
""")


# =========================================================
# CALCULATE VALUES
# =========================================================

rows = df.shape[0]
columns = df.shape[1]
duplicates = get_duplicate_count(df)
missing_cells = int(df.isnull().sum().sum())

numeric_columns = get_numeric_columns(df)
categorical_columns = get_categorical_columns(df)


# =========================================================
# DATASET OVERVIEW
# =========================================================

st.html("""
<div class="section-title">
    📋 Dataset health overview
</div>

<div class="section-description">
    A quick snapshot of the evidence currently under investigation.
</div>
""")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Rows",
        f"{rows:,}"
    )


with col2:

    st.metric(
        "Total Columns",
        f"{columns:,}"
    )


with col3:

    st.metric(
        "Duplicate Rows",
        f"{duplicates:,}"
    )


with col4:

    st.metric(
        "Missing Cells",
        f"{missing_cells:,}"
    )


# =========================================================
# COLUMN INFORMATION
# =========================================================

st.html("""
<div class="section-title">
    🔤 Column intelligence
</div>

<div class="section-description">
    Understand the type, completeness and uniqueness of every column.
</div>
""")


column_info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values,
    "Unique Values": [
        df[column].nunique()
        for column in df.columns
    ]
})


st.dataframe(
    column_info,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# COLUMN CATEGORIES
# =========================================================

st.html("""
<div class="section-title">
    🧬 Column categories
</div>

<div class="section-description">
    Your dataset's variables grouped by their analytical role.
</div>
""")


col1, col2 = st.columns(2)


with col1:

    numeric_preview = ", ".join(
        numeric_columns[:5]
    )

    if len(numeric_columns) > 5:
        numeric_preview += " ..."

    st.html(f"""
    <div class="category-card">

        <div class="category-icon">
            🔢
        </div>

        <div class="category-title">
            Numeric Columns
        </div>

        <div class="category-count">
            {len(numeric_columns)} numeric variable(s)
        </div>

    </div>
    """)

    if numeric_columns:

        st.write(
            ", ".join(numeric_columns)
        )

    else:

        st.caption(
            "No numeric columns found."
        )


with col2:

    st.html(f"""
    <div class="category-card">

        <div class="category-icon">
            🔤
        </div>

        <div class="category-title">
            Categorical Columns
        </div>

        <div class="category-count">
            {len(categorical_columns)} categorical variable(s)
        </div>

    </div>
    """)

    if categorical_columns:

        st.write(
            ", ".join(categorical_columns)
        )

    else:

        st.caption(
            "No categorical columns found."
        )


# =========================================================
# MISSING VALUES
# =========================================================

st.html("""
<div class="section-title">
    ⚠️ Missing value investigation
</div>

<div class="section-description">
    Identify incomplete fields that may affect your analysis.
</div>
""")


missing = get_missing_values(df)

missing_only = missing[missing > 0]


if missing_only.empty:

    st.html("""
    <div class="health-good">
        <strong>✓ Dataset looks complete</strong><br>
        No missing values were detected.
    </div>
    """)

else:

    missing_table = pd.DataFrame({
        "Column": missing_only.index,
        "Missing Values": missing_only.values,
        "Percentage": (
            missing_only.values /
            len(df) *
            100
        ).round(2)
    })

    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# DUPLICATE ANALYSIS
# =========================================================

st.html("""
<div class="section-title">
    ♻️ Duplicate investigation
</div>

<div class="section-description">
    Check whether repeated records are present in your dataset.
</div>
""")


if duplicates == 0:

    st.html("""
    <div class="health-good">
        <strong>✓ No duplicate rows detected</strong><br>
        Every record appears to be unique.
    </div>
    """)

else:

    st.html(f"""
    <div class="health-warning">
        <strong>⚠ {duplicates:,} duplicate row(s) detected</strong><br>
        Review the repeated records before further analysis.
    </div>
    """)

    show_duplicates = st.checkbox(
        "Show duplicate rows"
    )

    if show_duplicates:

        duplicate_rows = df[
            df.duplicated(keep=False)
        ]

        st.dataframe(
            duplicate_rows,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# STATISTICS
# =========================================================

st.html("""
<div class="section-title">
    📈 Statistical evidence
</div>

<div class="section-description">
    Descriptive statistics for your numeric variables.
</div>
""")


if numeric_columns:

    statistics = df[numeric_columns].describe().T

    st.dataframe(
        statistics,
        use_container_width=True
    )

else:

    st.info(
        "No numeric columns are available for statistical analysis."
    )


# =========================================================
# FINAL STATUS
# =========================================================

if missing_cells == 0 and duplicates == 0:

    st.success(
        "🟢 Investigation status: Dataset quality looks good."
    )

elif missing_cells > 0 or duplicates > 0:

    st.warning(
        "🟡 Investigation status: Review the quality findings above before continuing."
    )