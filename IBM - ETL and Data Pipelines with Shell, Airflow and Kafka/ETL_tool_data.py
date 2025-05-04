# 1. Library imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

# 2. DAG arguments
default_args = {
    'owner': 'Vbs-Matheus',
    'start_date': dt.datetime(2025, 5, 3),
    'email': 'course@ibm.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# 3. DAG definitions
dag = DAG('ETL_toll_data',
          description='Apache Airflow Final Assignment',
          default_args=default_args,
          schedule_interval='@daily'
)

# 4. Task definitions
unzip_data = BashOperator(
    task_id = 'unzip_data',
    bash_command = 'tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/',
    dag = dag
)

extract_data_from_csv = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = """cut -d',' -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv""",
    dag = dag
)

extract_data_from_tsv = BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = """cut -d$'\t' -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv""",
    dag = dag
)

extract_data_from_fixed_width = BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = """cut -c 60-62,64-68 /home/project/airflow/dags/finalassignment/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv""",
    dag = dag
)

consolidate_data = BashOperator(
    task_id = 'consolidate_data',
    bash_command = """
        cd /home/project/airflow/dags/finalassignment/ && \
        paste -d',' csv_data.csv tsv_data.csv fixed_width_data.csv > /home/project/airflow/dags/finalassignment/extracted_data.csv
    """,
    dag = dag
)

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = """
        cd /home/project/airflow/dags/finalassignment/ && \
        cut -d',' -f1-3 extracted_data.csv > part1.csv && \
        cut -d',' -f4 extracted_data.csv | tr 'a-z' 'A-Z' > part2.csv && \
        cut -d',' -f5-9 extracted_data.csv > part3.csv && \
        paste -d',' part1.csv part2.csv part3.csv > transformed_data.csv && \
        rm part1.csv part2.csv part3.csv
    """,
    dag = dag
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data