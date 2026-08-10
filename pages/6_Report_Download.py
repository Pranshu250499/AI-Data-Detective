import streamlit as st
import pandas as pd
import numpy as np
import io
import os
import tempfile

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Report Download",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Data Detective Report")

st.write(
    "Generate a professional PDF and Excel report containing "
    "dataset analysis, visualizations, data quality and "
    "machine learning results."
)

st.divider()


# =========================================================
# CHECK DATASET
# =========================================================

if "df" not in st.session_state:

    st.warning(
        "⚠️ Please upload a dataset first from the Upload Data page."
    )

    st.stop()


df = st.session_state["df"].copy()


# =========================================================
# DATA QUALITY
# =========================================================

rows = df.shape[0]
columns = df.shape[1]
duplicates = int(df.duplicated().sum())
missing_values = int(df.isnull().sum().sum())

total_cells = rows * columns

if total_cells > 0:
    data_quality = (
        100
        - ((missing_values + duplicates) / total_cells * 100)
    )

    data_quality = max(0, min(100, data_quality))
else:
    data_quality = 100


# =========================================================
# DASHBOARD
# =========================================================

st.header("📊 Dataset Overview")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("Rows", rows)

with c2:
    st.metric("Columns", columns)

with c3:
    st.metric("Duplicates", duplicates)

with c4:
    st.metric("Missing Values", missing_values)

with c5:
    st.metric("Data Quality", f"{data_quality:.1f}%")


st.divider()


# =========================================================
# DATA PREVIEW
# =========================================================

st.header("👀 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)


st.divider()


# =========================================================
# STATISTICS
# =========================================================

st.header("📈 Statistical Summary")

statistics = df.describe(
    include="all"
).fillna("")

st.dataframe(
    statistics,
    use_container_width=True
)


st.divider()


# =========================================================
# VISUALIZATIONS
# =========================================================

st.header("📊 Automatic Visualizations")

numeric_columns = df.select_dtypes(
    include=np.number
).columns.tolist()


# ---------------------------------------------------------
# NUMERIC DISTRIBUTION
# ---------------------------------------------------------

if numeric_columns:

    selected_numeric = st.selectbox(
        "Select numerical column",
        numeric_columns
    )

    fig1, ax1 = plt.subplots()

    ax1.hist(
        df[selected_numeric].dropna(),
        bins=10
    )

    ax1.set_title(
        f"Distribution of {selected_numeric}"
    )

    ax1.set_xlabel(
        selected_numeric
    )

    ax1.set_ylabel(
        "Frequency"
    )

    st.pyplot(fig1)

    plt.close(fig1)


# ---------------------------------------------------------
# CORRELATION
# ---------------------------------------------------------

if len(numeric_columns) >= 2:

    st.subheader("🔗 Correlation Matrix")

    correlation = df[numeric_columns].corr()

    fig2, ax2 = plt.subplots(
        figsize=(8, 6)
    )

    image = ax2.imshow(
        correlation,
        aspect="auto"
    )

    ax2.set_xticks(
        range(len(correlation.columns))
    )

    ax2.set_xticklabels(
        correlation.columns,
        rotation=45,
        ha="right"
    )

    ax2.set_yticks(
        range(len(correlation.columns))
    )

    ax2.set_yticklabels(
        correlation.columns
    )

    ax2.set_title(
        "Feature Correlation Matrix"
    )

    fig2.colorbar(image)

    st.pyplot(fig2)

    plt.close(fig2)


st.divider()


# =========================================================
# AUTOMATIC INSIGHTS
# =========================================================

st.header("🤖 Automatic Data Insights")

insights = []


# Missing values

if missing_values == 0:

    insights.append(
        "✅ The dataset contains no missing values."
    )

else:

    missing_columns = (
        df.isnull()
        .sum()
        .loc[lambda x: x > 0]
    )

    for column, count in missing_columns.items():

        insights.append(
            f"⚠️ {column} contains {count} missing value(s)."
        )


# Duplicate rows

if duplicates > 0:

    insights.append(
        f"⚠️ The dataset contains {duplicates} duplicate row(s)."
    )

else:

    insights.append(
        "✅ No duplicate rows were detected."
    )


# Numeric insights

if "Marks" in df.columns:

    marks_mean = df["Marks"].mean()

    insights.append(
        f"📈 Average Marks: {marks_mean:.2f}"
    )


if "Attendance" in df.columns:

    attendance_mean = df["Attendance"].mean()

    insights.append(
        f"📊 Average Attendance: {attendance_mean:.2f}%"
    )


if "Study_Hours" in df.columns:

    study_mean = df["Study_Hours"].mean()

    insights.append(
        f"📚 Average Study Hours: {study_mean:.2f}"
    )


for insight in insights:

    st.write(insight)


st.divider()


# =========================================================
# MACHINE LEARNING
# =========================================================

st.header("🧠 Machine Learning Analysis")

ml_results = None

if "Placement" in df.columns:

    st.info(
        "Placement detected as the target column. "
        "The report will evaluate a Logistic Regression "
        "classification model."
    )

    ml_df = df.copy()

    target = "Placement"

    # Remove rows where target is missing
    ml_df = ml_df.dropna(
        subset=[target]
    )

    X = ml_df.drop(
        columns=[target]
    )

    y = ml_df[target].astype(str)

    # Remove identifier columns
    remove_columns = []

    for column in X.columns:

        if column.lower() in [
            "name",
            "id",
            "student_id",
            "customer_id"
        ]:

            remove_columns.append(column)

    X = X.drop(
        columns=remove_columns,
        errors="ignore"
    )

    if y.nunique() >= 2 and len(ml_df) >= 6:

        numeric_features = X.select_dtypes(
            include=np.number
        ).columns.tolist()

        categorical_features = X.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        numeric_pipeline = Pipeline([
            (
                "imputer",
                SimpleImputer(
                    strategy="median"
                )
            )
        ])

        categorical_pipeline = Pipeline([
            (
                "imputer",
                SimpleImputer(
                    strategy="most_frequent"
                )
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ])

        transformers = []

        if numeric_features:

            transformers.append(
                (
                    "numeric",
                    numeric_pipeline,
                    numeric_features
                )
            )

        if categorical_features:

            transformers.append(
                (
                    "categorical",
                    categorical_pipeline,
                    categorical_features
                )
            )

        preprocessor = ColumnTransformer(
            transformers=transformers
        )

        model = Pipeline([
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000
                )
            )
        ])

        try:

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.20,
                random_state=42,
                stratify=y
            )

            model.fit(
                X_train,
                y_train
            )

            predictions = model.predict(
                X_test
            )

            accuracy = accuracy_score(
                y_test,
                predictions
            )

            classes = sorted(
                y.unique()
            )

            matrix = confusion_matrix(
                y_test,
                predictions,
                labels=classes
            )

            ml_results = {
                "target": target,
                "algorithm": "Logistic Regression",
                "accuracy": accuracy,
                "classes": classes,
                "matrix": matrix,
                "y_test": y_test,
                "predictions": predictions
            }

            m1, m2, m3 = st.columns(3)

            with m1:

                st.metric(
                    "Target",
                    target
                )

            with m2:

                st.metric(
                    "Algorithm",
                    "Logistic Regression"
                )

            with m3:

                st.metric(
                    "Accuracy",
                    f"{accuracy * 100:.2f}%"
                )

            st.subheader(
                "Confusion Matrix"
            )

            st.dataframe(
                pd.DataFrame(
                    matrix,
                    index=classes,
                    columns=classes
                )
            )

            st.subheader(
                "Classification Report"
            )

            report = classification_report(
                y_test,
                predictions,
                output_dict=True,
                zero_division=0
            )

            st.dataframe(
                pd.DataFrame(report).transpose()
            )

        except Exception as error:

            st.warning(
                f"ML evaluation could not be completed: {error}"
            )

    else:

        st.warning(
            "Not enough data/classes available for ML evaluation."
        )

else:

    st.info(
        "No Placement column was detected. "
        "Machine Learning results will not be included."
    )


st.divider()


# =========================================================
# EXCEL REPORT
# =========================================================

st.header("📊 Excel Report")

excel_buffer = io.BytesIO()

with pd.ExcelWriter(
    excel_buffer,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Dataset",
        index=False
    )

    statistics.to_excel(
        writer,
        sheet_name="Statistics"
    )

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": [
            int(df[column].isnull().sum())
            for column in df.columns
        ]
    })

    missing_df.to_excel(
        writer,
        sheet_name="Missing Values",
        index=False
    )

    quality_df = pd.DataFrame({
        "Metric": [
            "Rows",
            "Columns",
            "Duplicates",
            "Missing Values",
            "Data Quality"
        ],
        "Value": [
            rows,
            columns,
            duplicates,
            missing_values,
            f"{data_quality:.2f}%"
        ]
    })

    quality_df.to_excel(
        writer,
        sheet_name="Data Quality",
        index=False
    )

    if ml_results is not None:

        ml_df_report = pd.DataFrame({
            "Metric": [
                "Target",
                "Algorithm",
                "Accuracy"
            ],
            "Value": [
                ml_results["target"],
                ml_results["algorithm"],
                f"{ml_results['accuracy'] * 100:.2f}%"
            ]
        })

        ml_df_report.to_excel(
            writer,
            sheet_name="Machine Learning",
            index=False
        )


excel_buffer.seek(0)

st.download_button(
    label="📊 Download Excel Report",
    data=excel_buffer,
    file_name="AI_Data_Detective_Report.xlsx",
    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    )
)


# =========================================================
# PDF GENERATOR
# =========================================================

def generate_pdf(dataframe, ml_results):

    pdf_buffer = io.BytesIO()

    document = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=35,
        leftMargin=35,
        topMargin=35,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=24,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Heading2"],
        alignment=TA_CENTER,
        fontSize=13,
        spaceAfter=25
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=16,
        spaceBefore=12,
        spaceAfter=10
    )

    normal_style = ParagraphStyle(
        "Normal",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13
    )

    elements = []


    # =====================================================
    # TITLE
    # =====================================================

    elements.append(
        Paragraph(
            "AI Data Detective",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "Automated Data Intelligence Report",
            subtitle_style
        )
    )


    # =====================================================
    # OVERVIEW
    # =====================================================

    elements.append(
        Paragraph(
            "📊 Dataset Overview",
            heading_style
        )
    )

    overview = [
        ["Metric", "Value"],
        ["Rows", str(rows)],
        ["Columns", str(columns)],
        ["Duplicates", str(duplicates)],
        ["Missing Values", str(missing_values)],
        ["Data Quality", f"{data_quality:.2f}%"]
    ]

    overview_table = Table(
        overview,
        colWidths=[280, 160]
    )

    overview_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2E4057")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 1),
                (1, -1),
                "CENTER"
            )
        ])
    )

    elements.append(
        overview_table
    )

    elements.append(
        Spacer(1, 20)
    )


    # =====================================================
    # DATA QUALITY
    # =====================================================

    elements.append(
        Paragraph(
            "🔍 Data Quality Analysis",
            heading_style
        )
    )

    quality_text = (
        f"The dataset contains {rows} rows and {columns} columns. "
        f"There are {duplicates} duplicate rows and "
        f"{missing_values} missing values. "
        f"The calculated data quality score is "
        f"{data_quality:.2f}%."
    )

    elements.append(
        Paragraph(
            quality_text,
            normal_style
        )
    )

    elements.append(
        Spacer(1, 15)
    )


    # =====================================================
    # COLUMN INFORMATION
    # =====================================================

    elements.append(
        Paragraph(
            "📋 Column Information",
            heading_style
        )
    )

    column_data = [
        ["Column", "Data Type"]
    ]

    for column in dataframe.columns:

        column_data.append([
            str(column),
            str(dataframe[column].dtype)
        ])

    column_table = Table(
        column_data,
        colWidths=[280, 160],
        repeatRows=1
    )

    column_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2E4057")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            )
        ])
    )

    elements.append(
        column_table
    )

    elements.append(
        Spacer(1, 20)
    )


    # =====================================================
    # DATA PREVIEW
    # =====================================================

    elements.append(
        Paragraph(
            "👀 Data Preview",
            heading_style
        )
    )

    preview = dataframe.head(8).copy()

    preview = preview.fillna(
        "Missing"
    ).astype(str)

    preview_data = [
        list(preview.columns)
    ]

    preview_data.extend(
        preview.values.tolist()
    )

    preview_table = Table(
        preview_data,
        repeatRows=1
    )

    preview_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2E4057")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.3,
                colors.grey
            ),
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    elements.append(
        preview_table
    )

    elements.append(
        PageBreak()
    )


    # =====================================================
    # STATISTICS
    # =====================================================

    elements.append(
        Paragraph(
            "📈 Statistical Analysis",
            heading_style
        )
    )

    numeric_df = dataframe.select_dtypes(
        include=np.number
    )

    if not numeric_df.empty:

        stats = numeric_df.describe().round(2)

        stats_data = [
            ["Statistic"] +
            list(stats.columns)
        ]

        for index in stats.index:

            stats_data.append(
                [str(index)] +
                [
                    str(value)
                    for value in stats.loc[index]
                ]
            )

        stats_table = Table(
            stats_data,
            repeatRows=1
        )

        stats_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#2E4057")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.3,
                    colors.grey
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ])
        )

        elements.append(
            stats_table
        )


    elements.append(
        Spacer(1, 25)
    )


    # =====================================================
    # MISSING VALUES
    # =====================================================

    elements.append(
        Paragraph(
            "🔍 Missing Value Analysis",
            heading_style
        )
    )

    missing_data = [
        ["Column", "Missing Values"]
    ]

    for column in dataframe.columns:

        missing_data.append([
            str(column),
            str(int(dataframe[column].isnull().sum()))
        ])

    missing_table = Table(
        missing_data,
        repeatRows=1
    )

    missing_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2E4057")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            )
        ])
    )

    elements.append(
        missing_table
    )

    elements.append(
        PageBreak()
    )


    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    elements.append(
        Paragraph(
            "🧠 Machine Learning Analysis",
            heading_style
        )
    )

    if ml_results is not None:

        ml_data = [
            ["Metric", "Result"],
            [
                "Target",
                ml_results["target"]
            ],
            [
                "Algorithm",
                ml_results["algorithm"]
            ],
            [
                "Accuracy",
                f"{ml_results['accuracy'] * 100:.2f}%"
            ]
        ]

        ml_table = Table(
            ml_data,
            colWidths=[280, 160]
        )

        ml_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#2E4057")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                )
            ])
        )

        elements.append(
            ml_table
        )

        elements.append(
            Spacer(1, 20)
        )


        # Confusion matrix

        elements.append(
            Paragraph(
                "Confusion Matrix",
                heading_style
            )
        )

        classes = ml_results["classes"]
        matrix = ml_results["matrix"]

        cm_data = [
            ["Actual / Predicted"] +
            [str(c) for c in classes]
        ]

        for i, class_name in enumerate(classes):

            cm_data.append(
                [str(class_name)] +
                [
                    str(value)
                    for value in matrix[i]
                ]
            )

        cm_table = Table(
            cm_data,
            repeatRows=1
        )

        cm_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#2E4057")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                )
            ])
        )

        elements.append(
            cm_table
        )

        elements.append(
            Spacer(1, 25)
        )

        elements.append(
            Paragraph(
                "The current dataset contains a very small number "
                "of records, so the reported accuracy should be "
                "interpreted as a demonstration of the ML pipeline "
                "rather than a production-quality performance estimate.",
                normal_style
            )
        )

    else:

        elements.append(
            Paragraph(
                "No machine learning results were available.",
                normal_style
            )
        )


    elements.append(
        Spacer(1, 30)
    )


    # =====================================================
    # FINAL CONCLUSION
    # =====================================================

    elements.append(
        Paragraph(
            "🤖 Final Conclusion",
            heading_style
        )
    )

    conclusion = (
        f"The AI Data Detective analyzed a dataset containing "
        f"{rows} rows and {columns} columns. "
        f"The analysis identified {duplicates} duplicate rows "
        f"and {missing_values} missing values. "
        f"The calculated data quality score was "
        f"{data_quality:.2f}%. "
    )

    if ml_results is not None:

        conclusion += (
            f"A {ml_results['algorithm']} model was evaluated "
            f"using {ml_results['target']} as the target variable, "
            f"achieving an accuracy of "
            f"{ml_results['accuracy'] * 100:.2f}% "
            f"on the test split."
        )

    elements.append(
        Paragraph(
            conclusion,
            normal_style
        )
    )

    elements.append(
        Spacer(1, 30)
    )

    elements.append(
        Paragraph(
            "Generated by AI Data Detective",
            normal_style
        )
    )


    document.build(
        elements
    )

    pdf_buffer.seek(0)

    return pdf_buffer


# =========================================================
# PDF DOWNLOAD
# =========================================================

st.divider()

st.header("📄 Professional PDF Report")

if st.button(
    "🚀 Generate Professional PDF"
):

    with st.spinner(
        "Generating professional report..."
    ):

        pdf_file = generate_pdf(
            df,
            ml_results
        )

        st.success(
            "✅ Professional PDF generated successfully!"
        )

        st.download_button(
            label="📥 Download Professional PDF",
            data=pdf_file,
            file_name="AI_Data_Detective_Professional_Report.pdf",
            mime="application/pdf"
        )