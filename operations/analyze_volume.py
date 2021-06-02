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
        

tata_power = YahooFinance('CONCOR.NS', result_range='5d', interval='1d', dropna='True').result
print(tata_power)

