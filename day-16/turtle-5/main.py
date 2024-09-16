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

    def spirograph(size_of_gap):

        for i in range(int(360/size_of_gap)):
            tim.speed('fastest')
            tim.color(random_color())
            tim.circle(100)
            tim.setheading(tim.heading()+size_of_gap)
            tim.circle(100)
    spirograph((5))






    screen=t.Screen()
    screen.exitonclick()

random_walk()