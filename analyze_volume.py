from fetcher import *
import nsetools




class Analyzer(object):

    def  __init__(self,csv_data=None,symbol=None) -> None:

        self.csv_data =  csv_data
        self.symbol  = symbol

    def listen_for_alerts(self):
        pass

    def get_vol_avg(self):
        pass

    def find_breakdown(self):
        pass

    @property  
    def status(self):
        pass
        

tata_power = YahooFinance('TATAPOWER.NS', result_range='1d', interval='15m', dropna='True').result
print(tata_power['Volume'].mean())