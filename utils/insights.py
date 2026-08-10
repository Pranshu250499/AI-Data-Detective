import pandas as pd
import numpy as np


def generate_basic_insights(df):
    """
    Generate automatic insights from a dataset.
    """

    insights = []

    # -------------------------------------------------
    # Dataset size
    # -------------------------------------------------

    rows = df.shape[0]
    columns = df.shape[1]

    insights.append(
        f"📊 The dataset contains {rows} rows "
        f"and {columns} columns."
    )

    # -------------------------------------------------
    # Missing values
    # -------------------------------------------------

    missing_total = int(
        df.isnull().sum().sum()
    )

    if missing_total == 0:

        insights.append(
            "✅ No missing values were detected."
        )

    else:

        insights.append(
            f"⚠️ The dataset contains "
            f"{missing_total} missing values."
        )

    # -------------------------------------------------
    # Duplicate rows
    # -------------------------------------------------

    duplicates = int(
        df.duplicated().sum()
    )

    if duplicates == 0:

        insights.append(
            "✅ No duplicate rows were detected."
        )

    else:

        insights.append(
            f"♻️ {duplicates} duplicate row(s) "
            f"were detected."
        )

    # -------------------------------------------------
    # Numeric columns
    # -------------------------------------------------

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:

        insights.append(
            "🔢 Numeric columns detected: "
            + ", ".join(numeric_columns)
        )

    # -------------------------------------------------
    # Categorical columns
    # -------------------------------------------------

    categorical_columns = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    if categorical_columns:

        insights.append(
            "🔤 Categorical columns detected: "
            + ", ".join(categorical_columns)
        )

    # -------------------------------------------------
    # Highest average numeric values
    # -------------------------------------------------

    for column in numeric_columns:

        if df[column].notna().any():

            mean_value = df[column].mean()

            insights.append(
                f"📈 Average {column}: "
                f"{mean_value:.2f}"
            )

    return insights


def get_top_numeric_columns(df, n=5):
    """
    Return numeric columns with the highest mean values.
    """

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.empty:
        return pd.DataFrame()

    means = numeric_df.mean().sort_values(
        ascending=False
    )

    return means.head(n)