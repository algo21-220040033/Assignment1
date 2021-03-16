# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cheungxiaofee time:2021/2/4


# 导库
import requests
import time, datetime
import pandas as pd
import talib
pd.set_option('expand_frame_repr', False)


# 数据获取
BASE_URL = 'https://api.binancezh.cc'
limit = 1000 # 每次获取的数据数量（币安每次只能获取最多1000条数据）
ttime = time.strptime('2019-08-09 13:00:00', "%Y-%m-%d %H:%M:%S") # 开始时间
ctime = time.mktime(ttime)
start_time = int(ctime * 1000)
print(start_time)
end_time = int(start_time + limit * 60 * 1000)
print(end_time)
bttime = time.strptime('2020-03-13 23:00:00', "%Y-%m-%d %H:%M:%S") # 结束时间
bctime = time.mktime(bttime)
break_time = int(bctime * 1000) # 终止时间（超过则终止循环）

df1 = pd.DataFrame()

while True:

    url = BASE_URL + '/api/v1/klines' + '?symbol=XTZUSDT&interval=1h&limit=' + str(limit) + '&startTime=' + str(
        start_time) + '&endTime=' + str(end_time) # 获取url，symbol为货币对名称，interval为时间间隔，比如1m为分钟数据
    print(url)
    resp = requests.get(url)
    data = resp.json()
    df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
                                     'close_time': 6, 'quote_volume': 7, 'trades': 8, 'taker_base_volue': 9,
                                     'taker_quote_volume': 10, 'ignore': 11})


    print(df)

    df1 = df1.append(df)

    if end_time > break_time:
        break

    try: # 防止交易所暂停返回的是空的数据列表
        start_time = df['open_time'].iloc[-1] + 60 * 1000
        end_time = int(start_time + limit * 60 * 1000)
    except:
        start_time = start_time + 60 * 1000 * 2
        end_time = int(start_time + limit * 60 * 1000)

df1['open_time'] = df1['open_time'].apply(lambda x: time.localtime(x // 1000))
df1['open_time'] = df1['open_time'].apply(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", x))

df1.set_index('open_time', inplace=True)
print(df1)
df1.to_csv('xtz'+str(end_time) + '.csv')


# 获取一次数据用
# BASE_URL = 'https://api.binance.com'
# limit = 1000 # 每次获取的数据数量（币安每次只能获取最多1000条数据）
# start_time = 1615597200000
# end_time = 1615683600000
# # url = BASE_URL + '/api/v1/klines' + '?symbol=BUSDUSDT&interval=1m&limit=' + str(limit) + '&startTime=' + str(
# #         start_time) + '&endTime=' + str(end_time)
# url = BASE_URL + '/api/v1/klines' + '?symbol=BUSDUSDT&interval=1m&limit=' + str(limit)
# print(url)
# print(datetime.datetime.now())
# resp = requests.get(url)
# data = resp.json()
# df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
#                                  'close_time': 6, 'quote_volume': 7, 'trades': 8, 'taker_base_volue': 9,
#                                  'taker_quote_volume': 10, 'ignore': 11})
#
# # print(df)
# df['open_time'] = df['open_time'].apply(lambda x: time.localtime(x // 1000))
# df['open_time'] = df['open_time'].apply(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", x))
#
# df = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]
# df.set_index('open_time', inplace=True)
# df['EMA'] = talib.EMA(df['close'], timeperiod=60)
#
# print(df)
# df.to_csv(str(end_time) + '.csv')


# 时间触发再获取数据用（测试用）
# startTime = datetime.datetime(2021, 3, 11, 10, 42, 59)
# print('Program not starting yet...')
# while datetime.datetime.now() < startTime:
#     time.sleep(0.0001)
#     print(datetime.datetime.now())


# delta=datetime.timedelta(seconds=59) # , microseconds=999
# touch_time = datetime.datetime(2021,3,11,15,50,1)
# while True:
#     if datetime.datetime.now() > touch_time:
#         BASE_URL = 'https://api.binance.com'
#         limit = 500  # 每次获取的数据数量（币安每次只能获取最多1000条数据）
#         url = BASE_URL + '/api/v1/klines' + '?symbol=BUSDUSDT&interval=1m&limit=' + str(limit)
#         print(url)
#         print(datetime.datetime.now())
#         resp = requests.get(url)
#         data = resp.json()
#         df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
#                                          'close_time': 6, 'quote_volume': 7, 'trades': 8, 'taker_base_volue': 9,
#                                          'taker_quote_volume': 10, 'ignore': 11})
#
#         # print(df)
#         df['open_time'] = df['open_time'].apply(lambda x: time.localtime(x // 1000))
#         df['open_time'] = df['open_time'].apply(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", x))
#
#         df = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]
#         df.set_index('open_time', inplace=True)
#         df['EMA'] = talib.EMA(df['close'], timeperiod=60)
#
#         print(df)
#         touch_time = datetime.datetime.now() + delta
#     if touch_time > datetime.datetime(2021,3,11,15,53,0):
#         break