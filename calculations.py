import datetime as dt
import pandas as pd


def daydir(o_price, c_price):
    if o_price > c_price:
        direction = 'down'
    elif c_price > o_price:
        direction = 'up'
    else:
        direction = 'flat'
    return direction


def opengap(df):
    # add a column with the opening gap
    df['opengap'] = df['Open'] - df['Close'].shift()
    df['opengap'].fillna(0, inplace=True)
    df['opengap_perc'] = (df['opengap'] / df['Close'].shift()) * 100
    df['gapclosed'] = (df['Low'] <= df['Close'].shift()) & (df['High'] >= df['Close'].shift())
    return df


def smaclose(df, s, f):
    df['fast_sma'] = df['Close'].rolling(f).mean()
    df['slow_sma'] = df['Close'].rolling(s).mean()
    df['lbrosc'] = df['fast_sma'] - df['slow_sma']
    df['lbrosc_signal'] = df['lbrosc'].rolling(16).mean()
    return df
