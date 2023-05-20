import turtle
import random

turtle.colormode(255)
def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
for _ in range(100):
    my_turtle.color(randomColor())
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading() + 4)



screen = turtle.Screen()
screen.exitonclick()