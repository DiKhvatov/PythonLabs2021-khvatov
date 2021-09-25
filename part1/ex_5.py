import turtle

N = 10
A = 15. # A - сторона наименьшего

turtle.shape('turtle')
turtle.speed(0)

def square(a): # a - длина стороны квадрата
	turtle.penup()
	turtle.goto((-a/2), (-a/2))
	turtle.pendown()
	for i in range(4):
		turtle.forward(a)
		turtle.left(90)

for i in range(N): # рисуем
	square(A*(i + 1))
turtle.done()