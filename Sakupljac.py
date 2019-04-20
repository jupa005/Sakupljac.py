#Sakupljac
import turtle
import os
import math
import random
import time

#Postavi ekran
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sakupljac")


#Granice
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Timer

timer=5
timer_pen = turtle.Turtle()
timer_pen.speed(0)
timer_pen.color("white")
timer_pen.penup()
timer_pen.setposition(0,310)
timerString="Vrijeme: %s" %timer
timer_pen.write(timerString, False, align="center",font=("Arial",20,"normal"))
timer_pen.hideturtle()

#Score
score=0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(240,310)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#Igrac
igrac = turtle.Turtle()
igrac.color("white")
igrac.shape("square")
igrac.penup()
igrac.setposition(0,0)
brzinaigraca=15

#Hrana
hrana = turtle.Turtle()
hrana.color("red")
hrana.shape("circle")
hrana.penup()
hrana.speed(0)
x=random.randint(-280,280)
y=random.randint(-280,280)
hrana.setposition(x,y)

#Kretnje igraca
def move_left():
    x=igrac.xcor()
    x-=brzinaigraca
    if x < -280:
        x=-280
    igrac.setx(x)

def move_right():
    x=igrac.xcor()
    x+=brzinaigraca
    if x > 280:
        x=280
    igrac.setx(x)

def move_up():
    y=igrac.ycor()
    y+=brzinaigraca
    if y>280:
        y=280
    igrac.sety(y)

def move_down():
    y=igrac.ycor()
    y-=brzinaigraca
    if y<-280:
        y=-280
    igrac.sety(y)

def is_collision(t1,t2):
    udaljenost= math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if udaljenost < 15:
        return True
    else:
        return False


#keyBinding
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(move_up,"Up")
turtle.onkey(move_down,"Down")


    
while True:
    #Smanjuj timer
    timer-=0.02
    time.sleep(0.001)
    timer_pen.clear()
    timerString="Vrijeme: %s" %timer
    timer_pen.write(timerString, False, align="center",font=("Arial",20,"normal"))  
    if timer<=0:
        timer=0
        timer_pen.clear()
        timerString="Vrijeme: %s" %timer
        timer_pen.write(timerString, False, align="center",font=("Arial",20,"normal")) 
        igrac.hideturtle()
        hrana.hideturtle()
        print("GAME OVER")
        print("Score: "+str(score))
        break
    if is_collision(igrac,hrana):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        hrana.setposition(x,y)
        #Promijeni score
        score+=1
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
        score_pen.hideturtle()
        #Uvecaj timer
        timer+=3
        timer_pen.clear()
        timerString="Vrijeme: %s" %timer
        timer_pen.write(timerString, False, align="center",font=("Arial",20,"normal"))
        
        





turtle.done()



