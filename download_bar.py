import pandas as pd

btc_data_bar = pd.read_csv('btc_6y.csv')
btc_data_bar = pd.DataFrame(btc_data_bar)
del btc_data_bar['<TIME>']
del btc_data_bar['<VOL>']

btc_data_bar['<DATE>'] = pd.to_datetime(btc_data_bar['<DATE>'])

