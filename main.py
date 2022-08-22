import pandas as pd
import numpy as np
import function as f
import download_bar as bar

df = bar.btc_data_bar
df = f.dmi(df)
df['back'] = np.where(df['di+'] > df['di-'], 'green', 'red')
for i in range(2, len(df)):
    if df.loc[i, 'back'] == 'green' and df.loc[i - 1, 'back'] == 'red':
        df.loc[i, 'deal'] = 'long'
    elif df.loc[i, 'back'] == 'red' and df.loc[i-1, 'back'] == 'green':
        df.loc[i, 'deal'] = 'short'

df = df[df['deal'].isin(['long', 'short'])]
df = df.reset_index()
del df['index']
for i in range(0, len(df) - 1):
    if df.loc[i, 'deal'] == 'long' and df.loc[i + 1, 'deal'] == 'short':
        df.loc[i, 'result'] = df.loc[i + 1, '<CLOSE>'] / df.loc[i, '<CLOSE>']
    elif df.loc[i, 'deal'] == 'short' and df.loc[i + 1, 'deal'] == 'long':
        df.loc[i, 'result'] = df.loc[i, '<CLOSE>'] / df.loc[i + 1, '<CLOSE>']

df.to_csv('проба.csv')
print(df)