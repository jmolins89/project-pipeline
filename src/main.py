import pandas as pd
import requests

from acquisition import *
from clean import *

def read_file(file):
    data=acquisition.load_data(file)
    return data


def cleaning(data):
    data_clean= clean.delete_columns(data,['HDI for year','country-year'])
    return data_clean


