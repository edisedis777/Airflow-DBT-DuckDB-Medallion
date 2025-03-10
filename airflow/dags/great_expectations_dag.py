from airflow import DAG
from airflow.utils.dates import days_ago
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator

with DAG(
    dag_id='great_expectations_dag',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    ge_task = GreatExpectationsOperator(
        task_id='run_ge_checkpoint',
        checkpoint_name='<your_checkpoint_name>', #Replace with your checkpoint name
        data_context_root_dir='/path/to/airflow-dbt-duckdb-medallion/great_expectations/', #Replace with your path
    )
