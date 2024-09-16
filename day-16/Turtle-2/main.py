from turtle import *
import turtle as t
tim=t.Turtle()
tim.forward(10)
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen=t.Screen()
screen.exitonclick()