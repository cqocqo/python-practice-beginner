# My surname in Chinese
import turtle

turtle.color('red')
turtle.bgcolor('black')
turtle.pensize(2)

# kou 1
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

# heng 1 inside the kou
turtle.penup()
x = 0
y = 25
turtle.goto(x,y)
x = 50
y = 25
turtle.pendown()
turtle.goto(x,y)

turtle.penup()
x = 0
y = 75
turtle.goto(x, y)
x = 50
y = 75
turtle.pendown()
turtle.goto(x,y)

turtle.penup()
x = 15
y = 85
turtle.goto(x, y)
turtle.pendown()

x = 15
y = 0
turtle.goto(x,y)

turtle.penup()
x = 35
y = 85
turtle.goto(x,y)
turtle.pendown()

x = 35
y = 0
turtle.goto(x,y)

turtle.penup()
x = 5
y = -15
turtle.goto(x,y)
turtle.pendown()

turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.penup()

x = 0
y = -35
turtle.goto(x, y)
turtle.pendown()

x = 45
y = -35
turtle.goto(x,y)

turtle.done()