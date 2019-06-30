import argparse
import os
import requests
import acquisition
import clean
import importing
import analysis
import presentation
import sending

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

def filtering(data,year):
    y=int(year)
    df = analysis.filteryear(data,y)
    return df

def analyze(data):
    df2 = analysis.genderSex(data)
    path = analysis.plotingGenerSex(df2)
    return path

def pdf(p,f):
    url = presentation.generatePDF(p,f)
    return url

def emailing(a):
    sending.send(a)

#'../input/suicides.csv'
def main(file,year):
    data = read_file(file)
    data_clean = cleaning(data)
    data_imported = impor(data_clean,"https://restcountries.eu/rest/v2/name/")
    data_filtered= filtering(data_imported, year)
    path = analyze(data_filtered)
    file_to_send = pdf(path, 'Helvetica')
    emailing(file_to_send)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a suicides report')
    parser.add_argument('-f', dest='filePath', default= None, help='.csv file to analyze.')
    parser.add_argument('-y', dest='year', default= 2000, type=int, help='Year to analyze since.')
    args = parser.parse_args()

    if isinstance(args.filePath, str) and isinstance(args.year, int):
        print(args.filePath)
        main(os.path.normpath(args.filePath),args.year)
    elif isinstance(args.filePath, str):
        print('Hay que especificar un argumento -y con el año desde el que se quiere filtrar')
    elif isinstance(args.year, int):
        print('Hay que especificar un argumento -f con la ruta al fichero .csv')
    else:
        print('Hay que especificar dos argumentos: -f con la ruta al fichero .csv y -y con el año desde el que se quiere filtrar')



