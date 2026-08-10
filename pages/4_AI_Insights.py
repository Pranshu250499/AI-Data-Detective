import streamlit as st
import pandas as pd

from utils.insights import (
    generate_basic_insights,
    get_top_numeric_columns
)


st.title("🤖 AI Insights")

st.write(
    """
    AI Data Detective automatically examines your dataset
    and identifies important patterns, data-quality issues,
    and statistical observations.
    """
)


# ---------------------------------------------------------
# CHECK DATASET
# ---------------------------------------------------------

if "df" not in st.session_state:

    st.warning(
        "⚠️ Please upload a dataset first."
    )

    st.info(
        "Go to 📤 Upload Data and upload a CSV or Excel file."
    )

    st.stop()


df = st.session_state["df"]


file_name = st.session_state.get(
    "file_name",
    "Dataset"
)


st.success(
    f"🔎 Analyzing: {file_name}"
)


# ---------------------------------------------------------
# KEY INSIGHTS
# ---------------------------------------------------------

st.header("🔍 Key Findings")


insights = generate_basic_insights(df)


for insight in insights:

    st.write(insight)


# ---------------------------------------------------------
# NUMERIC ANALYSIS
# ---------------------------------------------------------

st.header("📈 Numeric Data Analysis")


top_columns = get_top_numeric_columns(df)


if top_columns.empty:

    st.info(
        "No numeric columns were found."
    )

else:

    st.dataframe(
        top_columns.rename(
            "Average Value"
        ).to_frame(),
        use_container_width=True
    )


# ---------------------------------------------------------
# CORRELATION
# ---------------------------------------------------------

st.header("🔗 Correlation Analysis")


numeric_df = df.select_dtypes(
    include="number"
)


if numeric_df.shape[1] >= 2:

    correlation = numeric_df.corr()

    st.dataframe(
        correlation,
        use_container_width=True
    )

    st.info(
        """
        A correlation close to +1 means two variables tend
        to increase together. A correlation close to -1 means
        they tend to move in opposite directions.
        """
    )

else:

    st.info(
        "At least two numeric columns are required "
        "for correlation analysis."
    )


# ---------------------------------------------------------
# DATA QUALITY SCORE
# ---------------------------------------------------------

st.header("🛡️ Data Quality")


total_cells = df.shape[0] * df.shape[1]

missing_cells = int(
    df.isnull().sum().sum()
)

duplicate_rows = int(
    df.duplicated().sum()
)


if total_cells > 0:

    missing_score = (
        missing_cells / total_cells
    ) * 100

else:

    missing_score = 0


duplicate_score = (
    duplicate_rows / len(df) * 100
    if len(df) > 0
    else 0
)


quality_score = max(
    0,
    100 - missing_score - duplicate_score
)


st.metric(
    "Data Quality Score",
    f"{quality_score:.1f}%"
)


if quality_score >= 90:

    st.success(
        "🟢 Excellent data quality."
    )

elif quality_score >= 70:

    st.warning(
        "🟡 Moderate data quality. "
        "Some cleaning may be required."
    )

else:

    st.error(
        "🔴 Data quality needs attention."
    )