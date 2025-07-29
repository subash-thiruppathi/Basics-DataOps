# Minimal DataOps ETL Project

This project demonstrates a minimal DataOps ETL pipeline using Apache Airflow.

## Setup Guide

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create and activate a virtual environment:

```bash
python3 -m venv airflow-env
source airflow-env/bin/activate
```

### 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Initialize the Airflow database:

```bash
airflow db init
```

### 5. Create an Airflow user:

```bash
airflow users create \
    --username admin \
    --firstname Your \
    --lastname Name \
    --role Admin \
    --email your.email@example.com
```

### 6. Start Airflow:

For local development, the `standalone` command will start the webserver, scheduler, and database for you:

```bash
airflow standalone
```
This will also create an admin user with the username `admin` and password `admin`.

### 7. Access the Airflow UI:

Open your web browser and go to `http://localhost:8080`.

## Project Structure

```
.airflow-project/
├── airflow-env/
├── data.csv
├── minimal_dataops_etl.py
├── sales_dashboard.py
├── requirements.txt
└── README.md
```

- `airflow-env/`: Python virtual environment.
- `data.csv`: Raw sales data.
- `minimal_dataops_etl.py`: The Airflow DAG for the ETL pipeline.
- `sales_dashboard.py`: A Dash application to visualize the transformed data.
- `requirements.txt`: Project dependencies.
- `README.md`: This file.

## How to Use

### ETL Pipeline

The ETL pipeline is defined in `minimal_dataops_etl.py` and consists of three tasks:

1.  **Extract**: Reads data from `data.csv`.
2.  **Transform**: Calculates gross price, discount amount, and net revenue.
3.  **Load**: Saves the transformed data to `output/transformed_sales.csv`.

To run the ETL pipeline, enable the `minimal_dataops_etl-3` DAG in the Airflow UI and trigger a new run.

### Sales Dashboard

The sales dashboard is a Dash application that visualizes the transformed sales data. To run the dashboard, execute the following command:

```bash
python sales_dashboard.py
```

Then, open your web browser and go to `http://127.0.0.1:8050/`.

## Data Schema

The `data.csv` file has the following columns:

- `id`: Transaction ID
- `date`: Date of the transaction
- `customer`: Customer name
- `product`: Product name
- `quantity`: Quantity of the product sold
- `price`: Price per unit of the product
- `region`: Sales region
- `discount`: Discount applied to the transaction



