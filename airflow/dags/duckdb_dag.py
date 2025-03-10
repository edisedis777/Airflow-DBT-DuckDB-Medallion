from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import subprocess

def run_duckdb_script():
    subprocess.run(['python', '/path/to/airflow-dbt-duckdb-medallion/duckdb/scripts/analyze_gold_data.py'], check=True) #Replace with your path

with DAG(
    dag_id='duckdb_dag',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    duckdb_task = PythonOperator(
        task_id='run_duckdb_analysis',
        python_callable=run_duckdb_script,
    )
