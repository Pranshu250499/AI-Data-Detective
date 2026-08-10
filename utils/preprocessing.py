import pandas as pd


def get_missing_values(df):
    return df.isnull().sum()


def get_duplicate_count(df):
    return int(df.duplicated().sum())


def get_numeric_columns(df):
    return df.select_dtypes(
        include="number"
    ).columns.tolist()


def get_categorical_columns(df):
    return df.select_dtypes(
        exclude="number"
    ).columns.tolist()


def remove_duplicates(df):
    return df.drop_duplicates()


def fill_missing_numeric(df):
    df = df.copy()

    for column in df.columns:

        # Only process genuinely numeric columns
        if pd.api.types.is_numeric_dtype(df[column]):

            if df[column].isnull().any():
                median_value = df[column].median()

                df[column] = df[column].fillna(
                    median_value
                )

    return df

def fill_missing_categorical(df):

    df = df.copy()

    categorical_columns = get_categorical_columns(df)

    for column in categorical_columns:

        if df[column].isnull().any():

            mode = df[column].mode()

            if not mode.empty:

                df[column] = df[column].fillna(
                    mode.iloc[0]
                )

    return df


def clean_dataset(df):

    df = remove_duplicates(df)

    df = fill_missing_numeric(df)

    df = fill_missing_categorical(df)

    return df