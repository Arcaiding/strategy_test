import numpy as np
import pandas as pd

import btc_adx
import function

df = pd.DataFrame(btc_adx.data_green)
df = function.fma(df)
df['line_yellow_open'] = np.where(df['<LOW>'] < df['line_yellow'], 1, 0)

print('line yellow', df['line_yellow_open'].sum()/len(df) * 100, '%')

df = pd.DataFrame(btc_adx.data_red)
df = function.fma(df)
df['line_orange_open'] = np.where(df['<HIGH>'] > df['line_orange'], 1, 0)
print('line orange', df['line_orange_open'].sum()/len(df) * 100, '%')
