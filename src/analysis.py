import pandas as pd


def filteryear(dataframe,year):
    return dataframe[dataframe['year']>year]