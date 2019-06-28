import pandas as pd
import requests

from acquisition import *
from clean import *
from importing import *

def read_file(file):
    data = acquisition.open_file(file)
    return data


def cleaning(data):
    data_clean = clean.delete_columns(data,['HDI for year','country-year'])
    data_clean = clean.delete_rows_excluding(data_clean,'country','Saint Vincent and Grenadines')
    return data_clean

def importing(data):
    languages = importing.apiimportregion(dataframe,url)



