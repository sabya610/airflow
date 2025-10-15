from datetime import datetime
from airflow import DAG
from airflow.providers.sftp.operators.sftp import SFTPOperator

# Define the DAG
with DAG(
    dag_id="aravind_test_sftp_dag",
    description="A test DAG to validate connect to SFTP Server",
    schedule_interval=None,  # Manual trigger
    start_date=datetime(2025, 10, 1),
    catchup=False,
    tags=["test"],
    access_control={"All": {"can_read", "can_edit", "can_delete"}}
) as dag:
    task_pull_file = SFTPOperator(
        task_id="test_sftp",
        ssh_conn_id="airflow_sftp",
        local_filepath="shared/data/raw/gts/SPLAUD",
        remote_filepath="/sapmnt/GGP/SPLAUD_DATA",
        operation="get",
        create_intermediate_dirs=True,
    )

    task_pull_file
