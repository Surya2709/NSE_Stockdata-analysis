from topgainers import *
import os 

folder = os.getcwd()

destination = str(folder) + '\symbols'

files = os.listdir(destination)

for file in files:
    
    calculate_topgainers(file)