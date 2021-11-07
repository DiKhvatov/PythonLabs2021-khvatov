import math
from random import choice, randint
import pygame

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

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
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
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        

    def draw(self):
        pygame.draw.circle(screen, self.color, (40, 450), 20)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
            elif self.f2_power == 70:
                self.color = RED
        else:
            self.color = GREY


class Target_1:
    def __init__(self):
        """ 
        Инициализация новой цели. 
        y_1, y_0 - координаты максимального отклонения цели при её движении
        """
        self.x = randint(625, 775)
        self.y_0 = randint(200, 550)
        self.y_1 = randint(200, 550)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.r = randint(10, 25)
        self.live = 1
        self.points = 1
        self.phase = 0
        color = self.color = RED

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(625, 780)
        self.y_0 = randint(300, 550)
        self.y_1 = randint(300, 550)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.r = randint(10, 25)
        self.phase = 0
        self.live = 1

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1

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
        self.x_0 = randint(450, 650)
        self.y_0 = randint(100, 565)
        self.y_1 = randint(100, 565)
        self.x_1 = randint(500, 650)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.x = int((self.x_0 + self.x_1) / 2)
        self.r = randint(10, 25)
        self.live = 1
        self.points = 1
        self.phase = 0
        self.delta = randint(0, 314) / 100
        color = self.color = MAGENTA

    def new_target(self):
        """ Инициализация новой цели. """
        self.x_0 = randint(450, 650)
        self.y_0 = randint(100, 565)
        self.y_1 = randint(100, 565)
        self.x_1 = randint(500, 650)
        self.y = int((self.y_0 + self.y_1) / 2)
        self.x = int((self.x_0 + self.x_1) / 2)
        self.r = randint(10, 25)
        self.phase = 0
        self.delta = randint(0, 314) / 100
        self.live = 1

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x = int(((self.x_0 + self.x_1)/2) + ((self.x_1 - self.x_0)/2) * math.sin(self.phase + self.delta))
        self.y = int(((self.y_0 + self.y_1)/2) + ((self.y_1 - self.y_0)/2) * math.sin(self.phase))
        self.phase += 0.05


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target_1()
target_2 = Target_2()
targets = [target_1, target_2]
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target_1.draw(screen)
    target_1.move()
    target_2.draw(screen)
    target_2.move()
    for b in balls:
        b.draw()
    pygame.display.update()

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

    for i, b in enumerate(balls):
        b.move()
        b.collision()
        b.delete(balls, i)
        for target in targets:    
            if b.hittest(target) and target.live == 1:
                target.live = 0
                target.hit()
                target.new_target()
    gun.power_up()

pygame.quit()
