import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def filteryear(dataframe,year):
    return dataframe[dataframe['year']>year]

def genderSex(dataframe):
    x = dataframe.groupby(['sex','generation']).agg(['sum','mean','std']).unstack(level=0).reset_index()
    return x
def continentSex(dataframe):
    y = dataframe.groupby(['sex','Region']).agg(['sum','mean','std']).unstack(level=0).reset_index()
    return y
def plotingGenerSex(df,year):
    men_means, men_std = tuple(df['suicides/100k pop']['mean']['male']), tuple(df['suicides/100k pop']['std']['male'])
    women_means, women_std = tuple(df['suicides/100k pop']['mean']['female']), tuple(df['suicides/100k pop']['std']['female'])

    ind = np.arange(len(men_means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, men_means,  width, yerr=men_std, label='Men') # remove std 
    rects2 = ax.bar(ind + width/2, women_means,  width, yerr=women_std, label='Women') # remove std 

    ax.set_ylabel('Suicides/100k pop', fontsize=20, fontweight='bold')
    ax.set_title('Suicides/100k pop. by GENERATION and GENDER\n              {}-2014'.format(year), fontsize=20, fontweight='bold')
    ax.set_xticks(ind)
    ax.set_xticklabels((tuple(set(df['generation']))), fontsize=16, fontweight='bold')
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
    path='../presentacion/Suicides-Generation-Sex.png'
    fig.savefig(path)
    return path

def plotingContinentSex(df,year):
    men_means, men_std = tuple(df['suicides/100k pop']['mean']['male']), tuple(df['suicides/100k pop']['std']['male'])
    women_means, women_std = tuple(df['suicides/100k pop']['mean']['female']), tuple(df['suicides/100k pop']['std']['female'])

    ind = np.arange(len(men_means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, men_means,  width, yerr=men_std, label='Men') # remove std 
    rects2 = ax.bar(ind + width/2, women_means,  width, yerr=women_std, label='Women') # remove std 

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Suicides/100k pop', fontsize=20, fontweight='bold')
    ax.set_title('Suicides/100k pop. by CONTINENT and GENDER\n              {}-2014'.format(year), fontsize=20, fontweight='bold')
    ax.set_xticks(ind)
    ax.set_xticklabels((tuple(set(df['Region']))), fontsize=20, fontweight='bold')
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
    path = '../presentacion/Suicides-per-contintent.png'
    fig.savefig(path)
    return path

def plot3(data,y):
    df1 = data.groupby(['year']).agg(['sum','mean'])
    fig, ax1 = plt.subplots()
    s1 = df1['suicides_no']['mean']
    ax1.plot( s1, 'b-')
    ax1.set_xlabel('Year')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel('Suicides per country', color='r')
    ax1.tick_params('y', colors='r')

    ax2 = ax1.twinx()
    s2 = df1['gdp_per_capita ($)']['mean']
    ax2.plot(s2, 'r')
    ax2.set_ylabel('GDP_per_capita', color='b')
    ax2.tick_params('y', colors='b')

    plt.title('Evolution suicides vs gdp per capita ({}-2014)'.format(y))
    fig.tight_layout()
    path = '../presentacion/Suicides-evolution-vs-gdp.png'
    fig.savefig(path)
    return path

def plot4(data,yea):
    df5 = data.groupby(['country']).agg(['sum','mean','std'])[['suicides/100k pop','gdp_per_capita ($)']].reset_index()
    df5.sort_values(('suicides/100k pop','mean'), ascending=False,inplace=True)
    df6=df5[:10]
    fig, ax = plt.subplots()    
    width = 0.75
    x = df6[('country')]
    y = df6[('suicides/100k pop','mean')]
    ind = np.arange(len(y))
    ax.barh(ind, y, width, color=['red', 'red', 'red', 'red', 'orange','orange','orange','yellow','yellow','yellow'],edgecolor='blue')
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(x, minor=False)
    for i, e in enumerate(y):
        ax.text(e + 1, i , "{0:.2f}".format(e), color='black', fontweight='bold')
    
    plt.title('Top 10 Countries by suicides average between {}-2014'.format(yea))
    plt.xlabel('Suicides/100k population')
    plt.ylabel('Country')
    fig.set_size_inches(18.5, 10.5)
    path = '../presentacion/Top10CountriesRate.png'
    fig.savefig(path)
    return path

def filtering(data,year):
    y=int(year)
    df = filteryear(data,y)
    return df

def analyze(data,year):
    df2 = genderSex(data)
    path = plotingGenerSex(df2,year)
    df3 = continentSex(data)
    path2 = plotingContinentSex(df3,year)
    path3 = plot3(data,year)
    path4 = plot4(data,year)
    return path, path2,path3, path4