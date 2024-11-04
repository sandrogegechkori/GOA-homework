from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(6)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left((90))

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill( )
penup()
goto(150, 150)
pendown()
color("blue")
begin_fill()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
exitonclick()