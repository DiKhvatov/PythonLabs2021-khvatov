import pygame
from pygame.draw import *
from random import randint
from random import choice
import pygame.freetype

class Ball:
	def __init__(self):
		self.x = randint(100, 1100)
		self.y = randint(100, 650)
		self.r = randint(20, 50)
		self.v_x = randint(-10, 10)
		self.v_y = randint(-10, 10)
		self.color = choice(COLORS)

	def draw(self, surface):
		circle(surface, self.color, (self.x, self.y), (self.r))

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
			elif ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5 <= (other.r + self.r) - 5:
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
			score += 1
			self.x = randint(100, 1100)
			self.y = randint(100, 650)
			stop = true
			while stop:
				for i, other in enumerate(pool, p):
					if i == p:
						continue
					elif ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5 <= (other.r + self.r) - 5:
						self.x = randint(100, 1100)
						self.y = randint(100, 650)
					else:
						stop = false

pygame.init()

balls = []
FPS = 120
screen = pygame.display.set_mode((1200, 750))
score = 0

pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)


AMBER = (254, 124, 0)
BANANA_YELLOW = (255, 216, 50)
TIFFANY_BLUE = (0, 180, 171)
MEDIUM_PERSIAN_BLUE = (2, 105, 164)
OXFORD_BLUE = (1, 27, 86)
BLACK = (0, 0, 0)
COLORS = [AMBER, BANANA_YELLOW, TIFFANY_BLUE, MEDIUM_PERSIAN_BLUE, OXFORD_BLUE]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

for i in range(randint(1, 50)):
	balls.append(Ball())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
        	pos = pygame.mouse.get_pos()
        	for p in range(len(balls)):
        		balls[p].hit(pos, balls, p)
    for j in range(len(balls)):
    	balls[j].draw(screen)
    	balls[j].move()
    	balls[j].collision()
    	balls[j].interaction(balls, j)
    text = font.render("Score " + str(score), True, (254, 124, 0), (1, 27, 86))
    textRect = text.get_rect()
    textRect.center = (70, 20)
    screen.blit(text, textRect)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()









