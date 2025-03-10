from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
from sqlalchemy import create_engine

def load_data():
    df = pd.read_csv('/path/to/airflow-dbt-duckdb-medallion/data/raw/sample_data.csv') #Replace with your path.
    engine = create_engine('postgresql://your_postgres_user:your_postgres_password@localhost:5432/your_postgres_database') #Replace with your credentials.
    df.to_sql('sample_data', engine, if_exists='replace', index=False)

with DAG(
    dag_id='load_data_dag',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    load_data_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )
