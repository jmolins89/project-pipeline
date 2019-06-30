import pandas as pd
import requests
import acquisition
import clean
import importing
import analysis

def read_file(file):
    data = acquisition.open_file(file)
    return data


def cleaning(data):
    data_ok=data.copy()
    clean.delete_columns(data_ok,['HDI for year','country-year']) 
    data_ok = clean.delete_rows_excluding(data_ok,'country','Saint Vincent and Grenadines')
    data_ok = clean.resetindex(data_ok)
    return data_ok

def impor(data,url):
    languages = importing.apiimportlanguage(data,url)
    regions = importing.apiimportregion(data,url)
    listlangu=importing.generatelist(data,'country',languages)
    listreg=importing.generatelist(data,'country',regions)
    importing.add_columns(data,'Language',listlangu)
    importing.add_columns(data,'Region',listreg)
    return data

def analyze(data):
    df2 = analysis.genderSex(data_clean)
    graph = analysis.plotingGenerSex(df2)
    return df2, graph


def main():
    data = read_file('../input/suicides.csv')
    data_clean = cleaning(data)
    data_imported = impor(data_clean,"https://restcountries.eu/rest/v2/name/")
    d_analyze, graph = analyze(data_imported)
    #report(d_analyze, figure)

if __name__ == "__main__":
    main()



