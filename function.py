import pandas as pd
import numpy as np


def dmi(df: pd.DataFrame(), interval: int = 3):
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
    df.loc[interval - 1, 'dmi+' + str(interval)] = df.loc[0:interval - 1, 'dm+'].sum()
    df.loc[interval - 1, 'dmi-' + str(interval)] = df.loc[0:interval - 1, 'dm-'].sum()
    for i in range(interval, len(df)):
        df.loc[i, 'dmi+' + str(interval)] = df.loc[i - 1, 'dmi+' + str(interval)] - (
                    df.loc[i - 1, 'dmi+' + str(interval)] / interval) + df.loc[i, 'dm+']
    for i in range(interval, len(df)):
        df.loc[i, 'dmi-' + str(interval)] = df.loc[i - 1, 'dmi-' + str(interval)] - (
                    df.loc[i - 1, 'dmi-' + str(interval)] / interval) + df.loc[i, 'dm-']
    df['di+'] = df['dmi+' + str(interval)] / df['tr' + str(interval)] * 100
    df['di-'] = df['dmi-' + str(interval)] / df['tr' + str(interval)] * 100
    del df['dm+']
    del df['dm-']
    del df['dmi+' + str(interval)]
    del df['dmi-' + str(interval)]
    del df['tr']
    del df['tr' + str(interval)]
    df['back'] = np.where(df['di+'] > df['di-'], 'green', 'red')
    for i in range(interval - 1, len(df)):
        if df.loc[i, 'back'] == 'green' and df.loc[i - 1, 'back'] == 'red':
            df.loc[i, 'deal'] = 'long'
        elif df.loc[i, 'back'] == 'red' and df.loc[i - 1, 'back'] == 'green':
            df.loc[i, 'deal'] = 'short'

    df = df[df['deal'].isin(['long', 'short'])]
    df = df.reset_index()
    del df['index']
    del df['<OPEN>']
    return df


def sma(df: pd.DataFrame(), interval: int = 12):
    df['sma' + str(interval)] = df['<CLOSE>'].rolling(interval).mean()
    return df


def fma(df: pd.DataFrame(), interval: int = 12):
    df = sma(df, interval)
    df['line_red'] = df['sma' + str(interval)] * 1.27
    df['line_orange'] = df['sma' + str(interval)] * 1.127845
    df['line_yellow'] = df['sma' + str(interval)] * 0.908844
    df['line_green'] = df['sma' + str(interval)] * 0.8
    return df
