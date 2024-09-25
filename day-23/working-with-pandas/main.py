import pandas as pd
data= pd.read_csv('weather_data.csv')
print(data)
data_dict = data.to_dict()
print(data_dict)