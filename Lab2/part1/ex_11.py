import turtle
import math

N = 100
l = 40.0
d = 10.0
k = int(input()) #k - количество слоёв

def circs(r): 
	ang_0 = 180.0 * ((N - 2.0) / (N))
	d = 2.0 * r * math.cos((ang_0 * ((math.pi) / 180.0)) / (2.0))
	turtle.right((180.0 - ang_0) / 2.0)
	for i in range(N):
		turtle.left(180.0 - ang_0)
		turtle.forward(d)
	turtle.left((180.0 - ang_0) / 2.0)
	turtle.left((180.0 - ang_0) / 2.0)
	for i in range(N):
		turtle.right(180.0 - ang_0)
		turtle.forward(d)
	turtle.right((180.0 - ang_0) / 2.0)

turtle.shape('turtle')
turtle.left(90)

for j in range(k): 
	circs(l + d * j)

turtle.done()



