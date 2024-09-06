#nested if and else

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height>=120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age?"))
    if age<=12:
        print("Please pay $5.")
    elif age<=18:
        print("Please Pay $7")
    else:
        print("Please pay $12")
else:
    print("Soory you are not allowed to ride rollercoaster!.")