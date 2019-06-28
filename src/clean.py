import pandas as pd
# data=pd.read_csv('../input/suicides.csv')
# data_clean=data.copy()
# columnstodelete=['HDI for year','country-year']

def delete_columns(dataframe,lista):
    for i in lista:
        dataframe.drop([i], axis=1, inplace = True)

def delete_rows_excluding(dataframe,column,condition):
    dataframe=dataframe[dataframe[column] != condition]
    dataframe.reset_index()
    return dataframe

# delete_columns(data_clean,columnstodelete)

# data_clean.to_csv('../output/Data_clean.csv', index=False)