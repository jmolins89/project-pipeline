import requests

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

def impor(data,url):
    languages = apiimportlanguage(data,url)
    regions = apiimportregion(data,url)
    listlangu= generatelist(data,'country',languages)
    listreg= generatelist(data,'country',regions)
    add_columns(data,'Language',listlangu)
    add_columns(data,'Region',listreg)
    return data