from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", # 분, 시, 일, 월, 요일, 
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),  # DAG이 언제부터 돌 지
    catchup=False,  # 시작일 전 누락 구간을 모두 다 돌릴 것이냐, 근데 순서대로 돌지 않고 한꺼번에 돌아감, 일반적으로 False로 둠
    tags=["example", "example2"], # Optional
) as dag:
    # Task 객체 명
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami", # 어떤 쉘스크립트를 수행할 것이냐
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    # Task들의 수행 순서(관계) 설정
    bash_t1 >> bash_t2