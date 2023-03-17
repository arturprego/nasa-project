import nasapy
import os 
from datetime import datetime
import urllib
import json
import asteroids_lib
from google.cloud import bigquery
import pandas as pd

#Initialize Nasa class by creating an object:
f = open("nasa_key", "r")  #key generated from nasa (https://api.nasa.gov/)
k = f.read()
nasa = nasapy.Nasa(key = k)

#Connect to bigquery client and initialize table
client = bigquery.Client()
dataset_id = 'nasa_asteroids'
dataset = client.create_dataset(dataset_id, exists_ok=True)
table_id = 'asteroids_raw'
table_ref = dataset.table(table_id)

#Get the first json file from asteroids. Print the current quota for the nasa key
asteroids = nasa.get_asteroids()
print("Limit of calls at start of program: " + nasa.limit_remaining)

#Load first page of asteroids
asteroids_df = pd.DataFrame()
asteroids_df = pd.concat([asteroids_lib.process_asteroids(asteroids),asteroids_df])

#Loop through the next objects while there's a next file to process
#Limiting the process of urls to 2000, nasa query hourly limit
i = 1
i_max = 2000

total_pages = asteroids["page"]["total_pages"]
print("total number of pages to process: " + str(total_pages))

while i < total_pages and  i<i_max:
    try:
        url = asteroids["links"]["next"]
        response = urllib.request.urlopen(url)
        asteroids = json.loads(response.read())
        asteroids_df = pd.concat([asteroids_lib.process_asteroids(asteroids),asteroids_df])
        print("processed page number: " + str(asteroids["page"]["number"]))
        i += 1
    except KeyError:
        print("no next found")

# map column names
asteroids_lib.map_columns(asteroids_df,'asteroids_col_mapping.csv')

# load data into database
job_config = bigquery.job.LoadJobConfig()
load_job = client.load_table_from_dataframe(asteroids_df, table_ref, job_config=job_config).result()

print(str(len(asteroids_df)) + ' rows loaded into ' + table_id)
