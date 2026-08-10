import streamlit as st
import pandas as pd

from utils.ml_model import (
    train_classification_models,
    train_regression_models
)


st.title("🧠 Machine Learning")

st.write(
    "Train and compare multiple machine learning models "
    "on your dataset."
)


# --------------------------------------------------
# GET DATA
# --------------------------------------------------

if "df" not in st.session_state:

    st.warning(
        "Please upload a dataset first from the Upload Data page."
    )

    st.stop()


df = st.session_state["df"]


# --------------------------------------------------
# MODEL CONFIGURATION
# --------------------------------------------------

st.header("⚙️ Model Configuration")


target_column = st.selectbox(
    "🎯 Select Target Column",
    df.columns
)


problem_type = st.selectbox(
    "🧩 Select Problem Type",
    [
        "Classification",
        "Regression"
    ]
)


test_percentage = st.slider(
    "Test Data Percentage",
    min_value=20,
    max_value=40,
    value=20
)


st.write(
    f"Training data: {100 - test_percentage}%"
)

st.write(
    f"Testing data: {test_percentage}%"
)


# --------------------------------------------------
# TRAIN MODELS
# --------------------------------------------------

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

        st.success(
            "✅ Models trained successfully!"
        )

    except Exception as e:

        st.error(
            f"❌ Model training failed: {e}"
        )


# --------------------------------------------------
# RESULTS
# --------------------------------------------------

if "ml_output" in st.session_state:

    output = st.session_state["ml_output"]

    results = output


    st.divider()

    st.header("📊 Model Comparison")


    comparison = []


    for name, result in results.items():

        if problem_type == "Classification":

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


    # --------------------------------------------------
    # BEST MODEL
    # --------------------------------------------------

    if problem_type == "Classification":

        best_model = max(
            results.items(),
            key=lambda x: x[1]["accuracy"]
        )

        st.success(
            f"🏆 Best Model: {best_model[0]} "
            f"({best_model[1]['accuracy'] * 100:.2f}% accuracy)"
        )

    else:

        best_model = max(
            results.items(),
            key=lambda x: x[1]["r2"]
        )

        st.success(
            f"🏆 Best Model: {best_model[0]} "
            f"(R² = {best_model[1]['r2']:.3f})"
        )


    # --------------------------------------------------
    # CLASSIFICATION DETAILS
    # --------------------------------------------------

    if problem_type == "Classification":

        st.divider()

        st.header("📈 Model Evaluation")


        for name, result in results.items():

            with st.expander(
                f"🔍 {name}"
            ):

                st.metric(
                    "Accuracy",
                    f"{result['accuracy'] * 100:.2f}%"
                )


                st.subheader(
                    "Confusion Matrix"
                )


                cm = result[
                    "confusion_matrix"
                ]


                st.dataframe(
                    pd.DataFrame(cm),
                    use_container_width=True
                )


                st.subheader(
                    "Classification Report"
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


    # --------------------------------------------------
    # REGRESSION DETAILS
    # --------------------------------------------------

    else:

        st.divider()

        st.header("📈 Regression Evaluation")


        for name, result in results.items():

            with st.expander(
                f"🔍 {name}"
            ):

                col1, col2 = st.columns(2)


                col1.metric(
                    "RMSE",
                    f"{result['rmse']:.3f}"
                )


                col2.metric(
                    "R² Score",
                    f"{result['r2']:.3f}"
                )


    # --------------------------------------------------
    # MODEL INFORMATION
    # --------------------------------------------------

    st.divider()

    st.header("🔎 Model Information")


    st.write(
        f"**Target:** `{target_column}`"
    )

    st.write(
        f"**Problem:** `{problem_type}`"
    )

    st.write(
        f"**Models Tested:** {len(results)}"
    )