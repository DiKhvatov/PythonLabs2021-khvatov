import turtle

f = open('output.txt', 'r')
strs = f.readlines()
index = input()
numbers = [[], [], [], [], [], [], [], [], [], []]
r = 20

for j in range(len(strs)):
	for i in range(len(strs[j])):
		if (strs[j])[i] == ",":
			(numbers[j]).append([int((strs[j])[i - 1]), int((strs[j])[i + 1])])

def draw_numb(i, j): 	# i - рисуемая цифра, j - какой по счёту рисуем её 
	dots = numbers[i]
	l = len(dots)
	turtle.penup()
	x, y = dots[0] # перемещаемся в нулевую точку
	turtle.goto(x * r + r * (1 + (2 * j)), y * r)
	turtle.pendown()
	for k in range (1, l, 1):
		x, y = dots[k]
		turtle.goto(x * r + r * (1 + (2 * j)), y * r)

A = [0] * len(index)
for i, num in enumerate(index):
	A[i] = int(num)

turtle.shape('turtle')
turtle.speed(4)

for p in range(len(A)):
	draw_numb(A[p], p)

turtle.done()