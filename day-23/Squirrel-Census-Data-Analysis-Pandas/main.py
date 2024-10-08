import pandas as pd
data= pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur color":["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

file=pd.DataFrame(data_dict)
file.to_csv("squirrel_color_count")
print(file)