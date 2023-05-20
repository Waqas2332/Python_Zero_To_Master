import turtle
from turtle import  Turtle
import random
turtle.colormode(255)
my_turtle = Turtle()
directions = [0,90,180,270,360]

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

my_turtle.width(5)
for _ in range(200):
    my_turtle.color(randomColor())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))