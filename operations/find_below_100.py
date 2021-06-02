import nsepy
import pandas as pd


nse = nsepy

df = pd.read_csv('chosensymbols.csv')

below_200 = list(df['symbols'])

_190to200 = []
_170to190 = []
_150to170 = []
_130to150 = []
_100to130 = []
_90to100 = []
_70to90 = []
_50to70 = []
_40to50  = []
_25to40 = []
_15to25 = []
_10to15 = []
_5to10 = []
_0to5 = []

unhandleable = []

for symbol in below_200:
    try:
        print(symbol)
        data= nse.get_quote(str(symbol))
        data = dict(data['data'][0])

        print('data')
        print(f'checking {symbol}')

        val = int(float(data['lastPrice'] ))

        if val> 190 and  val< 200:
            _190to200.append((symbol,data['lastPrice']))
        elif val> 170 and  val< 190:
            _170to190.append((symbol,data['lastPrice']))
        elif val> 150 and  val< 170:
            _150to170.append((symbol,data['lastPrice']))
        elif val> 130 and  val< 150:
            _130to150.append((symbol,data['lastPrice']))
        elif val> 100 and  val< 130:
            _100to130.append((symbol,data['lastPrice']))
        elif val> 90 and  val< 100:
            _90to100.append((symbol,data['lastPrice']))
        elif val> 70 and  val< 90:
            _70to90.append((symbol,data['lastPrice']))
        elif val> 50 and  val< 70:
            _50to70.append((symbol,data['lastPrice']))
        elif val> 40 and  val< 50:
            _40to50.append((symbol,data['lastPrice']))
        elif val> 25 and  val< 40:
            _25to40.append((symbol,data['lastPrice']))
        elif val> 15 and  val< 25:
            _15to25.append((symbol,data['lastPrice']))
        elif val> 10 and  val< 15:
            _10to15.append((symbol,data['lastPrice']))
        elif val> 5 and  val< 10:
            _5to10.append((symbol,data['lastPrice']))
        elif val> 0 and  val< 5:
            _0to5.append((symbol,data['lastPrice']))
        else:
            unhandleable.append((symbol,data['lastPrice']))
    except:
        print('bad Symbol')

print('[#] Done checking , Now converting to dict')

dict_190to200 = { 'data' : _190to200 }
dict_170to190 = { 'data' :  _170to190}
dict_150to170 ={ 'data' :  _150to170}
dict_130to150 ={ 'data' :  _130to150}
dict_100to130 ={ 'data' :  _100to130}
dict_90to100 ={ 'data' :  _90to100}
dict_70to90 = { 'data' :  _70to90}
dict_50to70 = { 'data' :  _50to70}
dict_40to50  =  { 'data' :  _40to50}
dict_25to40 = { 'data' :  _25to40}
dict_15to25 = { 'data' :  _15to25}
dict_10to15 = { 'data' :  _10to15}
dict_5to10 = { 'data' :  _5to10}
dict_0to5 = { 'data' :  _0to5}
dict_unhandled = {'data' :unhandleable }

print('[#] Creating data frames')

d1 = pd.DataFrame(dict_190to200 )
d2 = pd.DataFrame(dict_170to190 )
d3 = pd.DataFrame(dict_150to170 )
d4 = pd.DataFrame(dict_130to150 )
d5 = pd.DataFrame(dict_100to130 )
d6 = pd.DataFrame(dict_90to100 )
d7 = pd.DataFrame(dict_70to90 )
d8 = pd.DataFrame(dict_50to70 )
d9 = pd.DataFrame(dict_40to50 )
d10 = pd.DataFrame(dict_25to40 )
d11 = pd.DataFrame(dict_15to25 )
d12 = pd.DataFrame(dict_10to15 )
d13 = pd.DataFrame(dict_5to10 )
d14 = pd.DataFrame(dict_0to5 )
d15 = pd.DataFrame(dict_unhandled )


print('[#] Saving it in csv files')

d1.to_csv('_190to200.csv')
d2.to_csv('_170to190.csv')
d3.to_csv('_150to170.csv')
d4.to_csv('_130to150.csv')
d5.to_csv('_100to130.csv')
d6.to_csv('_90to100.csv')
d7.to_csv('_70to90.csv')
d8.to_csv('_50to70.csv')
d9.to_csv('_40to50.csv')
d10.to_csv('_25to40.csv')
d11.to_csv('_15to25.csv')
d12.to_csv('_10to15.csv')
d13.to_csv('_5to10.csv')
d14.to_csv('_0to5.csv')
d15.to_csv('_unhandled.csv')

print('[#] Saved Successfully !!')