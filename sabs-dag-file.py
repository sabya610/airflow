import pendulum
from airflow import DAG
from datetime import datetime, timedelta

local_tz = pendulum.timezone("Asia/Kolkata")
start_date=datetime(2016, 1, 1, tzinfo=local_tz)
default_args=(
    "start_date":start_date,
    "owner":"airflow",
    
)


dag = DAG(
    dag_id="sabs-dag",
    schedule_interval="*/5 * * * *",
    default_args=default_args,
    render_template_as_native_obj=True,
    access_control={"All": {"can_read", "can_edit", "can_delete"}},
    
)
print(dag.timezone)
