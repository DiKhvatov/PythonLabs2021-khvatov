from random import randint
import turtle

N = 25
dt = 0.1
Vx = []
Vy = []
X = []
Y = []
eps = 15

#границы
turtle.penup()
turtle.goto(-400, -400)
turtle.pendown()
turtle.goto(-400, +400)
turtle.goto(+400, +400)
turtle.goto(+400, -400)
turtle.goto(-400, -400)
#
pool = [turtle.Turtle(shape='circle') for i in range(N)]

for i in range(len(pool)):
	pool[i].penup()
	pool[i].speed(0)
	X.append(randint(-400, 400))
	Y.append(randint(-400, 400))
	Vx.append(randint(-150, 150))
	Vy.append(randint(-150, 150))
	pool[i].goto(X[i], Y[i])

while 0 < 1:
	for j in range(len(pool)):
		#collisions from horizontal up
		if (abs(400 - Y[j]) < eps) and (Vy[j] > 0):
			Vy[j] = -Vy[j]
		#collisions from horizontal down
		elif (abs(-400 - Y[j]) < eps) and (Vy[j] < 0):
			Vy[j] = -Vy[j]
		#collisions from vertical right
		elif (abs(400 - X[j]) < eps) and (Vx[j] > 0):
			Vx[j] = -Vx[j]
		#collisions from vertical left
		elif (abs(-400 - X[j]) < eps) and (Vx[j] < 0):
			Vx[j] = -Vx[j]
		X[j] += Vx[j] * dt
		Y[j] += Vy[j] * dt
		pool[j].goto(X[j], Y[j])
