import pandas as pd
from google.cloud import bigquery
import os
from io import StringIO
import json
import numpy as np

# gcp_project = 'robust-seat-338513'
# bd_dataset = 'dataframe_operation_perform'


credentials_path = '/home/jaygirigoswami/Downloads/robust-seat-338513-e1cb147a2181.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

project_id = "robust-seat-338513"
dataset_id = "robust-seat-338513.dataframe_operation_perform"
table_id = "robust-seat-338513.dataframe_operation_perform.subscription"

client  = bigquery.Client()
dataset  = client.dataset(dataset_id)
table = dataset.table(table_id)

x="/home/jaygirigoswami/Downloads/bq-results-20220406-071643-1649229436562.json"
df=pd.read_json("/home/jaygirigoswami/Downloads/bq-results-20220406-071643-1649229436562.json")
#print(df.head(2))
json_data=df.to_json(orient = 'records', lines = True)
# print(json_data)
in_json=StringIO(json_data)
# z=in_json.read(in_json)
# print(z)


job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    autodetect=True
)

job = client.load_table_from_file(in_json, table_id, job_config=job_config)

job.result() # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))