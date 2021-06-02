import nsepy
import pandas as pd 
import os


def calculate_toplosers(filename):
    folder = os.getcwd()
    destination = str(folder) + '\symbols'
    file_name = destination+'\\'+str(filename)
    df = pd.read_csv(file_name)

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
            if pchange < - 2 and int(float(change)) < 0 :
                print(symbol)
                top_mover_symbol.append(symbol)
                top_mover_price.append(lastPrice)
                top_mover_change.append(change)
                top_mover_pchange.append(pchange)
        except:
            print('Bad symbol')
    
    dict_top_mover = {'symbol':top_mover_symbol, 'price' : top_mover_price, 'change' : top_mover_change, 'pchange' : top_mover_pchange}
        
    df = pd.DataFrame(dict_top_mover)

    out = '\\toplosers\\toplosers'+str(filename)
    out = folder + out
    df.to_csv(out)