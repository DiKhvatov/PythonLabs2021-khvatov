import math
import turtle

N = 100
l_1 = 300
l_2 = 30

blue = "#0000FF"
yellow = "#FFFF00" 
red = "#FF0000"

def circ(r): 
	ang_0 = 180.0 * ((N - 2.0) / (N))
	d = 2.0 * r * math.cos((ang_0 * ((math.pi) / 180.0)) / (2.0))
	turtle.penup()
	turtle.forward(r)
	turtle.pendown()
	turtle.right(ang_0 / 2.0) 
	for i in range(N):
		turtle.right(180.0 - ang_0)
		turtle.forward(d)
	turtle.left(ang_0 / 2.0) 	

def hlf_circ(r): 
	ang_0 = 180.0 * ((N - 2.0) / (N))
	d = 2.0 * r * math.cos((ang_0 * ((math.pi) / 180.0)) / (2.0))
	turtle.penup()
	turtle.forward(r)
	turtle.pendown()
	turtle.right(ang_0 / 2.0) 
	for i in range(int(N / 2)):
		turtle.right(180.0 - ang_0)
		turtle.forward(d)
		
turtle.shape('turtle')

#head
turtle.fillcolor(yellow)
turtle.begin_fill()
circ(l_1)
turtle.end_fill()
#eyes
turtle.penup()
turtle.goto(150, 140)
turtle.pendown()
turtle.fillcolor(blue)
turtle.begin_fill()
circ(l_2)
turtle.end_fill()
turtle.penup()
turtle.goto(-150, 140)
turtle.pendown()
turtle.fillcolor(blue)
turtle.begin_fill()
circ(l_2)
turtle.end_fill()
#nose
turtle.width(25)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(0, -50)
#smile
turtle.color(red)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
hlf_circ(170)

turtle.done()
















