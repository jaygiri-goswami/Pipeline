from operator import index
import pandas as pd
from google.cloud import bigquery
import json
import csv
import os
# from google.oauth2 import service_account

gcp_project = 'robust-seat-338513'
bd_dataset = 'dataframe_operation_perform'

credentials_path = '/home/jaygirigoswami/Downloads/robust-seat-338513-e1cb147a2181.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table="robust-seat-338513.dataframe_operation_perform.prti"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)
table.time_partitioning = bigquery.TimePartitioning(field='__time')

with open("/home/jaygirigoswami/newproj/workspace/meet.csv", "rb") as source_file:
    job = client.load_table_from_file(source_file, "robust-seat-338513.dataframe_operation_perform.prti" , job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table("robust-seat-338513.dataframe_operation_perform.prti")  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), "robust-seat-338513.dataframe_operation_perform.prti"
    )
)