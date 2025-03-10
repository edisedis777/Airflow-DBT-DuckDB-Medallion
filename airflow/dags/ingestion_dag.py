from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='ingestion_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    task_echo = BashOperator(
        task_id='echo_hello',
        bash_command='echo "Hello, Airflow!"',
    )
