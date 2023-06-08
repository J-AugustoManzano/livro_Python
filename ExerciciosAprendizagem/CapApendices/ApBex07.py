from turtle import *

speed(0)

def petala():
    for x in range(90):
        fd(1)
        rt(1)
    rt(90)
    for x in range(90):
        fd(1)
        rt(1)

def flor():
    for x in range(8):
        petala()
        rt(45)

flor()
