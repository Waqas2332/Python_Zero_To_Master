import colorgram
import turtle
import random
rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_colors.append((r,g,b))

print(rgb_colors)
my_turtle = turtle.Turtle()
turtle.colormode(255)
for _ in range(10):
    for _ in range(10):
        rand_color = random.choice(rgb_colors)
        my_turtle.color(rand_color)
        my_turtle.dot(20)
        my_turtle.penup()
        my_turtle.forward(50)

    my_turtle.back(500)
    my_turtle.left(90)
    my_turtle.forward(40)
    my_turtle.right(90)