import turtle
from turtle import *
import random
def random_walk():
    color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray","SeaGreen"]
    directions=[0,90,180,270]

    tim=turtle.Turtle()
    for i in range(200):
        tim.width(13)
        tim.speed('fastest')
        tim.forward(30)
        tim.setheading(random.choice(directions))
        tim.color(random.choice(color))



    screen=turtle.Screen()
    screen.exitonclick()

random_walk()