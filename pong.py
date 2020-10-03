#Simple Pong game for practise
# By Prabhat

import turtle
import os


wn = turtle.Screen()
wn.title("Pong by @Prabhat")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0)  # this is used to stop automatic update of window which help to run the game faster


#Score
score_a = 0
#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=1,stretch_len=5)
paddle_a.penup()
paddle_a.goto(0, -270)

#paddle B

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()   # this will not create a line on the screen
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0",align = "center", font=("Arial",24,"normal"))

#Main Function

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_right, "Right")
wn.onkeypress(paddle_a_left, "Left")

#Main game loop
while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}".format(score_a), align="center", font=("Arial", 24, "normal"))

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

#paddel and ball collisions

    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle_a.xcor()  + 40 and ball.xcor() > paddle_a.xcor() -40 ):
        ball.sety(-240)
        ball.dy *= -1
