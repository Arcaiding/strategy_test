import pandas as pd

# week

btc_data_bar = pd.read_csv('btc_6y.csv')
btc_data_bar = pd.DataFrame(btc_data_bar)
del btc_data_bar['<TIME>']
del btc_data_bar['<VOL>']
btc_data_bar['<DATE>'] = pd.to_datetime(btc_data_bar['<DATE>'], format='%d/%m/%y')

# day

btc_data_bar_day = pd.read_csv('6y_d.csv')
del btc_data_bar_day['<TIME>']
del btc_data_bar_day['<VOL>']
btc_data_bar_day['<DATE>'] = pd.to_datetime(btc_data_bar_day['<DATE>'], format='%d/%m/%y')
