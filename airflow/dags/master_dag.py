from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.trigger_dag import TriggerDagRunOperator

with DAG(
    dag_id='master_dag',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    trigger_ingestion = TriggerDagRunOperator(
        task_id='trigger_ingestion',
        trigger_dag_id='ingestion_dag',
    )

    trigger_dbt = TriggerDagRunOperator(
        task_id='trigger_dbt',
        trigger_dag_id='dbt_dag',
    )

    trigger_ge = TriggerDagRunOperator(
        task_id='trigger_ge',
        trigger_dag_id='great_expectations_dag',
    )

    trigger_duckdb = TriggerDagRunOperator(
        task_id='trigger_duckdb',
        trigger_dag_id='duckdb_dag',
    )

    trigger_ingestion >> trigger_dbt >> trigger_ge >> trigger_duckdb
