import pandas as pd


btc=pd.read_csv('btc1584150060000.csv')
eth=pd.read_csv('eth1584150060000.csv')
ltc=pd.read_csv('ltc1584150060000.csv')

def Clean(data):
    data = data[['open_time', 'open']]
    data = data.set_index('open_time')
    return data

btc=Clean(btc)
btc.rename(columns={'open':'BTCUSDT'},inplace=True)
eth=Clean(eth)
eth.rename(columns={'open':'ETHUSDT'},inplace=True)
ltc=Clean(ltc)
ltc.rename(columns={'open':'LTCUSDT'},inplace=True)

list=[btc.T,eth.T,ltc.T]
df=pd.concat(list)
df=df.T
print(df)