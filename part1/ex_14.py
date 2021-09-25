import math
import turtle

N = int(input())
R = 100
phi = (math.pi) / 2

turtle.shape('turtle')
turtle.penup()
turtle.goto(R * (math.cos(phi)), R * (math.sin(phi)))
turtle.pendown()

for i in range(N):
	phi = phi + ((2 * (math.pi)) / (N)) * ((N - 1) / 2)
	turtle.goto(R * (math.cos(phi)), R * (math.sin(phi)))

turtle.done()