import random
stages=['''   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
''','''   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
''','''   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
''','''   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
''','''   +---+
   |   |
   O   |
   |   |
       |
       |
=========
''',''''   +---+
   |   |
   O   |
       |
       |
       |
=========
''','''   +---+
   |   |
       |
       |
       |
       |
=========
''']
word_list=["elephant","camel","baboon"]
lives=6

choosen_woord=random.choice(word_list)

placeholder=""
word_length=len(choosen_woord)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letters=[]

while not game_over:
    guess=input("Guess a letter: ").lower()

    display=""
    for letter in choosen_woord:

        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter


        else:
            display+="_"

    print(display)

    if guess not in choosen_woord:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")


    if "_" not in display:
        game_over=True
        print("You are Win!")

    print(stages[lives])