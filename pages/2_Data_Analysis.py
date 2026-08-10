import streamlit as st
import pandas as pd

from utils.preprocessing import (
    get_missing_values,
    get_duplicate_count,
    get_numeric_columns,
    get_categorical_columns
)


st.title("📊 Data Analysis")

st.write(
    "Explore the structure and quality of your uploaded dataset."
)


# Check whether dataset exists
if "df" not in st.session_state:

    st.warning(
        "⚠️ Please upload a dataset first."
    )

    st.info(
        "Go to 📤 Upload Data from the sidebar."
    )

    st.stop()


# Retrieve dataset
df = st.session_state["df"]


st.success(
    f"Analyzing: {st.session_state.get('file_name', 'Dataset')}"
)


# =========================================================
# DATASET OVERVIEW
# =========================================================

st.header("📋 Dataset Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Rows",
        df.shape[0]
    )


with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )


with col3:
    st.metric(
        "Duplicates",
        get_duplicate_count(df)
    )


with col4:
    st.metric(
        "Missing Cells",
        int(df.isnull().sum().sum())
    )


# =========================================================
# DATA TYPES
# =========================================================

st.header("🔤 Column Information")


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
    use_container_width=True
)


# =========================================================
# NUMERIC / CATEGORICAL
# =========================================================

st.header("🧮 Column Categories")


numeric_columns = get_numeric_columns(df)
categorical_columns = get_categorical_columns(df)


col1, col2 = st.columns(2)


with col1:

    st.subheader("🔢 Numeric Columns")

    if numeric_columns:
        for column in numeric_columns:
            st.write(f"• {column}")
    else:
        st.write("No numeric columns found.")


with col2:

    st.subheader("🔤 Categorical Columns")

    if categorical_columns:
        for column in categorical_columns:
            st.write(f"• {column}")
    else:
        st.write("No categorical columns found.")


# =========================================================
# MISSING VALUES
# =========================================================

st.header("⚠️ Missing Value Analysis")


missing = get_missing_values(df)

missing_only = missing[missing > 0]


if missing_only.empty:

    st.success(
        "✅ Excellent! No missing values were found."
    )

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
        use_container_width=True
    )


# =========================================================
# DUPLICATES
# =========================================================

st.header("♻️ Duplicate Analysis")


duplicates = get_duplicate_count(df)


if duplicates == 0:

    st.success(
        "✅ No duplicate rows found."
    )

else:

    st.warning(
        f"⚠️ {duplicates} duplicate row(s) detected."
    )

    show_duplicates = st.checkbox(
        "Show duplicate rows"
    )

    if show_duplicates:

        duplicate_rows = df[
            df.duplicated(keep=False)
        ]

        st.dataframe(
            duplicate_rows,
            use_container_width=True
        )


# =========================================================
# STATISTICS
# =========================================================

st.header("📈 Statistical Summary")


if numeric_columns:

    statistics = df[numeric_columns].describe().T

    st.dataframe(
        statistics,
        use_container_width=True
    )

else:

    st.info(
        "No numeric columns available for statistical analysis."
    )