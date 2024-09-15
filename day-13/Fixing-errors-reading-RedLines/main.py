try:
    age=int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical number ex: 1,2,3,4,5....")
    age=int(input("How old are you? "))

if age>10:
    print(f"You can drive at age {age}.  ")

