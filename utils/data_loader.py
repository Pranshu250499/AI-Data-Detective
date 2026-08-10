import pandas as pd
import os


def load_dataset(file_path):
    """
    Load a CSV or Excel file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            "Dataset file not found."
        )

    if file_path.lower().endswith(".csv"):

        return pd.read_csv(file_path)

    elif file_path.lower().endswith(
        (".xlsx", ".xls")
    ):

        return pd.read_excel(file_path)

    else:

        raise ValueError(
            "Unsupported file format. "
            "Please use CSV or Excel."
        )


def save_uploaded_file(
    uploaded_file,
    folder="uploads"
):
    """
    Save an uploaded file to the uploads folder.
    """

    # Create folder if it doesn't exist
    os.makedirs(
        folder,
        exist_ok=True
    )

    # Create complete file path
    file_path = os.path.join(
        folder,
        uploaded_file.name
    )

    # Save uploaded file
    with open(
        file_path,
        "wb"
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )

    return file_path