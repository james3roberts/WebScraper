import pandas as pd           
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import urllib.request
import bs4 as bs


#print('Badger ladder page.')
dfs = pd.read_html('https://www.badgerladder.com/pump-jacks/alum-pump-jack-packages/')
for df in dfs:
    writer = ExcelWriter('WebScraper.xlsx')
df.to_excel(writer,'Badger Lader',index= False)
# print('Poles')
dfs1 = pd.read_html('https://www.badgerladder.com/aluminum-pump-jack-poles-6-24-long//')
for df1 in dfs:
        writer = ExcelWriter('WebScraper.xlsx')
df1.to_excel(writer,sheet2='Badger Lader poles',index= False)
writer.save()
