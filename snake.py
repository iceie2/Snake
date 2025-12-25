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
head.direction = "stop"

#body
segments = []

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.shape("circle")
    new_segment.color("blue")
    new_segment.penup()
    segments.append(new_segment)

#food
food = turtle.Turtle()

#Move the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def move_segments():
    # Move each segment to the position of the previous segment (tail follows head)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

#collision




wn.mainloop()
