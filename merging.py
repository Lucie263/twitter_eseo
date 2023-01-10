import os
import pandas as pd
import glob

# Dossier ou son ranger les fichiers json (a remplir)
json_dir = 'json_files_dir'

json_pattern = os.path.join(json_dir, '*.json')
files = glob.glob(json_pattern)

# Création du DataFrame avec toutes les informations
total_df = pd.DataFrame()
for file in files:
    df = pd.read_json(file)
    total_df = pd.concat([total_df, df], ignore_index=True)

# Si besoin d'avoir un fichier json avec tout
# total_df.to_json('total_fichiers.json')