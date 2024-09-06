print("welcome to the rollercoaster!")
height=int(input("what is your height in cm? "))
blll=0

if height>=120:
    print("You can have a rollercoaser ride")
    age=int(input("what is your age?"))
    if age<=12:
        bill=5
        print("your ticket price is $5")
    elif age<=18:
        bill=7
        print("Your ticket price is $7")
    else:
        bill=12
        print("your ticket price is $12")
    photo=input("Do you want to have a photos take? type Y for yes ,N for no.")
    if photo=="Y":
        bill+=3
        print(f"your final bill is {bill}")

else:
    print("Sorry you are not allowed to have rollercoaster ride")