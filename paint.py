from turtle import *
from city import *

t = Turtle()
t.color('blue')
t.shape('circle')
t.width(5)
t.speed(3)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def setGreen():
    t.color('green')


def setBlue():
    t.color('blue')

def setRed():
    t.color('red')

def stepRight():
    t.goto(t.xcor() + 5,t.ycor())

def stepUp():
    t.goto(t.xcor(),t.ycor() + 5)

def stepDown():
    t.goto(t.xcor(),t.ycor() - 5)

def stepleft():
    t.goto(t.xcor() - 5,t.ycor())

def circle():
    t.circle(100)

scr = t.getscreen()
scr.listen()
#цвет
scr.onkey(setRed, 'r')
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
# СТРЕЛКИ
scr.onkey(stepDown, 'Down')
scr.onkey(stepUp, 'Up')
scr.onkey(stepRight, 'Right')
scr.onkey(stepleft, 'Left')
#КРУГ
scr.onkey(circle, 'c')
scr.onkey(draw_houes, 'd')

scr = t.getscreen()
scr.onscreenclick(move)
#ПЕРЕТАСКИВАНИЕ МЫШИ
t.ondrag(draw)
