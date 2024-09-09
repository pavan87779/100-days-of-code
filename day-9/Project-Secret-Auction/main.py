import art
from replit import clear

print(art.logo)
def actution(bidding):
    highest=0
    winner=""
    for value in bidding:
        bid_amount=bidding[value]
        if bid_amount>highest:
            highest=bid_amount
            winner=value

    print(f"The winner is {winner} with bid of ${highest}. ")



ac={}
continue_bidding=True
while continue_bidding:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    ac[name]=bid
    next = input("is there any other bit? if yes 'Y', No 'N' ").lower()
    if next=='no':
        continue_bidding=False
        actution(ac)
    elif next=='yes':
        clear()
    else:
        print("entered wrong")



