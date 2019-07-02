import pandas as pd

def delete_columns(dataframe,lista):
    try:
        print('Deleting columns...')
        for i in lista:
            dataframe.drop([i], axis=1, inplace = True)
    except: print('Error while deleting columns')

def delete_rows(dataframe,lista):
    for i in lista:
        dataframe.drop([i], axis=0, inplace = True)

def delete_rows_excluding(dataframe,column,condition):
    try:
        print('Deleting rows...')
        dataframe = dataframe[dataframe[column] != condition]
        return dataframe
    except: print('Error while deleting rows')

def changing_names(dataframe):
        for i in dataframe['country']:
                if i=='United States':
                        dataframe['country'][i]='United States of America'
                else: continue
        return dataframe

def resetindex(dataframe):
    dataframe = dataframe.reset_index(drop=True)
    return dataframe

def cleaning(data):
    data_ok=data.copy()
    delete_columns(data_ok,['HDI for year','country-year']) 
    data_ok = delete_rows_excluding(data_ok,'country','Saint Vincent and Grenadines')
    data_ok_ok= changing_names(data_ok)
    data_ok_ok = resetindex(data_ok_ok)
    return data_ok_ok
