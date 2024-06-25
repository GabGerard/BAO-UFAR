# src/create_database.py
import pandas as pd

def create_database(objects, output_file='data/processed/objects.csv'):
    df = pd.DataFrame(objects)
    df.to_csv(output_file, index=False)
