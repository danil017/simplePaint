from turtle import *

def draw_houes():
    color('black')
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    left(90)
    forward(100)
    right(90)
    color('blue')
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(6)
        left(90)
    end_fill()
def window(side):
    begin_fill()
    for i in range(4):
        forward(side)
        left(90)
    end_fill()
def day():
    #допиши функцию
    speed(0)
    color('yellow')
    begin_fill()
    for i in range(18):
        forward(30)
        left(100)
    end_fill()
