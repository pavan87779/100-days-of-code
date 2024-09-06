print("Welcome to Python Pizza deliveries!")
size=input("What size of Pizza you want? S, M, L?")
pepperoni=input("Do you want to pepperoni on your pizza? Y or N:?")
extra_cheese=input("Do you want to extra cheese? Y or N:?")
#billing according to customer requirements
bill=0
if size=='L':
    bill+=25
elif size=='M':
    bill+=20
elif size=='S':
    bill+=15
else:
    print("You enterd wrong option")
#adding bill on pepperoni
if pepperoni=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
#adding extra cheese
if extra_cheese=='Y':
    bill+=1
print(f"your final bill is {bill}")