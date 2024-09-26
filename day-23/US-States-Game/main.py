from turtle import *
import turtle
import pandas as pd
data = pd.read_csv("50_states.csv")

screen=Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states=data.state.to_list()

gussed_states=[]
while len(gussed_states)<50:
    answer_state= screen.textinput(title="Guess the state",prompt="What's another state's").title()
    print(answer_state)


    if answer_state== 'Exit':
        missing_states=[]
        for state in all_states:
            if state not in gussed_states:
                missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        gussed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state== answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)