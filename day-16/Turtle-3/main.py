import turtle
import random
from turtle import *
#num_sides=int(input("enter number of side: "))
tim=turtle.Turtle()
color=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

def draw_shape(num_sides):
    for i in range(num_sides):
        angle=360/num_sides
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(color))
    draw_shape(shape_side_n)


screen=turtle.Screen()
screen.exitonclick()