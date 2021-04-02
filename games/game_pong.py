import turtle # module pour créer les dessins et objets

# creating the board

window = turtle.Screen ()
window.title ("Pong")
window.bgcolor ("black")
window.setup (width = 800, height = 600)
window.tracer (0)

# objects

score_a = 0
score_b = 0

paddle_a = turtle.Turtle ()
paddle_a.speed (0) # moving speed set to the max
paddle_a.shape ("square")
paddle_a.color ("white")
paddle_a.shapesize (stretch_wid = 5, stretch_len = 1)
paddle_a.penup () # éviter d'écrire - juste afficher la forme
paddle_a.goto (-350,0)

paddle_b = turtle.Turtle ()
paddle_b.speed (0) # moving speed set to the max
paddle_b.shape ("square")
paddle_b.color ("white")
paddle_b.shapesize (stretch_wid = 5, stretch_len = 1) # change la forme carrée en rectangle
paddle_b.penup ()
paddle_b.goto (350,0)

ball = turtle.Turtle ()
ball.shape ("square")
ball.color ("white")
ball.penup ()
ball.goto (0, 0)

pen = turtle.Turtle () # crée un objet pen avec turtle
pen. speed (0) # animation speed
pen.color ("white")
pen.penup ()
pen.hideturtle () # don't want to see it - not the same as the ball and the paddles
pen.goto (0, 260)
pen.write ("Player A : %s || Player B : %s" % (score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

# moving the objects

initial_ball_xspeed = 0.1
initial_ball_yspeed = 0.1

ball.xmove = 0.1
ball.ymove = 0.1

def paddle_a_up () :
    y = paddle_a.ycor ()
    y += 30
    paddle_a.sety(y)
    
def paddle_a_down () :
    y = paddle_a.ycor ()
    y -= 30
    paddle_a.sety(y)
    
def paddle_b_up () :
    y = paddle_b.ycor ()
    y += 30
    paddle_b.sety(y)
    
def paddle_b_down () :
    y = paddle_b.ycor ()
    y -= 30
    paddle_b.sety(y)

window.listen ()
window.onkeypress (paddle_a_up, "z")
window.onkeypress (paddle_a_down, "s")
window.onkeypress (paddle_b_up, "Up")
window.onkeypress (paddle_b_down, "Down")

while True : # run the programm
    window.update() # 'refresh' the window
    ball.setx (ball.xcor() + ball.xmove)
    ball.sety (ball.ycor() + ball.ymove)
    if ball.ycor() > 290 :
        ball.sety (290)
        ball.ymove *= -1
    if ball.ycor() < -290 :
        ball.sety (-290)
        ball.ymove *= -1
    if ball.xcor() > 390 :
        score_a += 1
        ball.goto (0, 0)
        ball.xmove = - initial_ball_xspeed
        pen.clear ()
        pen.write ("Player A : %s || Player B : %s" % (score_a, score_b), align = "center", font = ("Courier", 24, "normal"))
    if ball.xcor() < -390 :
        score_b += 1
        ball.goto (0, 0)
        ball.xmove = initial_ball_xspeed
        pen.clear ()
        pen.write ("Player A : %s || Player B : %s" % (score_a, score_b), align = "center", font = ("Courier", 24, "normal"))
        
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40 :
        ball.setx (340)
        ball.xmove *= -1.25
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40 :
        ball.setx (-340)
        ball.xmove *= -1.25