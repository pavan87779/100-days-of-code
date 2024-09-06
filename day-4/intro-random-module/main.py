import random
random_integer=random.randint(1,10)
print(random_integer)
print(random_integer*10)

rand_float=random.uniform(2,8)
print(rand_float)

#head or tales
head_tales=random.randint(0,1)
if head_tales==0:
    print("head")
else:
    print("tale")
