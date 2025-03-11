# Airflow-dbt-DuckDB-Medallion
[![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![dbt version](https://img.shields.io/badge/dbt_version-1.0.0-blue)
![Made with DuckDB](https://img.shields.io/badge/Made%20with-DuckDB-1f425f.svg)



[![Markdown](https://img.shields.io/badge/Markdown-%23000000.svg?logo=markdown&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project implements a cost-optimized data platform using Apache Airflow for orchestration, dbt for data transformations, and DuckDB for ad-hoc analysis, following a Medallion Architecture. It focuses on streamlining data ingestion, ensuring data quality, and enabling efficient analytics.

## Project Overview

This repository provides a framework for building a modern data pipeline that leverages open-source tools to minimize cloud compute costs while maintaining high data quality and accessibility.

**Key Features:**

* **Data Ingestion & Orchestration:**
    * Airflow DAGs automate data ingestion from various sources (e.g., CSV, Google Sheets, databases).
    * Scheduled and dependency-managed data pipelines.
* **Data Transformation & Quality:**
    * dbt models define modular, tested, and version-controlled data transformations using SQL.
    * Great Expectations ensures data quality through comprehensive validation checks at each stage.
    * dbt documentation for data lineage.
* **Ad-Hoc Analysis:**
    * DuckDB enables fast, interactive ad-hoc analysis and rapid prototyping, especially for smaller datasets.
* **Medallion Architecture:**
    * Bronze, Silver, and Gold layers organize data for optimal consumption.
    * Optimized Gold layer for specific data access patterns to reduce query scan times.

## Project Structure
```
airflow-dbt-duckdb-medallion/
├── airflow/
│   ├── dags/
│   │   └── ingestion_dag.py
│   │   └── dbt_dag.py
│   │   └── great_expectations_dag.py
│   │   └── duckdb_dag.py
│   │   └── master_dag.py
│   ├── plugins/
│   └── config/
├── dbt/
│   ├── models/
│   │   ├── bronze/
│   │   ├── silver/
│   │   └── gold/
│   ├── tests/
│   ├── macros/
│   └── profiles.yml
├── duckdb/
│   ├── scripts/
│   └── data/
├── great_expectations/
│   └── checkpoints/
├── data/
│   └── raw/
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd airflow-dbt-duckdb-medallion
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Airflow:**
    * Initialize the Airflow database: `airflow db init`
    * Start the Airflow webserver: `airflow webserver -p 8080`
    * Start the Airflow scheduler: `airflow scheduler`
    * Access the Airflow UI: `http://localhost:8080`

5.  **Configure dbt:**
    * Navigate to the `dbt/` directory: `cd dbt`
    * Run `dbt init` and follow the prompts.
    * Configure `profiles.yml` with your database connection details.
    * Run `dbt debug` to verify the configuration.
    * Run `dbt run` to execute dbt models.
    * Run `dbt test` to execute dbt tests.
    * Run `dbt docs generate` and `dbt docs serve` to generate dbt documentation.

6.  **Configure Great Expectations:**
    * Navigate to the `great_expectations/` directory: `cd ../great_expectations`
    * Run `great_expectations init` and follow the prompts.
    * Configure a data source.
    * Create expectations and checkpoints.
    * Run checkpoints: `great_expectations checkpoint run <checkpoint_name>`

7.  **Configure DuckDB:**
    * Place your duckdb scripts in the duckdb/scripts folder.
    * Place data to be used by duckdb in the duckdb/data folder.

8.  **Configure Database:**
    * The project uses PostgreSQL as a database. Make sure you have a postgres instance running, and the correct credentials in the dbt profile file, and the python scripts.

9.  **Run Airflow DAGs:**
    * Trigger the `master_dag` in the Airflow UI to run the entire pipeline.

## Usage

* Modify the Airflow DAGs in `airflow/dags/` to ingest data from your sources.
* Define data transformations in the dbt models located in `dbt/models/`.
* Create data quality checks using Great Expectations.
* Write DuckDB scripts for ad-hoc analysis in `duckdb/scripts/`.
* Customize the Medallion Architecture by modifying the dbt models in the Bronze, Silver, and Gold directories.
* Use Airflow variables to store configuration settings.

## Dependencies

* Apache Airflow
* dbt (dbt-core)
* DuckDB
* Great Expectations
* pandas
* SQLAlchemy
* dbt-airflow-factory
* great-expectations-airflow

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements.

## License

This project is open-source and available under the MIT License.
