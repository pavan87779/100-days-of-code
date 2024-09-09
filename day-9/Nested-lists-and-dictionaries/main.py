capitals={
    "France": "Paris",
    "Germany" : "Berlin",
}

#nested list in dictionary
travel_log={
    "France": ["Pairs","Lille","Dijon"],
    "Germany": ["Stuttgart","Brtlin"],
}
#print Lille
print(travel_log["France"][1])

nested_list=['A','B',['C','D']]
print(nested_list[2][1])
#nested dictionaries
travel_log={
    "France":{
        "run_time_visitor": 8,
        "cities_visitors": ["Paris","Lille","Dijon"]
    },
    "Germany":{
        "cities_visites":["Hamburg","Stuttgart","Berlin"],
               "total_visits":5},

}
print(travel_log["Germany"]["cities_visites"][2])
print(travel_log["France"])