from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def etl():
    import yfinance as yf
    import pandas as pd
    import os

    # --- Extract ---
    symbol = 'AAPL'
    data = yf.download(symbol, period="6mo", interval="1d")  # Last 6 months

    # --- Transform ---
    if data.empty:
        print("No data returned from Yahoo Finance")
        return
    data = data.reset_index()
    data = data.rename(columns={
        'Date': 'date',
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Volume': 'volume',
        'Adj Close': 'adj_close'
    })

    # --- Load ---
    output_dir = '/home/finstein-emp/Desktop/try/airflow-project/output'
    os.makedirs(output_dir, exist_ok=True)
    out_path = f'{output_dir}/stock_data.csv'
    data.to_csv(out_path, index=False)
    print(f"Saved stock data: {out_path}")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 7, 31),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="finance_etl_dag",
    default_args=default_args,
    description="Yahoo Finance Data ETL Pipeline",
    schedule="@daily",
    catchup=False,
    tags=["finance", "dataops", "etl"],
) as dag:

    etl_task = PythonOperator(
        task_id="finance_etl",
        python_callable=etl,
    )
