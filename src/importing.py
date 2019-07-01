import requests
import acquisition
import clean

#API usada: https://restcountries.eu/#api-endpoints-name

def apiimportlanguage(dataframe,url):
    print('Importing languages from the API...')
    print('This will take a while...')
    languages={}
    countries = list(set(dataframe['country']))
    try:
        for i in range(len(countries)):
            countries[i]=countries[i].replace(' ','%20')
        for i in countries:
            res= requests.get(url+i)
            dev=res.json()
            languages.update({i.replace('%20',' '):dev[0]['languages'][0]['name']})
    except: print('Country not found!')
    return languages

def apiimportregion(dataframe,url):
    print('Importing regions from the API...')
    print('This will take a while...')
    regions={}
    countries = list(set(dataframe['country']))
    try:
        for i in range(len(countries)):
            countries[i]=countries[i].replace(' ','%20')
        for i in countries:
            res= requests.get(url+i)
            dev=res.json()
            regions.update({i.replace('%20',' '):dev[0]['region']})
    except: print(i,':Country not found!')
    return regions

def generatelist(dataframe,column,dictionary):
    lst=[]
    for i in range(len(dataframe[column])):
        lst.append(dictionary[dataframe[column][i]])
    return lst

def add_columns(dataframe,column_name,lista):
    dataframe[column_name]=lista


# url="https://restcountries.eu/rest/v2/name/"
# print('Reading file...')
# data = acquisition.open_file('../input/suicides.csv')
# data_clean=data.copy()

# print('Deleting columns...')
# clean.delete_columns(data_clean,['HDI for year','country-year']) 

# print('Deleting rows...')
# data_clean = clean.delete_rows_excluding(data_clean,'country','Saint Vincent and Grenadines')
# data_clean = clean.resetindex(data_clean)
# languages = apiimportlanguage(data_clean,url)
# regions = apiimportregion(data_clean,url)
# listlangu=generatelist(data_clean,'country',languages)
# listreg=generatelist(data_clean,'country',regions)
# add_columns(data_clean,'Language',listlangu)
# add_columns(data_clean,'Region',listreg)
# print(data_clean)
