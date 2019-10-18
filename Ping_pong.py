import turtle
import winsound

#window
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgpic("Game_pic_1.gif")
wn.setup(width=800,height=600)
wn.tracer(0)

#cont=0

#Score
score_a=0
score_b=0

#paddle A
paddle_a = turtle.Turtle()
#paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#B56015")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
#paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#B56015")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("#F7F1FC")
ball.penup()
ball.goto(0,0)

ball.dx=1
ball.dy=1
#Pen

pen = turtle.Turtle()
pen.color("#F5CE0C")

pen.speed(0)
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Player A : 0  Player B : 0", align="center", font=("chisel",30,"bold"))

#moving_paddle A up and down

def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    if y>250:
        paddle_a.sety(250)
    else:
        paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    if y<-250:
        paddle_a.sety(-250)
    else:
        paddle_a.sety(y)

#moing paddle B up and down

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    if y>250:
        paddle_b.sety(250)
    else:
        paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    if y<-250:
        paddle_b.sety(-250)
    else:
        paddle_b.sety(y)

#keyboard_Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

while True:
    wn.update()

    #moving ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Game_sond.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Game_sond.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b), align="center", font=("chisel", 30, "bold"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b), align="center", font=("chisel", 30, "bold"))

    #rebounce

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()>paddle_b.ycor()-50 and ball.ycor()<paddle_b.ycor()+50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Game_sond.wav", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()>paddle_a.ycor()-50 and ball.ycor()<paddle_a.ycor()+50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Game_sond.wav", winsound.SND_ASYNC)

    #cont+=1



turtle.done()