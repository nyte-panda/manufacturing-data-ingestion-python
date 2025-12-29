import pandas as pd 

def validate_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    """
    Validate production run records:\
    
Rules: 
- Required fields must not be null
- end-time must be after start-time


Returns:
- Valid records only
"""
    required_columns = [
        "run_id",
        "machine_id",
        "operator_id",
        "start_time",
        "end_time",
    ]

    # Drop rows with missing reuqired fields

    df = df.dropna(subset=required_columns)

    # Convert timestamps

    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    # Enforce time validity

    df = df[df["end_time"] > df["start_time"]]

    return df

