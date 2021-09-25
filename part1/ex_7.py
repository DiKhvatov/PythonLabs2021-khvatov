import math
import turtle

k = 0
r_0 = 5
delta = 0.01
N = 100000

def arc(k):
	ang_k1 = 2 * (math.pi) + delta * (k + 1)
	r_k1 = ((r_0) * ang_k1) / (2 * math.pi)
	turtle.goto(((r_k1) * math.cos(ang_k1)), ((r_k1) * math.sin(ang_k1)))

turtle.shape('turtle')
turtle.penup()
arc(-1)
turtle.pendown()

for i in range(N):
	arc(i)

turtle.done()