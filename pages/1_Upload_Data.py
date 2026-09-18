import streamlit as st
import pandas as pd

from utils.data_loader import save_uploaded_file
from utils.preprocessing import (
    get_missing_values,
    get_duplicate_count
)

# =========================================================
# CUSTOM UI
# =========================================================

st.html("""
<style>
    .upload-hero {
        padding: 28px 32px;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            rgba(15, 35, 61, 0.96),
            rgba(8, 24, 43, 0.92)
        );
        border: 1px solid rgba(56, 189, 248, 0.20);
        margin-bottom: 24px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(34, 211, 238, 0.10);
        border: 1px solid rgba(34, 211, 238, 0.25);
        color: #67e8f9;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .title {
        font-size: 34px;
        font-weight: 800;
        color: #f8fafc;
        margin: 0;
    }

    .title span {
        color: #38bdf8;
    }

    .subtitle {
        color: #94a3b8;
        margin-top: 8px;
        font-size: 15px;
    }

    .upload-card {
        padding: 25px;
        border-radius: 20px;
        background: rgba(15, 28, 47, 0.80);
        border: 1px solid rgba(148,163,184,0.13);
        margin-bottom: 25px;
    }

    .card-title {
        color: #bae6fd;
        font-size: 18px;
        font-weight: 700;
    }

    .card-text {
        color: #64748b;
        font-size: 13px;
        margin-top: 5px;
    }
</style>
""")

# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="upload-hero">
    <div class="badge">📤 DATA INGESTION CENTER</div>

    <h1 class="title">
        Upload <span>Dataset</span>
    </h1>

    <div class="subtitle">
        Import your CSV or Excel dataset and begin your AI-powered
        investigation.
    </div>
</div>
""")

# =========================================================
# UPLOAD AREA
# =========================================================

st.html("""
<div class="upload-card">
    <div class="card-title">📁 Select your dataset</div>
    <div class="card-text">
        Supported formats: CSV and Excel (.xlsx)
    </div>
</div>
""")

uploaded_file = st.file_uploader(
    "Choose your dataset",
    type=["csv", "xlsx"],
    key="dataset_uploader"
)

# =========================================================
# PROCESS DATASET
# =========================================================

if uploaded_file is not None:

    try:

        # Reset file pointer
        uploaded_file.seek(0)

        # Read dataset
        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Save physical file
        uploaded_file.seek(0)
        file_path = save_uploaded_file(uploaded_file)

        # =================================================
        # IMPORTANT SESSION STATE
        # =================================================

        st.session_state["df"] = df.copy()
        st.session_state["file_name"] = uploaded_file.name
        st.session_state["file_path"] = file_path
        st.session_state["dataset_loaded"] = True

        # =================================================
        # SUCCESS
        # =================================================

        st.success(
            f"✅ {uploaded_file.name} uploaded successfully!"
        )

        st.divider()

        # =================================================
        # DATASET OVERVIEW
        # =================================================

        st.subheader("📊 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Rows",
                f"{df.shape[0]:,}"
            )

        with col2:
            st.metric(
                "Columns",
                f"{df.shape[1]:,}"
            )

        with col3:
            st.metric(
                "Duplicates",
                f"{get_duplicate_count(df):,}"
            )

        with col4:
            st.metric(
                "Missing Cells",
                f"{int(df.isnull().sum().sum()):,}"
            )

        # =================================================
        # PREVIEW
        # =================================================

        st.subheader("👀 Data Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # DATA TYPES
        # =================================================

        st.subheader("🔤 Data Types")

        data_types = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(
            data_types,
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # MISSING VALUES
        # =================================================

        st.subheader("⚠️ Missing Values")

        missing = get_missing_values(df)

        missing_table = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values
        })

        st.dataframe(
            missing_table,
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # READY STATUS
        # =================================================

        st.success(
            "🚀 Dataset loaded successfully. "
            "You can now use Data Analysis, "
            "Data Visualization, AI Insights and Machine Learning."
        )

    except Exception as error:

        st.error(
            f"❌ Error loading dataset: {error}"
        )

# =========================================================
# EXISTING SESSION STATUS
# =========================================================

elif st.session_state.get("dataset_loaded", False):

    if "df" in st.session_state:

        df = st.session_state["df"]

        st.success(
            f"🟢 Active dataset: "
            f"{st.session_state.get('file_name', 'Dataset')}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", f"{df.shape[0]:,}")

        with col2:
            st.metric("Columns", f"{df.shape[1]:,}")

        with col3:
            st.metric(
                "Missing Cells",
                f"{int(df.isnull().sum().sum()):,}"
            )