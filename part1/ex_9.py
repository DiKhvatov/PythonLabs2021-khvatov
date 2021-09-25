import turtle
import math

r = 25

def n_agon(n, l):
	ang_0 = 180.0 * ((n - 2.0) / (n))
	d = 2.0 * l * math.cos((ang_0 * ((math.pi) / 180.0)) / (2.0))
	turtle.penup()
	turtle.forward(l)
	turtle.left(ang_0 / 2.0)
	turtle.pendown()
	for i in range(n):
		turtle.left(180 - ang_0)
		turtle.forward(d)
	turtle.right(ang_0 / 2.0)
	turtle.penup()
	turtle.goto(0, 0)
	turtle.pendown()

turtle.shape('turtle')
turtle.speed(4)

for i in range(3, 13):
	n_agon(i, (i - 2) * r)

turtle.done()
