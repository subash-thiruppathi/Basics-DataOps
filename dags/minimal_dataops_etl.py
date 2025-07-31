from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def extract():
    """
    Extract data from a CSV file and return as a list of dicts.
    """
    import pandas as pd
    data = pd.read_csv('/home/finstein-emp/airflow/data.csv')
    print(f"Extracted:\n{data.head()}")
    # Convert for XCom transport
    return data.to_dict(orient='records')

def transform(ti):
    data = ti.xcom_pull(task_ids='extract_task')
    if not data:
        print("No data pulled from extract_task.")
        return []
    transformed = []
    for row in data:
        gross_price = float(row['quantity']) * float(row['price'])
        discount_amount = gross_price * float(row['discount'])
        net_revenue = gross_price - discount_amount
        row['gross_price'] = gross_price
        row['discount_amount'] = discount_amount
        row['net_revenue'] = net_revenue
        transformed.append(row)
    print(f"Transformed (first 2 rows): {transformed[:2]}")
    return transformed


def load(ti):
    data = ti.xcom_pull(task_ids='transform_task')
    import pandas as pd
    df = pd.DataFrame(data)
    output_path = '/home/finstein-emp/airflow/output/transformed_sales.csv'
    df.to_csv(output_path, index=False)
    print(f"Loaded data saved to {output_path} (total rows: {len(df)})")


default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 7, 29),  # Use a fixed date in the past
}

with DAG(
    dag_id="minimal_dataops_etl-3",
    default_args=default_args,
    description="A minimal DataOps ETL pipeline",
    schedule="@daily",
    catchup=False,
    tags=["example", "dataops", "etl"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
