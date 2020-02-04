#I'm using the code from https://www.youtube.com/watch?v=DxVPN1PIuLM and
#improving on it in order to practice
import os
import turtle as tr
import time
import random

#variables
delay = 0.2
snake_speed = 20

#Setting up the screen
wn = tr.Screen()
wn.title("Snake Game by @TiagoS")

wn.bgcolor("Black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = tr.Turtle()
head.speed(0) #animation of the speed module - it is the fastest possible
head.shape("circle")
head.color("white")
head.penup() #so that it doesn't draw anything
head.goto(0,0)
head.direction = "left"

#snake food
food = tr.Turtle()
food.speed(0) #animation of the speed module - it is the fastest possible
food.shape("square")
food.color("red")
food.penup() #so that it doesn't draw anything
food.goto(0,100)

#bodyparts
body_parts = []


#functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

def move():
    global snake_speed
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+snake_speed)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-snake_speed)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-snake_speed)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+snake_speed)

#listener
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")


#Main Game Loop
while True:
    wn.update()

    #Check for collision with the wall
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for body_part in body_parts:
            body_part.goto(1000,1000)
        body_parts.clear()

    #Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add bodyparts
        #create new body part
        new_segment = tr.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        body_parts.append(new_segment)

    #make body parts follow the head
    for index in range(len(body_parts)-1,0,-1):
        x = body_parts[index-1].xcor()
        y = body_parts[index-1].ycor()
        body_parts[index].goto(x,y)

    if len(body_parts)>0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)


    move()

    #check for body collisions
    for body_part in body_parts:
        if body_part.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"
            for body_part in body_parts:
                body_part.goto(1000,1000)
            body_parts.clear()

    time.sleep(delay)


wn.mainloop()
