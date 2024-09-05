print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12, or 15?"))
split=int(input("How many people to splot the bill?"))
tip_per=tip/100
total_tip=bill*tip_per
total_bill=bill+total_tip
each_person=total_bill/split
round(each_person,2)
print("Each person should pay:"+"$",each_person)