import turtle
tat = turtle.Turtle()

tat.speed(0)
tat.shape("turtle")

def samambaia(folhas):
    if (folhas > 4):
        tat.fd(folhas / 25)
        tat.lt(80)
        samambaia(folhas * 0.3)
        tat.rt(82)
        tat.fd(folhas / 25)
        tat.rt(80)
        samambaia(folhas * 0.3)
        tat.lt(78)
        samambaia(folhas * 0.9)
        tat.lt(2)
        tat.bk(folhas / 25)
        tat.lt(2)
        tat.bk(folhas / 25)

samambaia(300)
