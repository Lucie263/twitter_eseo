"""
This script merges json files stored in a directory into a Panda DataFrame
The dataFrame can then be used to analyse data
Author: Lucie
Created on: 2024-01-10
Updated on:
"""
import os
import pandas as pd
import glob

# File where the json files are stored
json_dir = 'json_files_dir'

json_pattern = os.path.join(json_dir, '*.json')
files = glob.glob(json_pattern)

# Creation of a DataFrame
total_df = pd.DataFrame()
for file in files:
    df = pd.read_json(file)
    total_df = pd.concat([total_df, df], ignore_index=True)

# If needed to have a json file
total_df.to_json('total_fichiers_avant.json')