import random
friends=["pavan","kumar","nava","sridhar","pitta"]
bill_payer=random.choice(friends)
print(f"The bill is paying by {bill_payer}")

random_index=random.randint(0,4)
print(f"second method of payng bill is {friends[random_index]}")