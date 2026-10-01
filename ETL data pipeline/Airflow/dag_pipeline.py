
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add ETL folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../etl')))

from etl_pipeline import run_etl

default_args = {
    'owner': 'naveen',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='sales_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl
    )

    etl_task

