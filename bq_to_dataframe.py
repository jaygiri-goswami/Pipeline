from google.cloud import bigquery
import os

project_id = "robust-seat-338513"

credentials_path = '/home/jaygirigoswami/Downloads/robust-seat-338513-e1cb147a2181.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

bqclient = bigquery.Client()

# Download a table.
table = bigquery.TableReference.from_string("robust-seat-338513.dataframe_operation_perform.coins_architecture_project")
rows = bqclient.list_rows(
    table, 
    selected_fields=[
        bigquery.SchemaField("clientId", "STRING"),
        bigquery.SchemaField("coins", "INTEGER"),
    ],
)
dataframe = rows.to_dataframe(
    # Optionally, explicitly request to use the BigQuery Storage API. As of
    # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
    # API is used by default.
    create_bqstorage_client=True,
)

# dataframe.query(clientId=="983347468.1643905916",inplace=True)

print(dataframe)