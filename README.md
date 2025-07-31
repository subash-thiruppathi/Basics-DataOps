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

### 4. Set Up Airflow Environment

This project uses a self-contained Airflow environment. Before running any Airflow commands, you must set the `AIRFLOW_HOME` environment variable to the `airflow` directory within the project:

```bash
export AIRFLOW_HOME=$(pwd)/airflow
```

This ensures that Airflow's configuration, logs, and DAGs are all managed within this project, preventing conflicts with other projects.

### 5. Initialize the Airflow Database

With the `AIRFLOW_HOME` variable set, initialize the database:

```bash
airflow db migrate
```

This will create `airflow.cfg` and `airflow.db` in your `airflow` directory.

### 6. Start Airflow

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
├── airflow/
│   ├── airflow.cfg
│   ├── airflow.db
│   ├── logs/
│   └── webserver_config.py
├── dags/
│   └── minimal_dataops_etl.py
├── airflow-env/
├── data.csv
├── sales_dashboard.py
├── requirements.txt
└── README.md
```

- `airflow/`: This folder contains all the Airflow configurations for the project.
- `dags/`: This folder contains all the Airflow DAGs for the project.
  - `minimal_dataops_etl.py`: An example Airflow DAG for the ETL pipeline.
- `airflow-env/`: Python virtual environment.
- `data.csv`: Raw sales data.
- `sales_dashboard.py`: A Dash application to visualize the transformed data.
- `requirements.txt`: Project dependencies.
- `README.md`: This file.

## How to Use

### ETL Pipeline

The ETL pipelines are defined as Python scripts in the `dags/` folder. Airflow will automatically detect any valid DAGs in this directory.

The example ETL pipeline, `minimal_dataops_etl.py`, consists of three tasks:

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



