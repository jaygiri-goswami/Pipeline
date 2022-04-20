import pandas as pd
from google.cloud import bigquery
import json
import csv
import os

gcp_project = 'robust-seat-338513'
bd_dataset = 'dataframe_operation_perform'

credentials_path = '/home/jaygirigoswami/Downloads/robust-seat-338513-e1cb147a2181.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# df=pd.read_json("/home/jaygirigoswami/Downloads/proj_ls.json")
# # print(df.head(2))

# with open('/home/jaygirigoswami/Downloads/proj_ls.json') as json_file:
#     data = json.load(json_file)
 
# employee_data = data['emp_details']

# data_file = open('data_file.csv', 'w')

# csv_writer = csv.writer(data_file)

# count = 0
 
# for emp in employee_data:
#     if count == 0:
 
#         # Writing headers of CSV file
#         header = emp.keys()
#         csv_writer.writerow(header)
#         count += 1
 
#     # Writing data of CSV file
#     csv_writer.writerow(emp.values())
 
# data_file.close()
with open('/home/jaygirigoswami/Downloads/proj_ls.json') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('csvfile.csv',index=False)