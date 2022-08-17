import btc_adx as btc
import pandas as pd
import numpy as np
interval = 3
df = btc.btc_adx
df['dm+'] = df['<HIGH>'] - df.shift(1)['<HIGH>']
df['dm-'] = df.shift(1)['<LOW>'] - df['<LOW>']
df['dm+'] = np.where((df['dm+'] > df['dm-']) & (df['dm+'] > 0), df['dm+'], 0)
df['dm-'] = np.where((df['dm-'] > df['dm+']) & (df['dm-'] > 0), df['dm-'], 0)
df['tr_1'] = df['<HIGH>'] - df['<LOW>']
df['tr_2'] = df['<HIGH>'] - df.shift(1)['<CLOSE>']
df['tr_3'] = df['<LOW>'] - df.shift(1)['<CLOSE>']
df['tr'] = df[['tr_1', 'tr_2', 'tr_3']].max(axis=1)
del df['tr_1']
del df['tr_2']
del df['tr_3']
df['tr' + str(interval)] = df['tr'].rolling(interval).sum()
df['dmi+' + str(interval)] = df['dm+'].rolling(interval).sum()
df['dmi-' +str(interval)] = df['dm-'].rolling(interval).sum()
df['di+'] = df['dmi+' + str(interval)] / df['tr' + str(interval)] * 100
df['di-'] = df['dmi-' +str(interval)] / df['tr' + str(interval)] * 100
del df['tr']
del df['tr' + str(interval)]
del df['dmi+' + str(interval)]
del df['dmi-' +str(interval)]
del df['dm-']
del df['dm+']