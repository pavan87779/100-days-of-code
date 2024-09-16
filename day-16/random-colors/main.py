import turtle as t
import random
from turtle import *

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color


def random_walk():
    #color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray","SeaGreen"]
    directions=[0,90,180,270]

    tim=t.Turtle()
    for i in range(100):
        tim.width(13)
        tim.speed('fastest')
        tim.forward(30)
        tim.setheading(random.choice(directions))
        tim.color(random_color())



    screen=t.Screen()
    screen.exitonclick()

random_walk()