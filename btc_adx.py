import numpy as np
import pandas as pd
import download_bar as bar
import function as f
import matplotlib.pyplot as plt
btc_adx = bar.btc_data_bar
df = btc_adx
dmi = f.dmi(df)
dmi = pd.DataFrame(dmi)
dmi.to_csv('проба.csv')

print(dmi)
