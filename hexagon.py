from turtle import *
speed(1000000)
def sestiuhelnik():
    for i in range(6):
        trojuhelnik()
        left(60)

def trojuhelnik():
    for i in range(3):
        forward(300)
        left(120)

sestiuhelnik()
done()