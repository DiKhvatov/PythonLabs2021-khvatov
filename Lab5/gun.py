import math
from random import choice, randint
import pygame
import json

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 1200
HEIGHT = 800

move_f = False
move_b = False

class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 0.8

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение (pygame.circle).
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 >= (self.r + obj.r) ** 2:
            return False
        else:
            return True
    
    def collision(self):
        """
        """
        global WIDTH, HEIGHT
        if self.x > WIDTH - self.r:
            self.x = WIDTH - self.r
            self.vx *= -0.55
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy *= -0.55
            self.vx *= 0.55
    def delete(self, list, i):      
        if (abs(self.vy) < 0.02 or abs(self.vx) < 0.02) and self.y > HEIGHT - 5*self.r:
            list.pop(i)

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.t_on = 0
        self.c_l = 0
        self.c_r = 0
        self.time = 0
        self.an = 1
        self.color = GREY
        self.color_g = GREY
        self.l_1x = 120
        self.l_1y = 30
        self.l_2x = 65
        self.l_2y = 10
        self.x = 40
        self.y = HEIGHT-self.l_1y-5
        self.score = 0

    def score_plus(self, point):
        self.score += point

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, int(self.x+self.l_1x/2), self.y)
        new_ball.r += 5
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] != (self.x + self.l_1x/2) and event.pos[1] < self.y:
                self.an = -math.atan((event.pos[1]-self.y) / (event.pos[0]-(self.x + self.l_1x/2)))
                if self.an < 0:
                    self.an = 3.1415 + self.an
        

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.l_1x, self.l_1y))
        pygame.draw.polygon(screen, self.color_g, [(int(self.x+(self.l_1x/2)-(self.l_2y*math.sin(self.an)/2)), 
            int(self.y-(self.l_2y*math.cos(self.an)/2))),
            (int(self.x + self.l_1x/2+(self.l_2y*math.sin(self.an)/2)), 
                int(self.y+(self.l_2y*math.cos(self.an)/2))),
            (int(self.x + self.l_1x/2+(self.l_2y*math.sin(self.an)/2)+(self.l_2x*math.cos(self.an))), 
                int(self.y+(self.l_2y*math.cos(self.an)/2-self.l_2x*math.sin(self.an)))),
            (int(self.x+(self.l_1x/2)-(self.l_2y*math.sin(self.an)/2)+(self.l_2x*math.cos(self.an))), 
                int(self.y-(self.l_2y*math.cos(self.an)/2)-self.l_2x*math.sin(self.an))),
            (int(self.x+(self.l_1x/2)-(self.l_2y*math.sin(self.an)/2)), 
            int(self.y-(self.l_2y*math.cos(self.an)/2)))])
        pygame.draw.circle(screen, self.color, (int(self.x + self.l_1x/2), self.y), self.l_1y)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
            elif self.f2_power == 70:
                self.color_g = RED
        else:
            self.color_g = GREY

    def move_forward(self):
        if self.time == 2 and self.c_r == 1:
            self.x += 3
            self.time = 0 

    def move_backward(self):
        if self.time == 2 and self.c_l == 1:
            self.x -= 3
            self.time = 0

    def wait(self):
        if self.t_on == 1:
            if self.time < 2:
                self.time += 1
            elif self.time == 2:
                pass

class Target_1:
    def __init__(self):
        """ 
        Инициализация новой цели. 
        y_1, y_0 - координаты максимального отклонения цели при её движении
        """
        self.x = randint(625, 1050)
        self.y_0 = randint(150, 650)
        self.y_1 = randint(200, 650)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.r = randint(10, 25)
        self.live = 1
        self.points = 1
        self.phase = 0
        self.color = choice(GAME_COLORS)

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(625, 1050)
        self.y_0 = randint(300, 550)
        self.y_1 = randint(300, 550)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.r = randint(10, 25)
        self.phase = 0
        self.live = 1
        self.color = choice(GAME_COLORS)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.y = int(((self.y_0 + self.y_1)/2) + ((self.y_1 - self.y_0)/2) * math.sin(self.phase))
        self.phase += 0.05

class Target_2:
    def __init__(self):
        """ 
        Инициализация новой цели. 
        y_1, y_0 - координаты максимального отклонения цели при её движении
        """
        self.x_0 = randint(450, 1100)
        self.y_0 = randint(100, 565)
        self.y_1 = randint(100, 565)
        self.x_1 = randint(500, 1100)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.x = int((self.x_0 + self.x_1) / 2)
        self.r = randint(10, 25)
        self.live = 1
        self.points = 2
        self.phase = 0
        self.delta = randint(0, 314) / 100
        self.color = choice(GAME_COLORS)

    def new_target(self):
        """ Инициализация новой цели. """
        self.x_0 = randint(450, 1100)
        self.y_0 = randint(100, 565)
        self.y_1 = randint(100, 565)
        self.x_1 = randint(500, 1100)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.x = int((self.x_0 + self.x_1) / 2)
        self.r = randint(10, 25)
        self.phase = 0
        self.delta = randint(0, 314) / 100
        self.live = 1
        self.color = choice(GAME_COLORS)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x = int(((self.x_0 + self.x_1)/2) + ((self.x_1 - self.x_0)/2) * math.sin(self.phase + self.delta))
        self.y = int(((self.y_0 + self.y_1)/2) + ((self.y_1 - self.y_0)/2) * math.sin(self.phase))
        self.phase += 0.05


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.update()



screen.fill(WHITE)
clock.tick(FPS)

bullet = 0
balls = []
targets_1 = []
targets_2 = []


for i in range(randint(2, 4)):
    targets_1.append(Target_1())
    targets_2.append(Target_2())
targets = targets_1+targets_2

gun = Gun(screen)

font = pygame.font.SysFont("Helvetica Neue", 50)
font_medium = pygame.font.SysFont("Helvetica Neue", 40)


init = True
finished = True
Name = ""

while init:
    screen.fill(WHITE)
    text_hint = font_medium.render("(Hint: use arrows to move your tank)", False, (0, 0, 0))
    text_1 = font.render("Type your name", False, (0, 0, 0))
    text_2 = font.render("Submit", False, (0, 0, 0))
    text_name = font_medium.render(Name, False, (0, 0, 0))
    pygame.draw.rect(screen, BLACK, (int(WIDTH/2 - 3 - text_2.get_width()/2), 480-3, text_2.get_width() + 6, text_2.get_height() + 6), 2)
    screen.blit(text_hint, (int(WIDTH/2 - text_hint.get_width()/2), 90))
    screen.blit(text_1, (int(WIDTH/2 - text_1.get_width()/2), 270))
    screen.blit(text_2, (int(WIDTH/2 - text_2.get_width()/2), 480))
    pygame.draw.rect(screen, BLACK, (WIDTH/2 - 170, 390, 340, 50), 2)
    screen.blit(text_name, (WIDTH/2 - 170 + 3, 390 + 3))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            init = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                Name = Name[:-1]
            elif event.key == pygame.K_SPACE:
                Name += " "
            else:
                Name += pygame.key.name(event.key)
        elif event.type == pygame.MOUSEBUTTONUP:
            if (event.pos[0] > int(WIDTH/2 - text_2.get_width()/2)) and (
            event.pos[0] < int(WIDTH/2 + text_2.get_width()/2)) and (
            event.pos[1] > 480) and (event.pos[1] < 480 + text_2.get_height()):
                init = False
                finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    

    for target in targets:
        target.move()
        target.draw(screen)
    for b in balls:
        b.draw()
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.t_on = 1
                gun.c_r = 1
            elif event.key == pygame.K_LEFT:     
                gun.t_on = 1
                gun.c_l = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.c_r = 0
            elif event.key == pygame.K_LEFT:     
                gun.c_l = 0    

    for i, b in enumerate(balls):
        b.move()
        b.collision()
        b.delete(balls, i)
        for target in targets:    
            if b.hittest(target) and target.live == 1:
                target.live = 0
                gun.score_plus(target.points)
                target.new_target()
    gun.power_up()
    gun.wait()
    gun.move_forward()
    gun.move_backward()

    text_score = font.render("Score: " + str(gun.score), False, (0, 0, 0))
    text_bullets = font.render("Bullets: " + str(bullet), False, (0, 0, 0))
    screen.blit(text_score, (20, 20))
    screen.blit(text_bullets, (20, 70))
    pygame.display.update()

with open('records.json', 'r') as file:
    records = json.load(file)

records['name'].append(Name)
records['points'].append(gun.score)
records['bullets'].append(bullet)
scores = records

with open('records.json', 'w') as file:
    records = json.dump(records, file, indent = 2)

screen = pygame.display.set_mode((800, 750))

finished_ = False

while not finished_:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_ = True
    lb = font.render('Leaderboard', False, (0, 0, 0))
    lbRect = lb.get_rect()
    lbRect.center = (400, 30)
    screen.blit(lb, lbRect)
    for i in range(len(scores['name'])):
        pos = font_medium.render(scores['name'][i]+' - '+str(scores['points'][i])+' Bullets: '+str(scores['bullets'][i]), False, (0, 0, 0,))
        posRect = pos.get_rect()
        posRect.center = (400, 90 + i*int(680/(len(scores['name']))))
        screen.blit(pos, posRect)
    pygame.display.update()

pygame.quit()
