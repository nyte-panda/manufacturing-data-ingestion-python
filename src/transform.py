import pandas as pd 

def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform validated production run records:

    Transformations:
    - Ensure timestamps are datetime
    - Standardize column names 
    """

    df = df.copy()

    # Standardize column names
    df.columns = [collower().strip() for col in df.columns]

    # Ensure timestamps are datetime 
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    return df
