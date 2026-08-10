import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from sklearn.metrics import (
    accuracy_score,
    mean_squared_error,
    r2_score,
    confusion_matrix,
    classification_report,
)


# ============================================================
# PREPARE DATA
# ============================================================

def prepare_data(df, target_column):
    """
    Prepare dataset for machine learning.

    Automatically:
    - removes duplicate rows
    - separates target column
    - detects numerical and categorical columns
    - fills missing numerical values with median
    - fills missing categorical values with most frequent value
    - encodes categorical features
    - encodes classification target
    """

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Make sure target exists
    if target_column not in df.columns:
        raise ValueError(
            f"Target column '{target_column}' was not found in the dataset."
        )

    # Remove rows where target is missing
    df = df.dropna(subset=[target_column])

    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # --------------------------------------------------------
    # Detect column types
    # --------------------------------------------------------

    numeric_columns = X.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = X.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    # --------------------------------------------------------
    # Numeric preprocessing
    # --------------------------------------------------------

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler()
            ),
        ]
    )

    # --------------------------------------------------------
    # Categorical preprocessing
    # --------------------------------------------------------

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                )
            ),
        ]
    )

    # --------------------------------------------------------
    # Combine preprocessing
    # --------------------------------------------------------

    transformers = []

    if numeric_columns:
        transformers.append(
            (
                "numeric",
                numeric_pipeline,
                numeric_columns
            )
        )

    if categorical_columns:
        transformers.append(
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        )

    preprocessor = ColumnTransformer(
        transformers=transformers
    )

    # --------------------------------------------------------
    # Encode target for classification
    # --------------------------------------------------------

    target_encoder = None

    if y.dtype == "object":
        target_encoder = LabelEncoder()
        y = target_encoder.fit_transform(y.astype(str))

    return (
        X,
        y,
        preprocessor,
        target_encoder,
        numeric_columns,
        categorical_columns,
    )


# ============================================================
# CLASSIFICATION
# ============================================================

def train_classification_models(
    df,
    target_column,
    test_size=0.2
):

    (
        X,
        y,
        preprocessor,
        target_encoder,
        numeric_columns,
        categorical_columns,
    ) = prepare_data(
        df,
        target_column
    )

    # Make sure there are enough samples
    if len(X) < 5:
        raise ValueError(
            "Dataset is too small for machine learning."
        )

    # Stratification only when every class has enough samples
    stratify_value = None

    class_counts = pd.Series(y).value_counts()

    if len(class_counts) > 1 and class_counts.min() >= 2:
        stratify_value = y

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42,
        stratify=stratify_value
    )

    # --------------------------------------------------------
    # Models
    # --------------------------------------------------------

    models = {

        "Logistic Regression": LogisticRegression(
            max_iter=1000
        ),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),
    }

    results = {}

    # --------------------------------------------------------
    # Train models
    # --------------------------------------------------------

    for model_name, model in models.items():

        pipeline = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "model",
                    model
                )
            ]
        )

        pipeline.fit(
            X_train,
            y_train
        )

        predictions = pipeline.predict(
            X_test
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        cm = confusion_matrix(
            y_test,
            predictions
        )

        report = classification_report(
            y_test,
            predictions,
            output_dict=True,
            zero_division=0
        )

        results[model_name] = {
            "model": pipeline,
            "accuracy": accuracy,
            "predictions": predictions,
            "actual": y_test,
            "confusion_matrix": cm,
            "classification_report": report,
            "target_encoder": target_encoder,
        }

    return results


# ============================================================
# REGRESSION
# ============================================================

def train_regression_models(
    df,
    target_column,
    test_size=0.2
):

    (
        X,
        y,
        preprocessor,
        target_encoder,
        numeric_columns,
        categorical_columns,
    ) = prepare_data(
        df,
        target_column
    )

    # Regression target must be numeric
    y = pd.to_numeric(
        y,
        errors="coerce"
    )

    valid_rows = y.notna()

    X = X.loc[valid_rows]
    y = y.loc[valid_rows]

    if len(X) < 5:
        raise ValueError(
            "Not enough valid numeric data for regression."
        )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )

    models = {

        "Decision Tree": DecisionTreeRegressor(
            random_state=42
        ),

        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ),
    }

    results = {}

    for model_name, model in models.items():

        pipeline = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "model",
                    model
                )
            ]
        )

        pipeline.fit(
            X_train,
            y_train
        )

        predictions = pipeline.predict(
            X_test
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                predictions
            )
        )

        r2 = r2_score(
            y_test,
            predictions
        )

        results[model_name] = {
            "model": pipeline,
            "rmse": rmse,
            "r2": r2,
            "predictions": predictions,
            "actual": y_test,
        }

    return results