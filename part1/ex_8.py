import turtle

N = 60
A = 10
turtle.shape('turtle')
turtle.speed(0)

for i in range(N):
	turtle.forward(A*(i+1))
	turtle.left(90)
	turtle.forward(A*(i+1))
	turtle.left(90)

turtle.done()