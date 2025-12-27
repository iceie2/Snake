import turtle
import time
import random

game_running = False
delay = 0.005
score = 0
high_score = 0

GRID_SIZE = 20
GRid_COLS = 30
GRID_ROWS = 30

#screen
wn = turtle.Screen()
wn.title ("snake")
wn.bgcolor("Gray")
wn.setup(width=700, height=700)

border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.pensize(50)
border_pen.penup()
border_pen.goto(-325, 325)
border_pen.pendown()
for side in range(4):
    border_pen.forward(650)
    border_pen.right(90)
border_pen.penup()

#title
title = turtle.Turtle()
title.hideturtle()
title.speed(0)
title.color("white")
title.goto(0, 310)
title.write("Snake Game! Press Space to Start", align="center", font=("Courier", 24, "normal"))
title.penup()


#head
head = turtle.Turtle()
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

def show_title_screen():
    global game_running
    game_running = False
    title.clear()
    title.goto(0, 50)
    title.write("Snake Game", align="center", font=("Arial", 24, "bold"))
    title.goto(0, 0)
    title.write("Press SPACE to start", align="center", font=("Arial", 16, "normal"))
    title.goto(0, -30)
    title.write(f"High Score: {high_score}", align="center", font=("Arial", 14, "normal"))
    title.goto(0, -60)
    title.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))
    title.showturtle()

def hide_title_screen():
    title.clear()
    title.hideturtle()

#body
segments = []

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.hideturtle()
    new_segment.shape("circle")
    new_segment.color("blue")
    new_segment.penup()
    if segments:
        last_x, last_y = segments[-1].xcor(), segments[-1].ycor()
    else:
        last_x, last_y = head.xcor(), head.ycor()
    new_segment.goto(last_x, last_y)
    new_segment.showturtle()
    segments.append(new_segment)


starting_length = 3

for i in range(starting_length):
    add_segment()
    

positions = []
#food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()

def spawn_food():
    food.hideturtle()

    while True:
        x = random.randint(-13, 13) * 20
        y = random.randint(-13, 13) * 20

        snake_body_positions = [(head.xcor(), head.ycor())] + [(seg.xcor(), seg.ycor()) for seg in segments]
        if (x, y) not in snake_body_positions:
            break
        
    food.goto(x, y)
    food.showturtle()





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
    # Only move segments if we have enough positions stored
    for i in range(len(segments)):
        if len(positions) > (i + 1):
            x, y = positions[-(i + 2)]
            segments[i].goto(x, y)

def check_wall_collision():
    global game_running
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        print("Game Over")
        game_running = False
        show_title_screen()
    
def check_self_collision():
    global game_running
    for segment in segments:
        if segment.distance(head) < 20:
            print("Game Over")
            game_running = False
            show_title_screen()

def check_food_collision():
    global score
    if head.distance(food) < 20:
        add_segment()
        spawn_food()
        score += 10
        high_score_update()

def high_score_update():
    global score
    global high_score
    if score > high_score:
        high_score = score


def game_loop():
    move()
    positions.append((head.xcor(), head.ycor()))
    move_segments()
    check_wall_collision()
    check_self_collision()
    check_food_collision()
    wn.update()
    if game_running:
        wn.ontimer(game_loop, int(delay * 1000))
    

def start_game():
    global game_running, score, positions, segments
    score=0
    hide_title_screen()
    head.hideturtle()
    head.goto(0,0)
    head.direction = "stop"
    # Hide and clear old segments
    for seg in segments:
        seg.hideturtle()
    segments.clear()
    # Reset positions list properly
    positions = []
    # Rebuild starting snake
    for i in range(starting_length):
        add_segment()
    # Seed some initial positions where all parts overlap the head
    for _ in range(starting_length + 5):
        positions.append((head.xcor(), head.ycor()))
    spawn_food()
    head.showturtle()
    game_running = True
    game_loop()
#collision


wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(start_game, "space")



wn.mainloop()