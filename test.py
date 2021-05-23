import nsepy
from datetime import date


data = nsepy.get_history(symbol='SBIN',start=date(2021,5,1), end=date(2021,5,20),series='')

nsepy.get_expiry_date
print(data)