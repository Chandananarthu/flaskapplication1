from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import os

def get_file_paths(folder_path, **kwargs):
    file_paths = {}
    try:
        # Get the list of all items in the folder
        items = os.listdir(folder_path)

        # Iterate over the items and add file paths to the dictionary
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                file_paths[item] = item_path

        # Print the number of files and their paths
        print(f"Number of files: {len(file_paths)}")
        for name, path in file_paths.items():
            print(f"{name}: {path}")

        # Push file_paths to XCom
        kwargs['ti'].xcom_push(key='file_paths', value=file_paths)

    except FileNotFoundError:
        print(f"The folder {folder_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return file_paths

def print_file_name(file_name, file_path, **kwargs):
    # This function will be called for each file to print its name and path
    print(f"File: {file_name}, Path: {file_path}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dynamic_file_tasks',
    default_args=default_args,
    description='A DAG that dynamically generates tasks for each file in a directory',
    schedule_interval=timedelta(days=1),
)

# Get file paths and push them to XCom
get_file_paths_task = PythonOperator(
    task_id='get_file_paths',
    python_callable=get_file_paths,
    op_args=['/home/chandana/airflow/dags'],  # Linux-style path for Ubuntu
    provide_context=True,  # Ensure context is provided
    dag=dag,
)

# Dynamically create tasks for each file found in the directory
def create_file_task(file_name, file_path):
    return PythonOperator(
        task_id=f'print_file_name_{file_name}',
        python_callable=print_file_name,
        op_args=[file_name, file_path],
        provide_context=True,
        dag=dag,
    )

# Retrieve file paths and create tasks
file_paths = get_file_paths('/home/chandana/airflow/dags')
for file_name, file_path in file_paths.items():
    file_task = create_file_task(file_name, file_path)
    get_file_paths_task >> file_task
