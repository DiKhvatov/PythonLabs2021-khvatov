import turtle
import math


Vx = 15
Vy = 90 # в t = 0
Gy = -25
dt = 0.05
x = 0
y = 0
eps = 3
turtle.shape('circle')


while 0 < 1:
	if (abs(y) < eps) and (Vy < 0): #отражаемся и теряем часть скорости
		Vy *= (-0.9)
		Vx *= (0.9) 
	x += Vx * dt
	y += Vy * dt + (Gy * ((dt) ** 2)) / 2
	Vy += Gy * dt
	turtle.goto(x, y)
