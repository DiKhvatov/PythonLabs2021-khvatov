import turtle


r = 15


numbers = [
	[(0, 0), (r, 0), (r, -2*r), (0, -2*r), (0, 0)],
	[(0, -r), (r, 0), (r, -2*r)],
	[(0,0), (r, 0), (r, -r), (0, -2*r), (r, -2*r)],
	[(0, 0), (r, 0), (0, -r), (r, -r), (0, -2*r)],
	[(0,0), (0, -r), (r, -r), (r, 0), (r, -2*r)],
	[(r, 0), (0,0), (0, -r), (r, -r), (r, -2*r), (0, -2*r)],
	[(r, 0), (0, -r), (r, -r), (r, -2*r), (0, -2*r), (0, -r)],
	[(0, 0), (r, 0), (0, -r), (0, -2*r)],
	[(0, -r), (0, 0), (r, 0), (r, -2*r), (0, -2*r), (0, -r), (r, -r)],
	[(0, -2*r), (r, -r), (r, 0), (0, 0), (0, -r), (r, -r)],
]


def draw_numb(i, j): 	# i - рисуемая цифра, j - какой по счёту рисуем её 
	dots = numbers[i]
	l = len(dots)
	turtle.penup()
	x, y = dots[0] # перемещаемся в нулевую точку
	turtle.goto((x+r*(1+2*j)), y)
	turtle.pendown()
	for k in range (1, l, 1):
		x, y = dots[k]
		turtle.goto(x + r*(1+2*j), y)

index = input()
A = [0] * len(index)
for i, num in enumerate(index):
	A[i] = int(num)

turtle.shape('turtle')
turtle.speed(4)

for p in range(len(A)):
	draw_numb(A[p], p)

turtle.done()













