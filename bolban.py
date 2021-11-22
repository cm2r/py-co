import pyupbit
import pandas as pd
import datetime
import requests
import time
import webbrowser
import numpy

a = 1

while True:
    url = "https://api.upbit.com/v1/candles/minutes/5"
    
    querystring = {"market":"KRW-BTC","count":"100"}
    
    response = requests.request("GET", url, params=querystring)
    
    data = response.json()
    
    df = pd.DataFrame(data)
    
    df=df['trade_price'].iloc[::-1]
    

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

    
    if a==1:
        #url = "https://www.binance.com/kr/register?ref=X1401JUS"
        #webbrowser.open(url)

        #url = "https://bit.ly/3oWaIXG"
        #webbrowser.open(url)

        #url = "https://www.xn-----bt9ig0b31lcsga13i850awk2a6pg.com/"
        #webbrowser.open(url)
        a=2    
    

    unit=2
    
    band1=unit*numpy.std(df[len(df)-20:len(df)])
    
    bb_center=numpy.mean(df[len(df)-20:len(df)])
    
    band_high=bb_center+band1
    
    band_low=bb_center-band1   

    current_price = get_current_price("KRW-BTC")

        

    print('볼린저뱉드 상단: ', round(band_high,2))
    print('볼린저뱉드 하단: ', round(band_low,2))
    print('')
    print('현재가: ', round(current_price,2))
    time.sleep(1)

