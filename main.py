import datetime
import os
import pandas as pd

import calculations as calc

PATH = './data/'

columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adjustment']
df = pd.DataFrame(columns=columns)

for csvfile in os.listdir(PATH):
    if csvfile.endswith('.csv'):
        t = pd.read_csv(PATH+csvfile)
        df = df.append(t)

df.drop_duplicates(subset=columns, keep='first', inplace=True)

# convert date column
# sort by date
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by=['Date'], inplace=True, ascending=True)

# calcs
# add information
df['daydirection'] = df.apply(lambda x: calc.daydir(x['Open'], x['Close']),
                    axis=1)
df = calc.opengap(df)
df = calc.smaclose(df, 10, 3)


# how often do gaps fill for different sized gaps
# break down the fill scenarios
# is a SMA oscillator useful
# how many up and down days in a row occur
#df = df[(df['gapclosed'] == True) & (df['opengap_perc'] < 0.5)]
df = df[(df['opengap_perc'] > -0.5) & (df['opengap_perc'] < 0.5)]
table = pd.pivot_table(df, index=['gapclosed'], aggfunc='count')
table
 
#hist = df['opengap_perc'].plot(kind='hist',bins=50,figsize=(12,6))
#hist.plot()
#plt.show()