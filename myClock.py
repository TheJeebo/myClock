import turtle
import time
from datetime import datetime

def faceSetup(tT):
    tT.pu()
    tT.back(210)
    tT.pd()
    tT.right(90)
    tT.pensize(3)
    tT.circle(210)
    tT.pu()
    tT.setpos(0,0)

    for i in range(60):
        tT.pu()
        tT.setpos(0,0)
        tT.seth(90)
        tT.right(i * (360/60))
        if i % 5 == 0:
            tT.fd(185)
            tT.pd()
            tT.pensize(3)
            tT.fd(25)
            tT.pu()
        else:
            tT.fd(200)
            tT.pd()
            tT.pensize(1)
            tT.fd(10)
            tT.pu()
    tT.setpos(0,0)
    turtle.update()

def startNew(tT):
    tT.setpos(0,0)
    tT.seth(90)
    tT.clear()

def drawHand(angle, myTurtle, length):
    startNew(myTurtle)
    myTurtle.right(angle)
    myTurtle.fd(length)

def drawTime():
    t5.clear()
    drawBox()
    t5.setpos(0,-100)
    t5.write(datetime.now().strftime('%A, %B %d'),False,'center',('Arial Narrow',12,'bold'))
    t5.setpos(0,-120)
    t5.write(datetime.now().strftime('%I:%M:%S %p'),False,'center',('Arial Narrow',12,'bold'))

def drawBox():
    t5.setpos(-75,-75)
    t5.seth(0)
    t5.pd()
    t5.begin_fill()
    t5.fd(150)
    t5.right(90)
    t5.fd(50)
    t5.right(90)
    t5.fd(150)
    t5.right(90)
    t5.fd(50)
    t5.end_fill()
    t5.pu()

def getSeconds():
    now = datetime.now()
    sinceZero = int((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds())
    return sinceZero

turtle.tracer(0,0)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

t4.speed(0)
t1.color('red')
t1.shape('circle')
t1.shapesize(.5,.5,.5)
t2.shapesize(.1,.1,.1)
t3.shapesize(.1,.1,.1)
t4.shape('circle')
t1.pensize(2)
t2.pensize(4)
t3.pensize(4)

t5.pu()
t5.color('black','light blue')
t5.hideturtle()

turtle.title('This is not a Clock')
turtle.setup(450,450)
faceSetup(t4)

while True:
    turtle.tracer(0,0)
    t = getSeconds()
    drawHand(t * (360/60), t1, 180)
    drawHand(t * (360/3600), t2, 190)
    drawHand(t * (360/43200), t3, 150)
    drawTime()
    turtle.update()
    time.sleep(1)