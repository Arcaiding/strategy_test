import numpy as np
import pandas as pd
import download_bar as bar
import function as f
import matplotlib.pyplot as plt
btc_adx = bar.btc_data_bar
df = btc_adx
dmi = f.dmi(df)
dmi = pd.DataFrame(dmi)
dmi['back'] = np.where(dmi['di+'] > dmi['di-'], 'green', 'red')
sma = f.fma(df)

print(sma)
