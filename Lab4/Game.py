import pygame
import json
from pygame.draw import *
from random import randint
from random import choice
from pygame import mixer

class Ball:
	def __init__(self):
		self.x = randint(100, 1100)
		self.y = randint(100, 650)
		self.r = randint(20, 50)
		self.v_x = randint(-10, 10)
		self.v_y = randint(-10, 10)
		self.color = choice(COLORS)

	def draw(self, surface):
		circle(surface, self.color, (int(self.x + 0.5), int(self.y + 0.5)), (self.r))

	def move(self):
		self.x += self.v_x
		self.y += self.v_y

	def collision(self):
		if self.x <= self.r or self.x >= 1200 - self.r:
			self.v_x *= -1
		if self.y <= self.r or self.y >= 750 - self.r:
			self.v_y *= -1

	def interaction(self, pool, j):
		for i, other in enumerate(pool):
			if i <= j:
				continue
			elif ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5 <= (other.r + self.r):
				m_1 = (self.r)**2
				m_2 = (other.r)**2
				cos = (other.x - self.x) / (other.r + self.r)
				sin = (other.y - self.y) / (other.r + self.r)
				v_t1 = (self.v_x) * cos + (self.v_y) * sin
				v_n1 = (self.v_x) * sin - (self.v_y) * cos
				v_t2 = (other.v_x) * cos + (other.v_y) * sin
				v_n2 = (other.v_x) * sin - (other.v_y) * cos
				v_t1b = ((2 * m_2 * v_t2) + (v_t1) * (m_1 - m_2)) / (m_1 + m_2)
				v_n1b = v_n1
				v_t2b = ((2 * m_1 + v_t1) + (v_t2) * (m_2 - m_1)) / (m_1 + m_2)
				v_n2b = v_n2
				self.v_x = v_n1b * sin + v_t1b * cos
				self.v_y = v_n1b * (-cos) + v_t1b * sin
				other.v_x = v_n2b * sin + v_t2b * cos
				other.v_y = v_n2b * (-cos) + v_t2b * sin

	def hit(self, pos, pool, p):
		global score
		if ((pos[0] - self.x)**2 + (pos[1] - self.y)**2)**0.5 <= (self.r) * (5/6):
			click_Sound = mixer.Sound('click.wav')
			click_Sound.play()
			score += 1
			self.x = randint(100, 1100)
			self.y = randint(100, 650)
			stop = True
			while stop:
				for i, other in enumerate(pool):
					if i == p:
						continue
					elif ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5 <= (other.r + self.r):
						self.x = randint(100, 1100)
						self.y = randint(100, 650)
					else:
						stop = False
			self.v_x = randint(-10, 10)
			self.v_y = randint(-10, 10)

class JS:
	def __init__(self):
		self.x = randint(100, 1100)
		self.y = randint(100, 650)
		self.l = randint(50, 70)
		self.v_x = randint(-8, 8)
		self.v_y = randint(-8, 8)

	def draw(self, screen):
		screen.blit(pygame.transform.scale(JS_img, (self.l, int(1.28 * self.l))), (self.x, self.y))

	def move(self):
		self.x += self.v_x
		self.y += self.v_y

	def collision(self):
		if self.x <= 0 or self.x >= 1200 - self.l:
			self.v_x *= -1
		if self.y <= 0 or self.y >= 750 - int(1.28 * self.l):
			self.v_y *= -1
	def flucts(self):
		self.v_x += randint(-1, +1)
		self.v_y += randint(-1, +1)

	def hit(self, pos):
		global score, opacity
		if ((pos[0] >= self.x) and (pos[0] <= self.x + self.l)) and ((pos[1] >= self.y) and (pos[1] <= self.y + int(1.28 * self.l))):
			score += 20
			opacity += 15
			Quotes[randint(0, len(Quotes) - 1)].play()
			self.x = randint(100, 1100)
			self.y = randint(100, 650)


#picture opacity
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)


#initialization
pygame.init()

#some numerical constants and lists
balls = []
jss = []
FPS = 120
screen = pygame.display.set_mode((1200, 750))
score = 0

#import JS face and other
JS_img = pygame.image.load('JhzS.png')
pygame.display.set_caption('Catch the Ball!')
font = pygame.font.Font('freesansbold.ttf', 32)
J_the_big_S = pygame.image.load('bigjs.png')
J_the_pic_S = pygame.transform.scale(J_the_big_S, (575, 750))
Js_cords = [312, 0]
opacity = 0

#determining colors
AMBER = (254, 124, 0)
BANANA_YELLOW = (255, 216, 50)
TIFFANY_BLUE = (0, 180, 171)
MEDIUM_PERSIAN_BLUE = (2, 105, 164)
OXFORD_BLUE = (1, 27, 86)
BLACK = (0, 0, 0)
COLORS = [AMBER, BANANA_YELLOW, TIFFANY_BLUE, MEDIUM_PERSIAN_BLUE, OXFORD_BLUE]

#JS quotes

q1 = mixer.Sound('./Sounds/JS_qts/q1.wav')
q2 = mixer.Sound('./Sounds/JS_qts/q2.wav')
q3 = mixer.Sound('./Sounds/JS_qts/q3.wav')
q4 = mixer.Sound('./Sounds/JS_qts/q4.wav')
q5 = mixer.Sound('./Sounds/JS_qts/q5.wav')
Quotes = [q1, q2, q3, q4, q5]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

#creating balls
for i in range(randint(10, 30)):
	balls.append(Ball())

#creating JSs
for i in range(randint(1, 4)):
	jss.append(JS())

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			for p in range(len(balls)):
				balls[p].hit(pos, balls, p)
			for p in range(len(jss)):
				jss[p].hit(pos)
	for j in range(len(balls)):
		balls[j].draw(screen)
		balls[j].move()
		balls[j].collision()
		balls[j].interaction(balls, j)
	for j in range(len(jss)):
		jss[j].draw(screen)
		jss[j].move()
		jss[j].collision()
		jss[j].flucts()
	blit_alpha(screen, J_the_pic_S, Js_cords, opacity)
	text = font.render("Score " + str(score), True, (254, 124, 0), (1, 27, 86))
	textRect = text.get_rect()
	textRect.center = (70, 20)
	screen.blit(text, textRect)
	pygame.display.update()
	screen.fill(BLACK)

name = input('Type your name')

with open('records.json', 'r') as file:
	records = json.load(file)

records['name'].append(name)
records['points'].append(score)
scores = records

with open('records.json', 'w') as file:
	records = json.dump(records, file, indent = 2)

screen = pygame.display.set_mode((800, 750))

finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
	lb = font.render('Leaderboard', True, (254, 124, 0), (1, 27, 86))
	lbRect = lb.get_rect()
	lbRect.center = (400, 30)
	screen.blit(lb, lbRect)
	for i in range(len(scores['name'])):
		pos = font.render(scores['name'][i]+' - '+str(scores['points'][i]), True, AMBER, OXFORD_BLUE)
		posRect = pos.get_rect()
		posRect.center = (400, 80 + i*int(680/(len(scores['name']))))
		screen.blit(pos, posRect)
	pygame.display.update()
	screen.fill(BLACK)

pygame.quit()









