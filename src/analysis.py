import pandas as pd
import matplotlib.pyplot as plt

def filteryear(dataframe,year):
    return dataframe[dataframe['year']>year]

