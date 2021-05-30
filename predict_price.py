from sklearn.svm import SVR
import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')



def validate_data(file):
    df = pd.read_csv(file)
    dates = df["Date"]
    days = []
    for date in  dates:
        day = date.split(" ")
        days.append(day[0])
    df['Date'] = days
    return df

df = validate_data('CONCOR.csv')
actual_price = df.tail(1)
df = df.head(len(df)-1)

#create empty lists
days = list()
close_prices = list()

#get only the dates and the adjusted close prices
df_days = df.loc[:,'Date']
df_close = df.loc[:,'Close']

for day in df_days:
    day = day.split('-')[2]
    days.append([int(day)])
    
for close_price in df_close:
    close_prices.append(float(close_price))


#creating the models

lin_svr = SVR(kernel='linear',C=1000.0)
lin_svr.fit(days,close_prices)


poly_svr = SVR(kernel='poly',C=1000.0,degree=2)
poly_svr.fit(days,close_prices)


rbf_svr = SVR(kernel='rbf',C=1000.0,gamma=0.85)
rbf_svr.fit(days,close_prices)

#plot the models
plt.figure(figsize=(16,8))
plt.scatter(days,close_prices,color ='black',label='Data')
plt.plot(days,rbf_svr.predict(days),color= 'green', label="RBF Model")
plt.plot(days,poly_svr.predict(days),color = 'orange',label = 'Polynomial Model')
plt.plot(days,lin_svr.predict(days), color = 'blue', label = "Linear Model")
plt.xlabel("Days")
plt.ylabel("Close Prices")
plt.legend()
plt.show()

target_day = [[27]]
print(rbf_svr.predict(target_day))