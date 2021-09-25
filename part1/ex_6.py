import turtle

r = 150
n = 12
ang_0 = 360.0 / n

def leg():
	turtle.forward(r)
	turtle.stamp()
	turtle.right(180)
	turtle.forward(r)

turtle.shape('turtle')
turtle.speed(0)

for i in range(n):
	leg()
	turtle.right(180)
	turtle.right(ang_0)

turtle.done()
