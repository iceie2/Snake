import turtle
import time
import random

delay = 0.1
score = 0

#screen
wn = turtle.Screen()
wn.title ("snake")
wn.bgcolor("Gray")
wn.setup(width=600, height=600)

#head
head = turtle.Turtle()
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)

#body

#food
food = turtle.Turtle()

#Move the snake

#collision




wn.mainloop()
