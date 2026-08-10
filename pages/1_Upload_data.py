import streamlit as st
import pandas as pd

from utils.data_loader import save_uploaded_file
from utils.preprocessing import (
    get_missing_values,
    get_duplicate_count
)


st.title("📤 Upload Data")

st.write(
    "Upload a CSV or Excel file to start analyzing your dataset."
)


uploaded_file = st.file_uploader(
    "Choose your dataset",
    type=["csv", "xlsx"]
)


if uploaded_file is not None:

    try:

        # Save the uploaded file
        file_path = save_uploaded_file(
            uploaded_file
        )

        # Read the dataset
        if uploaded_file.name.lower().endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)


        # Store dataset for other pages
        st.session_state["df"] = df

        st.session_state["file_name"] = (
            uploaded_file.name
        )

        st.session_state["file_path"] = (
            file_path
        )


        st.success(
            f"✅ {uploaded_file.name} uploaded successfully!"
        )


        # -------------------------------------------------
        # DATASET OVERVIEW
        # -------------------------------------------------

        st.subheader("📊 Dataset Overview")


        col1, col2, col3 = st.columns(3)


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


        # -------------------------------------------------
        # DATA PREVIEW
        # -------------------------------------------------

        st.subheader("👀 Data Preview")


        st.dataframe(
            df.head(10),
            use_container_width=True
        )


        # -------------------------------------------------
        # DATA TYPES
        # -------------------------------------------------

        st.subheader("🔤 Data Types")


        data_types = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })


        st.dataframe(
            data_types,
            use_container_width=True
        )


        # -------------------------------------------------
        # MISSING VALUES
        # -------------------------------------------------

        st.subheader("⚠️ Missing Values")


        missing = get_missing_values(df)


        missing_table = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values
        })


        st.dataframe(
            missing_table,
            use_container_width=True
        )


        st.info(
            "✅ Dataset is ready for Data Analysis "
            "and Visualization."
        )


    except Exception as error:

        st.error(
            f"❌ Error loading dataset: {error}"
        )