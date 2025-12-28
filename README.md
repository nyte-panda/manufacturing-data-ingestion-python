# Manufacturing Data Ingestion & Validation Pipeline (Python)

## Overview

This project implements a Python-based batch ingestion pipeline for a
manufacturing operations dataset. The pipeline reads raw CSV files, validates
their structure and contents, applies basic transformations, and loads clean
data into a PostgreSQL database.

The goal of this project is to demonstrate core data engineering skills such as
data ingestion, validation, transformation, and reliable database loading
using Python.

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
- Validate required fields and basic data types
- Enforce simple business rules (e.g. start time precedes end time)
- Transform data into a standardized format
- Load validated records into PostgreSQL tables
- Log or reject invalid records

---

## Architecture

Raw CSV Files → Python (Validation & Transformation) → PostgreSQL

---

## Project Structure

manufacturing-data-ingestion-python/
├── data/
│ ├── raw/ # Incoming CSV files
│ └── processed/ # Cleaned / validated outputs
├── src/
│ ├── ingest.py # Pipeline orchestration
│ ├── validate.py # Data validation logic
│ ├── transform.py # Data transformation logic
│ └── db.py # Database connection and loading
├── sql/
│ └── schema.sql
└── requirements.txt


---

## Scope

This project intentionally focuses on batch ingestion and data quality checks
using Python. Workflow orchestration, streaming, and cloud infrastructure are
out of scope and reserved for a future anchor project.
