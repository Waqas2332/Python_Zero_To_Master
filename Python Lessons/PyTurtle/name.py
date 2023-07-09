import turtle

my_turtle = turtle.Turtle()
# my_turtle.right(45)
# my_turtle.forward(60)
# my_turtle.right(-110)
# my_turtle.forward(50)
# my_turtle.right(110)
# my_turtle.forward(60)
# my_turtle.right(-110)
# my_turtle.forward(60)

my_turtle.circle(30)
my_turtle.penup()
my_turtle.forward(30)
my_turtle.setheading(90)
my_turtle.pendown()
my_turtle.forward(60)
print(my_turtle)


screen = turtle.Screen()
screen.exitonclick()