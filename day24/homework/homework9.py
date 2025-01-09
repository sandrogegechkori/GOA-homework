import turtle

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Draw the first square
t.penup()
t.goto(100, 100)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.right(90)

t.penup()
t.goto(-300, 100)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.right(90)

t.penup()
t.goto(-300, -300)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.right(90)

t.penup()
t.goto(100, -300)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.right(90)

t.hideturtle()
screen.mainloop()