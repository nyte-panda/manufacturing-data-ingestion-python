# Manufacturing Data Ingestion & Validation Pipeline (Python)

## Overview

This project implements a Python-based batch ingestion pipeline for a
manufacturing operations dataset. The pipeline reads raw CSV files, validates
their structure and contents, applies basic transformations, and loads clean
data into a PostgreSQL database.

The goal of this project is to demonstrate core data engineering skills such as
data ingestion, validation, transformation, and reliable database loading using
Python.

---

## Problem Statement

Manufacturing data often arrives as raw CSV files that may contain missing
values, invalid timestamps, or inconsistent formats. Before this data can be
used for analytics, it must be validated, cleaned, and loaded in a controlled
and repeatable way.

This project focuses on building that ingestion layer.

---

## Pipeline Responsibilities

The pipeline performs the following steps:

- Read raw CSV files from disk
- Validate required fields and basic data integrity rules
- Enforce simple business rules (e.g. start time precedes end time)
- Transform data into a standardized format
- Load validated records into PostgreSQL tables

---

## Architecture

Raw CSV Files → Python (Validation & Transformation) → PostgreSQL

---

## Project Structure


```
manufacturing-data-ingestion-python/
├── data/
│   ├── raw/           # Incoming CSV files
│   └── processed/     # Cleaned / validated outputs
├── src/
│   ├── ingest.py      # Pipeline orchestration
│   ├── validate.py    # Data validation logic
│   ├── transform.py   # Data transformation logic
│   └── db.py          # Database connection and loading
├── sql/
│   └── schema.sql
└── requirements.txt
```

---

## How to Run

1. Ensure PostgreSQL is running locally and the target schema exists.
2. Activate a virtual environment and install dependencies:
  ```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m src.ingest