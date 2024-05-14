import pendulum
from airflow import DAG
from datetime import datetime, timedelta

local_tz = pendulum.timezone("Asia/kolkata")

default_args=dict(
    start_date=datetime(2016, 1, 1, tzinfo=local_tz),
    owner='airflow',
	"start_date"=START_DATE,
)


dag = DAG(
    dag_id="sabs-dag",
    schedule_interval="*/5 * * * *",
    default_args=default_args,
    render_template_as_native_obj=True,
    access_control={"All": {"can_read", "can_edit", "can_delete"}},
    
)
print(dag.timezone)