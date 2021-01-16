import csv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

filename = 'texas-history.csv'

df = pd.read_csv(filename)
#print(df)
cols_plot = ['date','deathIncrease', 'positiveIncrease']
axes = df[cols_plot].set_index('date').plot(marker='.', alpha=0.5, linestyle='solid', figsize=(18, 9), subplots=True)
#axes.set_xticklabels(x=df['date'], rotation=20)
for ax in axes:
    ax.set_ylabel('Number')
    #ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.show()
plt.savefig('new2.png')

#ax = plt.gca()
"""
fig, ax = plt.subplots()
ax.plot(df['deathIncrease'], color='black', label='deathIncrease')
#ax.plot(df['positiveIncrease'], color='red', label='positiveIncrease')
#opsd_monthly[['Wind', 'Solar']].plot.area(ax=ax, linewidth=0)
#ax = df.plot(x_compat=True)
ax.xaxis.set_major_locator(mdates.MonthLocator())
#ax.xaxis.set_major_locator(mdates.WeekdayLocator)
ax.legend()
ax.set_ylabel('Monthly Total (GWh)')

#df.plot(kind='line',x='date',y='death',ax=ax)
#df.plot(kind='line',x='date',y='deathIncrease', color='red', ax=ax)
#df.plot(kind='line',x='date',y='positive',color='blue', ax=ax)
#df.plot(kind='line',x='date',y='positiveIncrease', color='green', ax=ax)
#df.plot(kind='line',x='date',y='recovered',color='yellow', ax=ax)
#ax = df.plot(x_compat=True)
#ax.xaxis.set_major_locator(mdates.MonthLocator())
# df.plot(kind='bar',x='date',y='death',ax=ax)
# df.plot(kind='bar',x='date',y='deathIncrease', color='red', ax=ax)
# df.plot(kind='bar',x='date',y='positive',color='blue', ax=ax)
# df.plot(kind='bar',x='date',y='positiveIncrease', color='green', ax=ax)
# df.plot(kind='bar',x='date',y='recovered',color='yellow', ax=ax)
#plt.axis('tight')
#ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))
plt.xticks(rotation=20)    #range(0, N, 12),
plt.show()
plt.savefig('line.png')
"""
"""
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    death = []  # 2
    death_increase = [] # 3
    positive = []   # 4
    positive_increase = []  # 5
    recovered = []  # 6

    for index,column_header in enumerate(header_row):
        print(index, column_header)
    
    for row in reader:
        if row[2]=='' or row[3]=='' or row[4]=='' or row[5]=='' or row[6]=='':
            continue
        d = int(row[2],10)
        d_i = int(row[3],10)
        p = int(row[4],10)
        p_i = int(row[5],10)
        r = int(row[6],10)

        death.append(d)  #appending high temperatures   
        death_increase.append(d_i)
        positive.append(p)
        positive_increase.append(p_i)
        recovered.append(r)

    #Plot Data
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(highs, c = 'red') #Line 1
    #Format Plot
    plt.title("Daily High Temperatures, 2018", fontsize = 24)
    plt.xlabel('',fontsize = 16)
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major' , labelsize = 16)
    plt.show()
    """