import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
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
    PageBreak
)


# =========================================================
# PREMIUM PAGE STYLE
# =========================================================

st.html(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 8% 8%,
                rgba(37, 99, 235, 0.14),
                transparent 27%
            ),
            radial-gradient(
                circle at 92% 12%,
                rgba(6, 182, 212, 0.11),
                transparent 25%
            ),
            #07111f;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 4.8rem !important;
        padding-bottom: 3rem !important;
    }

    .report-hero {
        padding: 38px 40px;
        border-radius: 24px;
        margin-bottom: 28px;

        background:
            linear-gradient(
                135deg,
                rgba(17, 43, 75, 0.98),
                rgba(8, 25, 46, 0.98)
            );

        border: 1px solid rgba(56, 189, 248, 0.25);

        box-shadow:
            0 22px 55px rgba(0, 0, 0, 0.30),
            inset 0 1px 0 rgba(255, 255, 255, 0.04);
    }

    .report-kicker {
        color: #38bdf8;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .report-title {
        color: #f8fbff;
        font-size: 42px;
        line-height: 1.12;
        font-weight: 850;
        margin: 0;
    }

    .report-subtitle {
        color: #a5b7cb;
        font-size: 16px;
        line-height: 1.65;
        max-width: 900px;
        margin-top: 13px;
    }

    .dataset-status {
        display: flex;
        align-items: center;
        gap: 13px;

        padding: 17px 20px;
        margin-bottom: 25px;

        border-radius: 16px;

        background: rgba(13, 31, 53, 0.85);
        border: 1px solid rgba(96, 165, 250, 0.16);
    }

    .status-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 12px rgba(34, 197, 94, 0.75);
    }

    .status-small {
        color: #7f95ad;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .status-file {
        color: #f1f7ff;
        font-size: 16px;
        font-weight: 750;
        margin-top: 2px;
    }

    .section-kicker {
        color: #38bdf8;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.6px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .section-title {
        color: #f5f9ff;
        font-size: 27px;
        font-weight: 800;
        margin-bottom: 17px;
    }

    .insight-card {
        padding: 15px 18px;
        margin-bottom: 9px;

        border-radius: 13px;

        background: rgba(13, 30, 51, 0.82);
        border: 1px solid rgba(96, 165, 250, 0.13);

        color: #dbe8f7;
        font-size: 14px;
        line-height: 1.5;
    }

    .export-card {
        padding: 24px;
        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                rgba(15, 39, 67, 0.98),
                rgba(8, 25, 45, 0.98)
            );

        border: 1px solid rgba(56, 189, 248, 0.19);

        box-shadow:
            0 18px 45px rgba(0, 0, 0, 0.22);

        margin-bottom: 15px;
    }

    .export-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .export-title {
        color: #f8fbff;
        font-size: 20px;
        font-weight: 800;
    }

    .export-text {
        color: #99acc2;
        font-size: 14px;
        line-height: 1.55;
        margin-top: 7px;
    }

    .footer-note {
        text-align: center;
        color: #687d96;
        font-size: 12px;

        margin-top: 38px;
        padding-top: 20px;

        border-top: 1px solid rgba(148, 163, 184, 0.10);
    }

    </style>
    """
)


# =========================================================
# HERO
# =========================================================

st.html(
    """
    <div class="report-hero">

        <div class="report-kicker">
            AI DATA DETECTIVE / REPORT CENTER
        </div>

        <div class="report-title">
            Professional Report Studio
        </div>

        <div class="report-subtitle">
            Generate a complete intelligence report containing
            dataset quality, statistics, insights, visual analysis,
            and machine learning evaluation.
        </div>

    </div>
    """
)


# =========================================================
# DATASET CHECK
# =========================================================

if "df" not in st.session_state:

    st.warning(
        "Please upload a dataset first from the Upload Data page."
    )

    st.info(
        "Go to Upload Data from the sidebar and upload a CSV or Excel file."
    )

    st.stop()


df = st.session_state["df"].copy()

file_name = st.session_state.get(
    "file_name",
    "Dataset"
)


# =========================================================
# DATASET STATUS
# =========================================================

st.html(
    f"""
    <div class="dataset-status">

        <div class="status-dot"></div>

        <div>
            <div class="status-small">
                Active Dataset
            </div>

            <div class="status-file">
                {file_name}
            </div>
        </div>

    </div>
    """
)


# =========================================================
# DATA QUALITY CALCULATION
# =========================================================

rows = int(df.shape[0])
columns = int(df.shape[1])

duplicates = int(
    df.duplicated().sum()
)

missing_values = int(
    df.isnull().sum().sum()
)

total_cells = rows * columns

if total_cells > 0:

    data_quality = (
        100
        -
        (
            (missing_values + duplicates)
            / total_cells
            * 100
        )
    )

    data_quality = max(
        0,
        min(100, data_quality)
    )

else:

    data_quality = 100


# =========================================================
# DATASET OVERVIEW
# =========================================================

st.html(
    """
    <div class="section-kicker">
        DATASET INTELLIGENCE
    </div>

    <div class="section-title">
        Dataset Overview
    </div>
    """
)


c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "Rows",
        f"{rows:,}"
    )

with c2:
    st.metric(
        "Columns",
        f"{columns:,}"
    )

with c3:
    st.metric(
        "Duplicates",
        f"{duplicates:,}"
    )

with c4:
    st.metric(
        "Missing Values",
        f"{missing_values:,}"
    )

with c5:
    st.metric(
        "Data Quality",
        f"{data_quality:.1f}%"
    )


st.divider()


# =========================================================
# DATA PREVIEW
# =========================================================

st.html(
    """
    <div class="section-kicker">
        DATA EXPLORER
    </div>

    <div class="section-title">
        Dataset Preview
    </div>
    """
)

st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True
)


# =========================================================
# STATISTICAL SUMMARY
# =========================================================

st.divider()

st.html(
    """
    <div class="section-kicker">
        STATISTICAL ENGINE
    </div>

    <div class="section-title">
        Statistical Summary
    </div>
    """
)

try:

    statistics = (
        df.describe(
            include="all"
        )
        .fillna("")
    )

except Exception:

    statistics = (
        df.describe()
        .fillna("")
    )


st.dataframe(
    statistics,
    use_container_width=True
)


# =========================================================
# AUTOMATIC INSIGHTS
# =========================================================

st.divider()

st.html(
    """
    <div class="section-kicker">
        AI INSIGHT ENGINE
    </div>

    <div class="section-title">
        Automatic Data Insights
    </div>
    """
)

insights = []


# Missing values

if missing_values == 0:

    insights.append(
        "The dataset contains no missing values."
    )

else:

    missing_columns = (
        df.isnull()
        .sum()
    )

    missing_columns = (
        missing_columns[
            missing_columns > 0
        ]
    )

    for column, count in missing_columns.items():

        insights.append(
            f"{column} contains {int(count)} missing value(s)."
        )


# Duplicate rows

if duplicates > 0:

    insights.append(
        f"The dataset contains {duplicates} duplicate row(s)."
    )

else:

    insights.append(
        "No duplicate rows were detected."
    )


# Numeric insights

numeric_columns = (
    df.select_dtypes(
        include=np.number
    )
    .columns
    .tolist()
)


for column in numeric_columns[:6]:

    try:

        mean_value = df[column].mean()

        if pd.notna(mean_value):

            insights.append(
                f"Average {column}: {mean_value:.2f}"
            )

    except Exception:

        pass


for insight in insights:

    st.html(
        f"""
        <div class="insight-card">
            {insight}
        </div>
        """
    )


# =========================================================
# CORRELATION ANALYSIS
# =========================================================

if len(numeric_columns) >= 2:

    st.divider()

    st.html(
        """
        <div class="section-kicker">
            RELATIONSHIP ANALYSIS
        </div>

        <div class="section-title">
            Feature Correlation
        </div>
        """
    )

    correlation = (
        df[numeric_columns]
        .corr()
    )

    st.dataframe(
        correlation.round(3),
        use_container_width=True
    )

else:

    correlation = None


# =========================================================
# MACHINE LEARNING
# =========================================================

st.divider()

st.html(
    """
    <div class="section-kicker">
        PREDICTIVE ANALYTICS
    </div>

    <div class="section-title">
        Machine Learning Analysis
    </div>
    """
)

ml_results = None


if "Placement" in df.columns:

    st.info(
        "Placement detected as the target column. "
        "A Logistic Regression classification model "
        "will be evaluated."
    )

    ml_df = df.copy()

    target = "Placement"

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

            remove_columns.append(
                column
            )


    X = X.drop(
        columns=remove_columns,
        errors="ignore"
    )


    if (
        y.nunique() >= 2
        and len(ml_df) >= 6
        and len(X.columns) > 0
    ):

        numeric_features = (
            X.select_dtypes(
                include=np.number
            )
            .columns
            .tolist()
        )

        categorical_features = (
            X.select_dtypes(
                exclude=np.number
            )
            .columns
            .tolist()
        )


        transformers = []


        if numeric_features:

            numeric_pipeline = Pipeline(
                [
                    (
                        "imputer",
                        SimpleImputer(
                            strategy="median"
                        )
                    )
                ]
            )

            transformers.append(
                (
                    "numeric",
                    numeric_pipeline,
                    numeric_features
                )
            )


        if categorical_features:

            categorical_pipeline = Pipeline(
                [
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
                ]
            )

            transformers.append(
                (
                    "categorical",
                    categorical_pipeline,
                    categorical_features
                )
            )


        if transformers:

            preprocessor = ColumnTransformer(
                transformers=transformers
            )


            model = Pipeline(
                [
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
                ]
            )


            try:

                X_train, X_test, y_train, y_test = (
                    train_test_split(
                        X,
                        y,
                        test_size=0.20,
                        random_state=42,
                        stratify=y
                    )
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
                    ),
                    use_container_width=True
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
                    pd.DataFrame(
                        report
                    ).transpose(),
                    use_container_width=True
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
        "Machine Learning results will not be included "
        "in the generated report."
    )


# =========================================================
# EXCEL REPORT
# =========================================================

st.divider()

st.html(
    """
    <div class="section-kicker">
        EXPORT CENTER
    </div>

    <div class="section-title">
        Excel Report
    </div>

    <div class="export-card">

        <div class="export-icon">
            XLSX
        </div>

        <div class="export-title">
            Excel Intelligence Workbook
        </div>

        <div class="export-text">
            Includes the complete dataset, statistics,
            missing-value analysis, data-quality metrics,
            column information, correlation analysis and
            machine-learning results when available.
        </div>

    </div>
    """
)


excel_buffer = io.BytesIO()


with pd.ExcelWriter(
    excel_buffer,
    engine="openpyxl"
) as writer:

    # Dataset

    df.to_excel(
        writer,
        sheet_name="Dataset",
        index=False
    )


    # Statistics

    statistics.to_excel(
        writer,
        sheet_name="Statistics"
    )


    # Missing Values

    missing_df = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing Values": [
                int(
                    df[column]
                    .isnull()
                    .sum()
                )
                for column in df.columns
            ]
        }
    )


    missing_df.to_excel(
        writer,
        sheet_name="Missing Values",
        index=False
    )


    # Data Quality

    quality_df = pd.DataFrame(
        {
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
        }
    )


    quality_df.to_excel(
        writer,
        sheet_name="Data Quality",
        index=False
    )


    # Column Information

    column_info = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": [
                str(
                    df[column].dtype
                )
                for column in df.columns
            ],
            "Missing Values": [
                int(
                    df[column]
                    .isnull()
                    .sum()
                )
                for column in df.columns
            ],
            "Unique Values": [
                int(
                    df[column]
                    .nunique()
                )
                for column in df.columns
            ]
        }
    )


    column_info.to_excel(
        writer,
        sheet_name="Column Information",
        index=False
    )


    # Correlation

    if correlation is not None:

        correlation.to_excel(
            writer,
            sheet_name="Correlation"
        )


    # Machine Learning

    if ml_results is not None:

        ml_report = pd.DataFrame(
            {
                "Metric": [
                    "Target",
                    "Algorithm",
                    "Accuracy"
                ],
                "Value": [
                    ml_results["target"],
                    ml_results["algorithm"],
                    (
                        f"{ml_results['accuracy'] * 100:.2f}%"
                    )
                ]
            }
        )


        ml_report.to_excel(
            writer,
            sheet_name="Machine Learning",
            index=False
        )


excel_buffer.seek(0)


st.download_button(
    label="Download Excel Report",
    data=excel_buffer,
    file_name="AI_Data_Detective_Report.xlsx",
    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    ),
    use_container_width=True
)


# =========================================================
# PDF GENERATOR
# =========================================================

def generate_pdf(
    dataframe,
    ml_results
):

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
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=24,
        leading=30,
        textColor=colors.HexColor(
            "#123B66"
        ),
        spaceAfter=8
    )


    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["BodyText"],
        alignment=TA_CENTER,
        fontSize=11,
        leading=16,
        textColor=colors.HexColor(
            "#64748B"
        ),
        spaceAfter=25
    )


    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontSize=16,
        leading=20,
        textColor=colors.HexColor(
            "#123B66"
        ),
        spaceBefore=12,
        spaceAfter=10
    )


    normal_style = ParagraphStyle(
        "ReportNormal",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor(
            "#334155"
        )
    )


    small_style = ParagraphStyle(
        "ReportSmall",
        parent=styles["BodyText"],
        fontSize=7,
        leading=9,
        textColor=colors.HexColor(
            "#475569"
        )
    )


    elements = []


    # =====================================================
    # COVER / TITLE
    # =====================================================

    elements.append(
        Spacer(1, 45)
    )


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


    elements.append(
        Spacer(1, 15)
    )


    cover_data = [
        ["Report Information", "Value"],
        ["Dataset", str(file_name)],
        ["Rows", str(rows)],
        ["Columns", str(columns)],
        ["Data Quality", f"{data_quality:.2f}%"]
    ]


    cover_table = Table(
        cover_data,
        colWidths=[250, 190]
    )


    cover_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#123B66")
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
                    0.4,
                    colors.HexColor("#CBD5E1")
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#F8FAFC")
                    ]
                )
            ]
        )
    )


    elements.append(
        cover_table
    )


    elements.append(
        Spacer(1, 35)
    )


    elements.append(
        Paragraph(
            "Generated by AI Data Detective",
            small_style
        )
    )


    elements.append(
        PageBreak()
    )


    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    elements.append(
        Paragraph(
            "Dataset Overview",
            heading_style
        )
    )


    overview = [
        ["Metric", "Value"],
        ["Rows", str(rows)],
        ["Columns", str(columns)],
        ["Duplicates", str(duplicates)],
        ["Missing Values", str(missing_values)],
        [
            "Data Quality",
            f"{data_quality:.2f}%"
        ]
    ]


    overview_table = Table(
        overview,
        colWidths=[280, 160]
    )


    overview_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#123B66")
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
                    0.4,
                    colors.HexColor("#CBD5E1")
                ),
                (
                    "ALIGN",
                    (1, 1),
                    (1, -1),
                    "CENTER"
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#F8FAFC")
                    ]
                )
            ]
        )
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
            "Data Quality Analysis",
            heading_style
        )
    )


    quality_text = (
        f"The dataset contains {rows} rows and "
        f"{columns} columns. There are "
        f"{duplicates} duplicate rows and "
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
            "Column Information",
            heading_style
        )
    )


    column_data = [
        [
            "Column",
            "Data Type",
            "Missing",
            "Unique"
        ]
    ]


    for column in dataframe.columns:

        column_data.append(
            [
                str(column),
                str(dataframe[column].dtype),
                str(
                    int(
                        dataframe[column]
                        .isnull()
                        .sum()
                    )
                ),
                str(
                    int(
                        dataframe[column]
                        .nunique()
                    )
                )
            ]
        )


    column_table = Table(
        column_data,
        colWidths=[
            210,
            90,
            70,
            70
        ],
        repeatRows=1
    )


    column_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#123B66")
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
                    colors.HexColor("#CBD5E1")
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ]
        )
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
            "Data Preview",
            heading_style
        )
    )


    preview = (
        dataframe
        .head(8)
        .copy()
        .fillna("Missing")
        .astype(str)
    )


    preview_data = [
        [
            str(column)
            for column in preview.columns
        ]
    ]


    preview_data.extend(
        preview.values.tolist()
    )


    preview_table = Table(
        preview_data,
        repeatRows=1
    )


    preview_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#123B66")
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
                    colors.HexColor("#CBD5E1")
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    6
                )
            ]
        )
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
            "Statistical Analysis",
            heading_style
        )
    )


    numeric_df = dataframe.select_dtypes(
        include=np.number
    )


    if not numeric_df.empty:

        stats = (
            numeric_df
            .describe()
            .round(2)
        )


        stats_data = [
            ["Statistic"]
            +
            [
                str(column)
                for column in stats.columns
            ]
        ]


        for index in stats.index:

            stats_data.append(
                [
                    str(index)
                ]
                +
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
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#123B66")
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
                        colors.HexColor("#CBD5E1")
                    ),
                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, -1),
                        7
                    )
                ]
            )
        )


        elements.append(
            stats_table
        )

    else:

        elements.append(
            Paragraph(
                "No numeric columns were available.",
                normal_style
            )
        )


    elements.append(
        Spacer(1, 25)
    )


    # =====================================================
    # MISSING VALUES
    # =====================================================

    elements.append(
        Paragraph(
            "Missing Value Analysis",
            heading_style
        )
    )


    missing_data = [
        [
            "Column",
            "Missing Values"
        ]
    ]


    for column in dataframe.columns:

        missing_data.append(
            [
                str(column),
                str(
                    int(
                        dataframe[column]
                        .isnull()
                        .sum()
                    )
                )
            ]
        )


    missing_table = Table(
        missing_data,
        colWidths=[320, 120],
        repeatRows=1
    )


    missing_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#123B66")
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
                    0.4,
                    colors.HexColor("#CBD5E1")
                ),
                (
                    "ALIGN",
                    (1, 1),
                    (1, -1),
                    "CENTER"
                )
            ]
        )
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
            "Machine Learning Analysis",
            heading_style
        )
    )


    if ml_results is not None:

        ml_data = [
            ["Metric", "Result"],
            [
                "Target",
                str(
                    ml_results["target"]
                )
            ],
            [
                "Algorithm",
                str(
                    ml_results["algorithm"]
                )
            ],
            [
                "Accuracy",
                (
                    f"{ml_results['accuracy'] * 100:.2f}%"
                )
            ]
        ]


        ml_table = Table(
            ml_data,
            colWidths=[280, 160]
        )


        ml_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#123B66")
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
                        0.4,
                        colors.HexColor("#CBD5E1")
                    )
                ]
            )
        )


        elements.append(
            ml_table
        )


        elements.append(
            Spacer(1, 20)
        )


        # Confusion Matrix

        elements.append(
            Paragraph(
                "Confusion Matrix",
                heading_style
            )
        )


        classes = ml_results["classes"]

        matrix = ml_results["matrix"]


        cm_data = [
            ["Actual / Predicted"]
            +
            [
                str(c)
                for c in classes
            ]
        ]


        for i, class_name in enumerate(classes):

            cm_data.append(
                [
                    str(class_name)
                ]
                +
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
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#123B66")
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
                        0.4,
                        colors.HexColor("#CBD5E1")
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    )
                ]
            )
        )


        elements.append(
            cm_table
        )


        elements.append(
            Spacer(1, 25)
        )


        elements.append(
            Paragraph(
                "The reported accuracy should be interpreted "
                "in the context of the available dataset size "
                "and test split.",
                small_style
            )
        )


    else:

        elements.append(
            Paragraph(
                "No machine learning results were available "
                "for this dataset.",
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
            "Final Conclusion",
            heading_style
        )
    )


    conclusion = (
        f"The AI Data Detective analyzed a dataset "
        f"containing {rows} rows and {columns} columns. "
        f"The analysis identified {duplicates} duplicate "
        f"rows and {missing_values} missing values. "
        f"The calculated data quality score was "
        f"{data_quality:.2f}%."
    )


    if ml_results is not None:

        conclusion += (
            f" A {ml_results['algorithm']} model was "
            f"evaluated using {ml_results['target']} "
            f"as the target variable, achieving an "
            f"accuracy of "
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
            small_style
        )
    )


    # BUILD

    document.build(
        elements
    )


    pdf_buffer.seek(0)

    return pdf_buffer


# =========================================================
# PDF DOWNLOAD
# =========================================================

st.divider()

st.html(
    """
    <div class="section-kicker">
        DOCUMENT GENERATOR
    </div>

    <div class="section-title">
        Professional PDF Report
    </div>

    <div class="export-card">

        <div class="export-icon">
            PDF
        </div>

        <div class="export-title">
            AI Data Detective Professional Report
        </div>

        <div class="export-text">
            Generate a professional multi-page PDF containing
            dataset overview, data quality, column information,
            preview, statistics, missing values, machine learning
            evaluation and final analytical conclusion.
        </div>

    </div>
    """
)


if st.button(
    "Generate Professional PDF",
    type="primary",
    use_container_width=True
):

    with st.spinner(
        "Generating your professional report..."
    ):

        try:

            pdf_file = generate_pdf(
                df,
                ml_results
            )


            st.success(
                "Professional PDF generated successfully!"
            )


            st.download_button(
                label="Download Professional PDF",
                data=pdf_file,
                file_name=(
                    "AI_Data_Detective_"
                    "Professional_Report.pdf"
                ),
                mime="application/pdf",
                use_container_width=True
            )


        except Exception as error:

            st.error(
                f"PDF generation failed: {error}"
            )


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="footer-note">
        AI Data Detective • Automated Data Intelligence Platform
    </div>
    """
)