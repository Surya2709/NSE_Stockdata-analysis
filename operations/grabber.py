import nsetools
import pandas as pd

nse = nsetools.Nse()

val_dict = dict(nse.get_stock_codes())
print(type(val_dict))
all_codes = list(val_dict.keys())

considerlist = []

for symbol in all_codes:
    try:
        data = dict(nse.get_quote(symbol))
        if int(data['lastPrice']) < 200:
            print(f'adding {symbol}')
            considerlist.append(symbol)
    except:
        print("bad Symbol")

dict = { 'symbols': considerlist} 
df = pd.DataFrame(dict) 
df.to_csv('chosensymbols.csv')