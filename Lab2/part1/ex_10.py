import math
import turtle

k = int(input())

N = 80
l = 40

def circ_pls(r): 
	ang_0 = 180.0 * ((N - 2.0) / (N))
	d = 2.0 * r * math.cos((ang_0 * ((math.pi) / 180.0)) / (2.0))
	turtle.right((180.0 - ang_0) / 2.0)
	for i in range(N):
		turtle.left(180.0 - ang_0)
		turtle.forward(d)
	turtle.left((180.0 - ang_0) / 2.0)

def circ_mns(r): 
	ang_0 = 180.0 * ((N - 2.0) / (N))
	d = 2.0 * r * math.cos((ang_0 * ((math.pi) / 180.0)) / (2.0))
	turtle.left((180.0 - ang_0) / 2.0)
	for i in range(N):
		turtle.right(180.0 - ang_0)
		turtle.forward(d)
	turtle.right((180.0 - ang_0) / 2.0)

turtle.shape('turtle')
turtle.speed(0)

for j in range(k): #2k - количество лепестков
	circ_pls(l)
	circ_mns(l)
	turtle.left(180.0 / k)

turtle.done()



