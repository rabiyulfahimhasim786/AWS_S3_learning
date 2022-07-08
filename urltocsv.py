import pandas as pd

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
c=pd.read_csv(url)
#print(c)
a = 'test'
file_name = f'{a}.csv'
c.to_csv(file_name, encoding='utf-8')