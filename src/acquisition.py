import pandas as pd

def open_file(file):
    print('Reading csv file...')
    data = pd.read_csv(file)
    return data
