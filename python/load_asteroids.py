import nasapy
import os 
from datetime import datetime
import urllib
import json
import asteroids_lib
from google.cloud import bigquery
import pandas as pd

#Initialize Nasa class by creating an object:
f = open("nasa_key", "r") #key generated from nasa (https://api.nasa.gov/)
k = f.read()
nasa = nasapy.Nasa(key = k)

#initialize dataframe
asteroids_df = pd.DataFrame()

#Connect to bigquery client
client = bigquery.Client()

# Create schema in case it doesn't exist.
try:
    dataset = client.create_dataset('nasa_asteroids')
except:
    dataset = client.dataset('nasa_asteroids')
table = dataset.table('asteroids_raw')

job_config = bigquery.job.LoadJobConfig()

#Get the first json file from asteroids. Print the current quota for the nasa key
asteroids = nasa.get_asteroids()
print("Limit of calls at start of program: " + nasa.limit_remaining)

#Load first iteration of asteroids
asteroids_df = pd.concat([asteroids_lib.process_asteroids(asteroids),asteroids_df])

#Loop through the next objects while there's a next file to process
#Limiting the process of urls to 2000, nasa query hourly limit
i = 1
total_pages = asteroids["page"]["total_pages"]
print("total number of pages to process: " + str(total_pages))

while i < total_pages and  i<2000:
    try:
        url = asteroids["links"]["next"]
        response = urllib.request.urlopen(url)
        asteroids = json.loads(response.read())
        asteroids_df = pd.concat([asteroids_lib.process_asteroids(asteroids),asteroids_df])
        print("processed page number: " + str(asteroids["page"]["number"]))
        i += 1
    except KeyError:
        print("no next found")

asteroids_lib.map_columns(asteroids_df,'../csv/asteroids_col_mapping.csv')
print(asteroids_df.iloc[1])

load_job = client.load_table_from_dataframe(asteroids_df, table, job_config=job_config).result()

print('JSON file loaded to BigQuery')
