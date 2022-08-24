import pandas as pd
import numpy as np
import function as f
import download_bar as bar

df = bar.btc_data_bar
df = f.dmi(df)
for i in range(0, len(df) - 1):
    if df.loc[i, 'deal'] == 'long' and df.loc[i + 1, 'deal'] == 'short':
        df.loc[i, 'result'] = df.loc[i + 1, '<CLOSE>'] / df.loc[i, '<CLOSE>']
    elif df.loc[i, 'deal'] == 'short' and df.loc[i + 1, 'deal'] == 'long':
        df.loc[i, 'result'] = df.loc[i, '<CLOSE>'] / df.loc[i + 1, '<CLOSE>']
del df['back']

print(df)
