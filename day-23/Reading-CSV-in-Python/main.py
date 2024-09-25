"""import csv
with open('weather_data.csv') as file:
    data=csv.reader(file)
    for row in data:
        temperature=[]
        if row[1]!='temp':
            temperature.append(row[1])
    print(temperature)"""

import pandas as pd
data= pd.read_csv("weather_data.csv")
#print(type(data))
print(data['temp'])