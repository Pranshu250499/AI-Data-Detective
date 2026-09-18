import streamlit as st
import pandas as pd

from utils.ml_model import (
    train_classification_models,
    train_regression_models
)


# =========================================================
# PREMIUM UI
# =========================================================

st.html("""
<style>

    /* ---------- APP BACKGROUND ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 229, 255, 0.07),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(59, 130, 246, 0.08),
                transparent 25%
            ),
            linear-gradient(
                135deg,
                #07111f 0%,
                #0b1628 50%,
                #07101d 100%
            );
    }


    /* ---------- STREAMLIT HEADER ---------- */

    [data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }


    /* ---------- MAIN CONTENT ---------- */

    .block-container {
        max-width: 1450px;
        padding-top: 4.8rem !important;
        padding-bottom: 3rem !important;
    }


    /* ---------- HERO ---------- */

    .ml-hero {
        padding: 30px 34px;
        margin-bottom: 24px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(17, 37, 65, 0.96),
                rgba(9, 25, 44, 0.92)
            );

        border: 1px solid rgba(56, 189, 248, 0.20);

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.30),
            inset 0 1px 0 rgba(255,255,255,0.04);
    }


    .ml-badge {
        display: inline-block;

        padding: 7px 15px;

        border-radius: 999px;

        background: rgba(34,211,238,0.10);

        border: 1px solid rgba(34,211,238,0.25);

        color: #67e8f9;

        font-size: 13px;

        font-weight: 800;

        letter-spacing: 0.5px;

        margin-bottom: 12px;
    }


    .ml-title {
        margin: 0;

        font-size: 35px;

        font-weight: 800;

        color: #f8fafc;
    }


    .ml-title span {
        color: #38bdf8;
    }


    .ml-description {
        margin-top: 9px;

        color: #94a3b8;

        font-size: 15px;

        line-height: 1.6;
    }


    /* ---------- DATASET STATUS ---------- */

    .dataset-status {
        padding: 15px 19px;

        border-radius: 15px;

        background:
            rgba(16,185,129,0.08);

        border:
            1px solid rgba(16,185,129,0.20);

        color: #a7f3d0;

        margin-bottom: 25px;
    }


    /* ---------- SECTION ---------- */

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

        margin-bottom: 16px;
    }


    /* ---------- INFO CARDS ---------- */

    .info-card {
        padding: 18px;

        min-height: 115px;

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
            0 10px 30px rgba(0,0,0,0.15);
    }


    .info-icon {
        font-size: 24px;
    }


    .info-title {
        color: #e2e8f0;

        font-size: 15px;

        font-weight: 750;

        margin-top: 5px;
    }


    .info-text {
        color: #64748b;

        font-size: 12px;

        line-height: 1.5;

        margin-top: 5px;
    }


    /* ---------- CONFIGURATION ---------- */

    .config-box {
        padding: 22px;

        border-radius: 20px;

        background:
            rgba(15,28,47,0.80);

        border:
            1px solid rgba(148,163,184,0.12);

        margin-bottom: 18px;
    }


    .config-title {
        color: #bae6fd;

        font-size: 17px;

        font-weight: 750;
    }


    .config-text {
        color: #64748b;

        font-size: 12px;

        margin-top: 5px;
    }


    /* ---------- SELECT BOX ---------- */

    div[data-baseweb="select"] > div {
        background-color: #101d31 !important;

        border-color:
            rgba(56,189,248,0.18) !important;

        border-radius: 10px !important;
    }


    div[data-baseweb="select"] span {
        color: #e2e8f0 !important;
    }


    label {
        color: #cbd5e1 !important;

        font-weight: 600 !important;
    }


    /* ---------- BUTTON ---------- */

    div.stButton > button {
        width: 100%;

        min-height: 48px;

        border-radius: 12px;

        background:
            linear-gradient(
                135deg,
                #0ea5e9,
                #2563eb
            );

        border:
            1px solid rgba(56,189,248,0.35);

        color: white;

        font-weight: 750;

        font-size: 15px;
    }


    /* ---------- BEST MODEL ---------- */

    .best-model {
        padding: 20px;

        border-radius: 18px;

        background:
            rgba(245,158,11,0.08);

        border:
            1px solid rgba(245,158,11,0.22);

        margin-top: 18px;

        margin-bottom: 20px;
    }


    .best-label {
        color: #fcd34d;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1px;
    }


    .best-name {
        color: #f8fafc;

        font-size: 21px;

        font-weight: 800;

        margin-top: 5px;
    }


    /* ---------- FOOTER ---------- */

    .ml-footer {
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
<div class="ml-hero">

    <div class="ml-badge">
        🧠 MACHINE LEARNING LAB
    </div>

    <h1 class="ml-title">
        Machine <span>Learning</span>
    </h1>

    <div class="ml-description">
        Train and compare multiple machine learning models
        on your dataset. Configure your experiment, evaluate
        performance and identify the best model.
    </div>

</div>
""")


# =========================================================
# GET DATA
# =========================================================

if "df" not in st.session_state:

    st.warning(
        "⚠️ Please upload a dataset first from the Upload Data page."
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

    🟢 <strong>Dataset ready for machine learning</strong>

    &nbsp; • &nbsp;

    {file_name}

    &nbsp; • &nbsp;

    {df.shape[0]:,} rows

    &nbsp; • &nbsp;

    {df.shape[1]:,} columns

</div>
""")


# =========================================================
# ML WORKFLOW
# =========================================================

st.html("""
<div class="section-title">
    ⚡ ML Workflow
</div>

<div class="section-description">
    Follow the steps below to configure and train your models.
</div>
""")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🎯</div>

        <div class="info-title">
            Target
        </div>

        <div class="info-text">
            Select the column you want to predict.
        </div>

    </div>
    """)


with col2:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🧩</div>

        <div class="info-title">
            Problem Type
        </div>

        <div class="info-text">
            Choose classification or regression.
        </div>

    </div>
    """)


with col3:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🚀</div>

        <div class="info-title">
            Training
        </div>

        <div class="info-text">
            Train multiple machine learning models.
        </div>

    </div>
    """)


with col4:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🏆</div>

        <div class="info-title">
            Evaluation
        </div>

        <div class="info-text">
            Compare performance and find the best model.
        </div>

    </div>
    """)


# =========================================================
# MODEL CONFIGURATION
# =========================================================

st.html("""
<div class="section-title">
    ⚙️ Model Configuration
</div>

<div class="section-description">
    Configure the machine learning experiment.
</div>

<div class="config-box">

    <div class="config-title">
        🎛️ Experiment Settings
    </div>

    <div class="config-text">
        Select a target column, choose the problem type
        and define the test-data percentage.
    </div>

</div>
""")


# =========================================================
# TARGET
# =========================================================

target_column = st.selectbox(
    "🎯 Select Target Column",
    df.columns
)


# =========================================================
# PROBLEM TYPE
# =========================================================

problem_type = st.selectbox(
    "🧩 Select Problem Type",
    [
        "Classification",
        "Regression"
    ]
)


# =========================================================
# TEST PERCENTAGE
# =========================================================

test_percentage = st.slider(
    "🧪 Test Data Percentage",
    min_value=20,
    max_value=40,
    value=20
)


train_percentage = 100 - test_percentage


c1, c2 = st.columns(2)


with c1:

    st.metric(
        "📚 Training Data",
        f"{train_percentage}%"
    )


with c2:

    st.metric(
        "🧪 Testing Data",
        f"{test_percentage}%"
    )


# =========================================================
# TRAIN
# =========================================================

st.write("")


if st.button(
    "🚀 Train & Compare Models",
    type="primary"
):

    try:

        test_size = test_percentage / 100


        if problem_type == "Classification":

            output = train_classification_models(
                df,
                target_column,
                test_size
            )

        else:

            output = train_regression_models(
                df,
                target_column,
                test_size
            )


        st.session_state["ml_output"] = output

        st.session_state["ml_target"] = target_column

        st.session_state["ml_problem_type"] = problem_type

        st.success(
            "✅ Models trained successfully!"
        )


    except Exception as e:

        st.error(
            f"❌ Model training failed: {e}"
        )


# =========================================================
# RESULTS
# =========================================================

if "ml_output" in st.session_state:

    output = st.session_state["ml_output"]

    results = output


    # =====================================================
    # GET STORED SETTINGS
    # =====================================================

    result_problem_type = st.session_state.get(
        "ml_problem_type",
        problem_type
    )

    result_target = st.session_state.get(
        "ml_target",
        target_column
    )


    st.divider()


    st.html("""
    <div class="section-title">
        📊 Model Comparison
    </div>

    <div class="section-description">
        Compare the performance of all trained models.
    </div>
    """)


    # =====================================================
    # COMPARISON TABLE
    # =====================================================

    comparison = []


    for name, result in results.items():

        if result_problem_type == "Classification":

            comparison.append({

                "Model": name,

                "Accuracy":
                    round(
                        result["accuracy"] * 100,
                        2
                    )

            })

        else:

            comparison.append({

                "Model": name,

                "RMSE":
                    round(
                        result["rmse"],
                        3
                    ),

                "R² Score":
                    round(
                        result["r2"],
                        3
                    )

            })


    comparison_df = pd.DataFrame(
        comparison
    )


    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # BEST MODEL
    # =====================================================

    if result_problem_type == "Classification":

        best_model = max(
            results.items(),
            key=lambda x: x[1]["accuracy"]
        )


        best_name = best_model[0]

        best_accuracy = (
            best_model[1]["accuracy"] * 100
        )


        st.html(f"""
        <div class="best-model">

            <div class="best-label">
                🏆 BEST MODEL
            </div>

            <div class="best-name">
                {best_name}
            </div>

            <div style="
                color:#94a3b8;
                font-size:13px;
                margin-top:5px;
            ">
                Accuracy: {best_accuracy:.2f}%
            </div>

        </div>
        """)


    else:

        best_model = max(
            results.items(),
            key=lambda x: x[1]["r2"]
        )


        best_name = best_model[0]

        best_r2 = best_model[1]["r2"]


        st.html(f"""
        <div class="best-model">

            <div class="best-label">
                🏆 BEST MODEL
            </div>

            <div class="best-name">
                {best_name}
            </div>

            <div style="
                color:#94a3b8;
                font-size:13px;
                margin-top:5px;
            ">
                R² Score: {best_r2:.3f}
            </div>

        </div>
        """)


    # =====================================================
    # CLASSIFICATION
    # =====================================================

    if result_problem_type == "Classification":

        st.html("""
        <div class="section-title">
            📈 Classification Evaluation
        </div>

        <div class="section-description">
            Detailed evaluation for each classification model.
        </div>
        """)


        for name, result in results.items():

            with st.expander(
                f"🔍 {name}"
            ):

                st.metric(
                    "🎯 Accuracy",
                    f"{result['accuracy'] * 100:.2f}%"
                )


                st.subheader(
                    "🔲 Confusion Matrix"
                )


                cm = result[
                    "confusion_matrix"
                ]


                st.dataframe(
                    pd.DataFrame(cm),
                    use_container_width=True
                )


                st.subheader(
                    "📋 Classification Report"
                )


                report = pd.DataFrame(
                    result[
                        "classification_report"
                    ]
                ).transpose()


                st.dataframe(
                    report,
                    use_container_width=True
                )


    # =====================================================
    # REGRESSION
    # =====================================================

    else:

        st.html("""
        <div class="section-title">
            📈 Regression Evaluation
        </div>

        <div class="section-description">
            Detailed performance metrics for each regression model.
        </div>
        """)


        for name, result in results.items():

            with st.expander(
                f"🔍 {name}"
            ):

                col1, col2 = st.columns(2)


                with col1:

                    st.metric(
                        "📉 RMSE",
                        f"{result['rmse']:.3f}"
                    )


                with col2:

                    st.metric(
                        "📈 R² Score",
                        f"{result['r2']:.3f}"
                    )


    # =====================================================
    # MODEL INFORMATION
    # =====================================================

    st.divider()


    st.html("""
    <div class="section-title">
        🔎 Model Information
    </div>

    <div class="section-description">
        Details about the current machine learning experiment.
    </div>
    """)


    info1, info2, info3 = st.columns(3)


    with info1:

        st.metric(
            "🎯 Target",
            str(result_target)
        )


    with info2:

        st.metric(
            "🧩 Problem",
            str(result_problem_type)
        )


    with info3:

        st.metric(
            "🤖 Models Tested",
            len(results)
        )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="ml-footer">

    🧠 AI Data Detective
    &nbsp; • &nbsp;
    Machine Learning Laboratory

</div>
""")