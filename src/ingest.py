import pandas as pd 

from src.validate import validate_production_runs, validate_work_orders
from src.transform import transform_production_runs, transform_work_orders
from src.db import insert_production_runs


def run_pipeline():
    #load raw data
    production_run = pd.read_csv("data/raw/production_runs.csv")
    work_orders = pd.read_csv("data/raw/work_orders.csv")

    #validate data
    production_runs = validate_production_runs(production_run)
    work_orders = validate_work_orders(work_orders)

    #transform data
    production_runs = transform_production_runs(production_runs)
    work_orders = transform_work_orders(work_orders)

    #load
    insert_production_runs(production_runs)

if __name__ == "__main__":
    run_pipeline()