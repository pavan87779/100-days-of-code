import pandas as pd
data=pd.read_csv('weather_data.csv')
temp_list=data['temp'].to_list()
print(temp_list)

#dictionary
temp_dict =data['temp'].to_dict()
print(temp_dict)

print(data['temp'].mean())
print(data['temp'].median())
print(data['temp'].max())
#print(data['temp'].avg())

print(data.condition)

print(data[data.day=='Monday'])
print(data[data.temp==data.temp.max()])

monday=data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_f = monday_temp*9/5 +32

print(monday_temp_f)

#create a dataframe fromk scratch
data_dictt={
    "students": ["Any", "James", "Angela"],
    "scores": [76,66,65]

}
datafile=pd.DataFrame(data_dictt)
print(datafile)