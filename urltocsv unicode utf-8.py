import pandas as pd
import io
import requests
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
#print(c)
a = 'data'
file_name = f'{a}.csv'
#c.to_csv(file_name, sep='\t')
c.to_csv(file_name, encoding='utf-8')
#