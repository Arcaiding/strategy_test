import numpy as np
import pandas as pd
import download_bar as bar
import function as f
import matplotlib.pyplot as plt

btc_adx = bar.btc_data_bar
df = btc_adx
dmi = f.dmi(df)
dmi = pd.DataFrame(dmi)
dmi = dmi.drop(['<HIGH>', '<LOW>', '<CLOSE>', 'di+', 'di-', 'deal'], axis=1)
data_day = bar.btc_data_bar_day

data = pd.merge(data_day, dmi, on='<DATE>', how='left')  # переобразование недельки в дневку
for i in range(len(data) - 1, 0, -1):
    if data.loc[i, 'back'] == 'green':
        data.loc[i + 6, 'back'] = 'green'
        data.loc[i, 'back'] = np.nan
    if data.loc[i, 'back'] == 'red':
        data.loc[i + 6, 'back'] = 'red'
        data.loc[i, 'back'] = np.nan

for i in range(1, len(data)):
    if data.loc[i - 1, 'back'] == 'green' and data.loc[i, 'back'] != 'red':
        data.loc[i, 'back'] = 'green'
    if data.loc[i - 1, 'back'] == 'red' and data.loc[i, 'back'] != 'green':
        data.loc[i, 'back'] = 'red'

data_green = data.loc[data['back'] == 'green']
data_red = data.loc[data['back'] == 'red']

data_green.reset_index(drop=True, inplace=True)
data_green = pd.DataFrame(data_green)
data_red.reset_index(drop=True, inplace=True)
data_red = pd.DataFrame(data_red)
