import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 550))
y2 = 320.
y1 = 85.
x = 0.
l = 400.
N = 16
#background
rect(screen, (60, 189, 215), (0, 0, 400, 85))
rect(screen, (203, 174, 0), (0, 85, 400, 235))
rect(screen, (0, 209, 107), (0, 320, 400, 230))
#fence
line(screen, (0, 0, 0), (x, y1), (l, y1))
line(screen, (0, 0, 0), (x, y2), (l, y2))
h = l / (N - 1)
for i in range(N):
    line(screen, (0, 0, 0), (x, y1), (x, y2))
    x += h
#cab
polygon(screen, (217, 173, 0), [(256, 342), (293, 295), (326, 358), (256, 342)])
polygon(screen, (217, 173, 0), [(293, 295), (318, 281), (348, 336), (326, 358), (293, 295)])
polygon(screen, (203, 174, 0), [(256, 342), (256, 415), (326, 450), (326, 358), (256, 342)])
polygon(screen, (203, 174, 0), [(326, 358), (348, 336), (348, 403), (326, 450), (326, 358)])


polygon(screen, (0, 0, 0), [(293, 295), (318, 281), (348, 336), (326, 358), (293, 295)], 1)
polygon(screen, (0, 0, 0), [(256, 342), (293, 295), (326, 358), (256, 342)], 1)
polygon(screen, (0, 0, 0), [(256, 342), (256, 415), (326, 450), (326, 358), (256, 342)], 1)
polygon(screen, (0, 0, 0), [(326, 358), (348, 336), (348, 403), (326, 450), (326, 358)], 1)


#chain
ellipse(screen, (0, 0, 0), (267, 407, 13, 7), 1)
ellipse(screen, (108, 104, 81), (265, 409, 9, 15))
ellipse(screen, (0, 0, 0), (265, 409, 9, 15), 1)
ellipse(screen, (0, 0, 0), (257, 416, 15, 12), 1)
ellipse(screen, (0, 0, 0), (249, 421, 15, 7), 1)
ellipse(screen, (0, 0, 0), (247, 423, 9, 9), 1)
ellipse(screen, (0, 0, 0), (227, 428, 25, 8), 1)
ellipse(screen, (0, 0, 0), (220, 431, 14, 7), 1)
ellipse(screen, (0, 0, 0), (206, 432, 17, 4), 1)
ellipse(screen, (0, 0, 0), (200, 425, 12, 16), 1)
ellipse(screen, (0, 0, 0), (189, 436, 17, 5), 1)
ellipse(screen, (0, 0, 0), (175, 438, 17, 8), 1)


circle(screen, (0, 255, 0), (200, 175), 100, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()