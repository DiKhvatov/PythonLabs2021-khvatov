from random import *
import turtle

random()
l = 50
n = 1000
def rand():
	r_1 = random()
	r_2 = random()
	turtle.forward(r_1*l)
	turtle.left(360*(r_2-0.5))

turtle.shape('turtle')

for i in range (n):
	rand() 
turtle.done()