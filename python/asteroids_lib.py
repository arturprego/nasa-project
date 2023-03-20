#Process all asteroids in json file
import json
import pandas as pd
import csv

def process_asteroids(asteroids):
    return pd.DataFrame.from_dict(pd.json_normalize(asteroids["near_earth_objects"]), orient='columns')

def map_columns(asteroids, map_file):
    with open(map_file, newline='') as csvfile:
        map_cols_file = csv.reader(csvfile)
        for row in map_cols_file:
            asteroids.rename({row[0]: row[1]}, axis='columns', inplace=True)
