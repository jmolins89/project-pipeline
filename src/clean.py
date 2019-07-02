import pandas as pd
import acquisition

# data=pd.read_csv('../input/suicides.csv')
# data_clean=data.copy()
# columnstodelete=['HDI for year','country-year']


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


# delete_columns(data_clean,columnstodelete)

# data_clean.to_csv('../output/Data_clean.csv', index=False)

# print('Reading file...')
# data = acquisition.open_file('../input/suicides.csv')
# data_clean=data.copy()

# print('Deleting columns...')
# delete_columns(data_clean,['HDI for year','country-year']) 

# print('Deleting rows...')
# data_clean = delete_rows_excluding(data_clean,'country','Saint Vincent and Grenadines')
# resetindex(data_clean)
# print(data_clean)


# rows = data_clean.loc[data_clean['country']=='Saint Vincent and Grenadines']
# rowsind = list(rows.index)
# delete_rows(data_clean,rowsind)
