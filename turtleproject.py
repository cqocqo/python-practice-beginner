# Drawing with the package turtle

# Import turtle
import turtle

# Let's get a nice set-up in turtle
turtle.bgcolor("black")  # background colour
turtle.pensize(2)  # pen size
turtle.color('silver')
turtle.speed(50)  # speed on pen

# Draw a square
# turtle.forward(50)  # moves forward
# turtle.left(90)  # moves left
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()  # Turtle stays on the screen

# Nice little project - create a nice graph
# for colours in ['red', 'blue', 'red', 'blue', 'red', 'blue']:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# for i in range(6):
#     for colours in ['red', 'blue', 'red', 'blue', 'red', 'blue']:
#         turtle.color(colours)
#         turtle.circle(150)
#         turtle.left(10)
# turtle.done()

# draw avenger's logo
turtle.circle(85)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
x = 0
y = 250
turtle.goto(x, y)
turtle.done()