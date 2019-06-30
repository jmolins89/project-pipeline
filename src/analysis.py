import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import acquisition
import clean
import importing


def filteryear(dataframe,year):
    return dataframe[dataframe['year']>year]

def genderSex(dataframe):
    x = dataframe.groupby(['sex','generation']).agg(['sum','mean','std']).unstack(level=0).reset_index()
    return x

def plotingGenerSex(df):
    men_means, men_std = tuple(df['suicides/100k pop']['mean']['male']), tuple(df['suicides/100k pop']['std']['male'])
    women_means, women_std = tuple(df['suicides/100k pop']['mean']['female']), tuple(df['suicides/100k pop']['std']['female'])

    ind = np.arange(len(men_means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, men_means,  width, yerr=men_std, label='Men') # remove std 
    rects2 = ax.bar(ind + width/2, women_means,  width, yerr=women_std, label='Women') # remove std 

    ax.set_ylabel('Suicides/100k pop')
    ax.set_title('Suicides/100k pop. by generation and gender')
    ax.set_xticks(ind)
    ax.set_xticklabels((tuple(set(df['generation']))))
    ax.legend()
    def autolabel(rects, xpos='center'):
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0, 'right': 1, 'left': -1}
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{0:.2f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(offset[xpos]*3, 3),  # use 3 points offset
                        textcoords="offset points",  # in both directions
                        ha=ha[xpos], va='bottom')
    autolabel(rects1, "left")
    autolabel(rects2, "right")
    fig.tight_layout()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('../presentacion/SuicidesGenerationSex.png')
    plt.show()

url="https://restcountries.eu/rest/v2/name/"
print('Reading file...')
data = acquisition.open_file('../input/suicides.csv')
data_clean=data.copy()
clean.delete_columns(data_clean,['HDI for year','country-year']) 
data_clean = clean.delete_rows_excluding(data_clean,'country','Saint Vincent and Grenadines')
data_clean = clean.resetindex(data_clean)
languages = importing.apiimportlanguage(data_clean,url)
regions = importing.apiimportregion(data_clean,url)
listlangu=importing.generatelist(data_clean,'country',languages)
listreg=importing.generatelist(data_clean,'country',regions)
importing.add_columns(data_clean,'Language',listlangu)
importing.add_columns(data_clean,'Region',listreg)
df2 = genderSex(data_clean)
plotingGenerSex(df2)



