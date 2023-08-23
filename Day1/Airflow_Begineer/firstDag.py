from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import datetime as dt

def printWorld():
    print('World')

default_args = {
    'owner':'VivekPatel',
    'start_date': dt.datetime(2023, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('airflow_beginner',
            default_args=default_args,
            schedule_interval='0 * * * *',
        ) as dag:
    print_hello = BashOperator(task_id='print_hello',
                                bash_command = 'echo "Hello"')
    sleep = BashOperator(task_id ='sleep',
                        bash_command='sleep 5')
    print_world = PythonOperator (task_id= 'print_world',
                            python_callable=printWorld)
    
print_hello >> sleep >> print_world