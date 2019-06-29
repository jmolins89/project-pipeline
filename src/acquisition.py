import pandas as pd

def open_file(file):
    print('Reading csv file...')
    return pd.read_csv(file)