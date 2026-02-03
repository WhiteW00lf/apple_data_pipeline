from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from google.cloud import storage
from airflow.exceptions import AirflowException,AirflowSkipException
from dotenv import load_dotenv
import os
import requests


BUCKET_NAME = 'apple-data-raw'
load_dotenv()
key = os.getenv('API_KEY')

def fetch_raw_data_task(execution_date, **kwargs):
    print("🔥 FUNCTION STARTED 🔥")

    end_date = execution_date.strftime('%Y-%m-%d')
    start_date = (execution_date - timedelta(days=1)).strftime('%Y-%m-%d')
    raw_file = f"raw/date={start_date}/aapl.csv"
    client = storage.Client('market-data-analytics-486307')
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(raw_file)
    

    if blob.exists():
        raise AirflowSkipException(f"File {raw_file} already exists in bucket {BUCKET_NAME}")


    url = f"https://api.twelvedata.com/time_series?apikey={key}&interval=1day&start_date={start_date}&end_date={end_date}&format=CSV&type=stock&exchange=NASDAQ&country=US&symbol=AAPL&timezone=exchange"
    print("Calling TwelveData API:", url)

    response = requests.get(url,timeout=30)
    response.raise_for_status()

    print("Response received, length:", len(response.text))


    if response.status_code == 200:
        blob.upload_from_string(response.text,content_type='text/csv')
        print(f"File {raw_file} uploaded to bucket {BUCKET_NAME}")
    else:
        raise AirflowException(f"Failed to fetch data from API")

    




default_args = {
    'owner': 'data-eng',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='fetch_raw_data',
    default_args=default_args,
    start_date=datetime(2026, 2, 3),
    schedule='@daily',
    catchup=False
) as dag:

    fetch_raw_data = PythonOperator(
    task_id='fetch_raw_data',
    python_callable=fetch_raw_data_task,
    dag=dag
)






