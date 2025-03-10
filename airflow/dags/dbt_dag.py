from airflow import DAG
from airflow.utils.dates import days_ago
from dbt_airflow_factory.operators.dbt import DbtRunOperator, DbtTestOperator

with DAG(
    dag_id='dbt_dag',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    dbt_run = DbtRunOperator(
        task_id='dbt_run',
        project_dir='/path/to/airflow-dbt-duckdb-medallion/dbt/', #Replace with your path
        profiles_dir='/path/to/airflow-dbt-duckdb-medallion/dbt/', #Replace with your path
    )

    dbt_test = DbtTestOperator(
        task_id='dbt_test',
        project_dir='/path/to/airflow-dbt-duckdb-medallion/dbt/', #Replace with your path
        profiles_dir='/path/to/airflow-dbt-duckdb-medallion/dbt/', #Replace with your path
    )

    dbt_run >> dbt_test
