import turtle
import math

r = 300.
n = 5000.
S = 180.0*(n-2)
l = 2*r*(math.cos((S/(2*n))*((2*(math.pi))/(360.0))))
ang_0 = S/(2*n)

turtle.speed(0)
turtle.shape('turtle')
turtle.penup()
turtle.forward(r)
turtle.pendown()
turtle.left(ang_0)
for i in range(int(n)):
    turtle.left(180 - 2*ang_0)
    turtle.forward(l)
turtle.done()
