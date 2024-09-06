import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps=[rock,paper,scissor]
computer_choice=random.choice(rps)
user_choice=int(input("enter your choice Rock-0,Paper-1,scissor-2 ."))
game=0
if user_choice==0:
    game=rock
    print(game)
    if computer_choice==rps[0]:
        print(computer_choice)
        print("its Draw")
    elif computer_choice==rps[1]:
        print(computer_choice)
        print("computer wins")
    elif computer_choice==rps[2]:
        print(computer_choice)
        print("You wins")
    else:
        print("enterd wrong")
elif user_choice==1:
    game=paper
    print(game)
    if computer_choice==rps[0]:
        print(rock)
        print("you wins")
    elif computer_choice==rps[1]:
        print(paper)
        print("Its Draw")
    elif computer_choice==rps[2]:
        print(scissor)
        print("Computer Wins!")
    else:
        print("enter wrong option")
elif user_choice==2:
    game=scissor
    print(game)
    if computer_choice==rps[0]:
        print(rock)
        print("Computer wins!")
    elif computer_choice==rps[1]:
        print(paper)
        print("you wins!")
    elif computer_choice==rps[2]:
        print(scissor)
        print("Its a Draw!")
    else:
        print("entere wrong option")
else:
    print("enter wrong input(it should be in b/w o-2 only)")
