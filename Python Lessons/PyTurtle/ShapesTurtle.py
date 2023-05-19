from turtle import  Turtle
my_turtle = Turtle()
angel = 360
angel_divisor = 3
color = ["red","yellow","green","purple","pink","brown","blue"]
my_turtle.width(5)
while angel_divisor < 10:
    for i in range(angel_divisor):
        my_turtle.color(color[angel_divisor-3])
        my_turtle.forward(60)
        my_turtle.right(angel/angel_divisor)
    angel_divisor = angel_divisor + 1