import pandas as pd

def transform_production_runs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform validated production run records:

    Transformations:
    - Ensure timestamps are datetime
    - Standardize column names 
    """

    df = df.copy()

    # Standardize column names
    df.columns = [col.lower().strip() for col in df.columns]

    # Ensure timestamps are datetime 
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    return df


def transform_work_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform validated work order records:

    Transformations:
    - Standardize column names
    - Ensure scheduled date is datetime
    """
    df = df.copy()

    # Standardize column names
    df.columns = [col.lower().strip() for col in df.columns]

    # Ensure scheduled date is datetime
    if "scheduled_date" in df.columns:
        df["scheduled_date"] = pd.to_datetime(df["scheduled_date"])

    return df
