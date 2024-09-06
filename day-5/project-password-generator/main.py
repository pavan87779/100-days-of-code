#Passsword Generator
import random
print("Welcome to the pyPassword Generator!")
l=int(input("How many letters would you like in your password?"))
s=int(input("How many symbols in"))
n=int(input("how many number would you like in your password?"))
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
symbol=['!','@','#','$','%,','^','&','*','(',')','_','+','-','=','~','<','>','?','.','/',',','|',';',':']
numbers=['1','2','3','4','5','6','7','8','9','0']
password=''
for i in range(1,l+1):
    password+=random.choice(letters)
for j in range(1,s+1):
    password+=random.choice(symbol)
for k in range(1,n+1):
    password+=random.choice(numbers)

print(f"The generator Password is {password}")