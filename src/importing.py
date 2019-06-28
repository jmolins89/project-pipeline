import requests


def apiimportlanguage(dataframe,url):
    languages={}
    countries = list(set(dataframe['country']))
    try:
        for i in range(len(countries)):
            countries[i]=countries[i].replace(' ','%20')
        for i in countries[1:]:
            res= requests.get(url+i)
            dev=res.json()
            languages.update({i.replace('%20',' '):dev[0]['languages'][0]['name']})
    except: print('Country not found!')
    return languages

def apiimportregion(dataframe,url):
    regions={}
    countries = list(set(dataframe['country']))
    try:
        for i in range(len(countries)):
            countries[i]=countries[i].replace(' ','%20')
        for i in countries[1:]:
            res= requests.get(url+i)
            dev=res.json()
            languages.update({i.replace('%20',' '):dev[0]['region']})
    except: print('Country not found!')
    return regions

