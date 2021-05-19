import nsepy
import pandas as pd 


df = pd.read_csv('_190to200.csv')

data = df['data']
top_mover_symbol = []
top_mover_price = []
top_mover_change = []
top_mover_pchange = []


for d in data :
    try:
        e = d.split("'")
        symbol = e[1]
        q = nsepy.get_quote(symbol)
        q_data = dict(q['data'][0])
        
        change = q_data['change']
        pchange = int(float(q_data['pChange']) )
        lastPrice = q_data['lastPrice']
        print(symbol)
        if pchange > 2:
            print(symbol)
            top_mover_symbol.append(symbol)
            top_mover_price.append(lastPrice)
            top_mover_change.append(change)
            top_mover_pchange.append(pchange)
    except:
        print('Bad symbol')
   
dict_top_mover = {'symbol':top_mover_symbol, 'price' : top_mover_price, 'change' : top_mover_change, 'pchange' : top_mover_pchange}
    
df = pd.DataFrame(dict_top_mover)

df.to_csv('topmovers_190to200.csv')