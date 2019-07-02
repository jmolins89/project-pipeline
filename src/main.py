import argparse
import os

from acquisition import open_file
from clean import cleaning
from importing import impor
from analysis import filtering
from analysis import analyze
from presentation import pdf
from sending import emailing

def main(year, inform):
    df = open_file('../input/suicides.csv')
    data_clean = cleaning(df)
    data_imported = impor(data_clean,"https://restcountries.eu/rest/v2/name/")
    data_filtered= filtering(data_imported, year)
    path, path2, path3,path4 = analyze(data_filtered,year)
    file_to_send = pdf(path,path2,path3,path4, 'Helvetica',year,inform)
    emailing(file_to_send, year)

if __name__ == "__main__":
    valid_inform=['s','e']
    parser = argparse.ArgumentParser(description='This pipeline generates a suicides report')
    parser.add_argument('-y','--year', dest='year', default= None, type=int,required=True, help='Year from which you are going to filter. Min value is 1987 and max value is 2014')
    parser.add_argument('-i','--inform', dest='typeinform', choices = valid_inform, default= None, type=str,required=True, help='Type of inform you want to receive: Short (s) or extended version(e)')
    args = parser.parse_args()

    if isinstance(args.year, int) and isinstance(args.typeinform,str):
        main(args.year,args.typeinform)
    elif isinstance(args.year, int):
        print('You should specify the argument -i with the type of inform you want to receive')
    elif isinstance(args.typeinform,str):
        print('You should specify the argument -y with the year from which you are going to filter')
    else:
        print('You have to specify the arguments -y with the year from which you are going to filter and -i with the type of inform you want to receive')
