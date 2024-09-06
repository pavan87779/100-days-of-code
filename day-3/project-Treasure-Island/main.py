print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("your Mission is to find the treasure.")
choice1=input('you are at a corssroad, where do you want to go? type "left"or "right". ')
if choice1=='left':
    print("you are ahead towards treasure!")
    choice2=input("choose to swim or wait.")
    if choice2=='wait':
        print("yahhy! a step away from treasure")
        choice3=input('choose any one colored door: "Red", "Yellow", "Blue"  ')
        if choice3=="Red":
            print("You are Burned by Fire! Game Over!")
        elif choice3=='Yellow':
            print("congrats! you Win!")
        elif choice3=='Blue':
            print("You are Eaten by beasts! Game Over!")
        else:
            print("Game Over!")
    elif choice2=='swim':
        print("Attacked by trout.Game Over!.")
    else:
        print("Attacked by trout.Game Over!.")
elif choice1=='Right':
    print("Fall into a hole.Game Over!")

else:
    print("Game Over!")
