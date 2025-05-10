FROM apache/airflow:3.0.0

COPY requirements.txt /opt/airflow

USER root

RUN apt-get update && apt-get install -y gcc python3

USER airflow 
RUN pip install uv
RUN uv pip install --no-cache-dir -r /opt/airflow/requirements.txt
RUN uv pip install psycopg2-binary
