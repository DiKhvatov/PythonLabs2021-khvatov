import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1100))
y2 = 640.
y1 = 170.
x = 0.
l = 800.
N = 16

def dog(x0, y0, scale):
    #body

    ellipse(screen, (107, 103, 85), (x0 + scale * (60 - 55), y0 + scale * 24, 2 * 55 * scale, 62 * scale))
    ellipse(screen, (107, 103, 85), (x0 + scale * (60 - 52 + 67), y0 + scale * (24 - 12), 2 * 0.75 * 52 * scale, 0.75 * 62 * scale))

    #front legs

    ellipse(screen, (107, 103, 85), (x0 + scale * (-5), y0 + scale * (44), scale * 35, scale * 75))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-23), y0 + scale * (110), scale * 42, scale * 17))

    ellipse(screen, (107, 103, 85), (x0 + scale * (-5 + 55), y0 + scale * (44 + 23), scale * 35, scale * 75))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-23 + 55), y0 + scale * (110 + 23), scale * 42, scale * 17))

    #back legs

    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20), y0 + scale * (14), scale * 40, scale * 47))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 31), y0 + scale * (14 + 30), scale * 12, scale * 45))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 12), y0 + scale * (14 + 30 + 40.5), scale * 25, scale * 12))

    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 59), y0 + scale * (14 + 19), scale * 40, scale * 47))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 31 + 59), y0 + scale * (14 + 30 + 19), scale * 12, scale * 45))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 12 + 59), y0 + scale * (14 + 30 + 40.5 + 19), scale * 25, scale * 12))

    #head

    rect(screen, (107, 103, 85), (x0, y0, 60 * scale, 70 * scale)) #head
    rect(screen, (0, 0, 0), (x0, y0, 60 * scale, 70 * scale), 1) #head outline
    ellipse(screen, (107, 103, 85), (x0 - 7 * scale, y0, 14 * scale, 20 * scale)) #left ear
    ellipse(screen, (0, 0, 0), (x0 - 7 * scale, y0, 14 * scale, 20 * scale), 1)  # left ear outline
    ellipse(screen, (107, 103, 85), (x0 + 60 * scale - 7 * scale, y0, 14 * scale, 20 * scale)) #right ear
    ellipse(screen, (0, 0, 0), (x0 + 60 * scale - 7 * scale, y0, 14 * scale, 20 * scale), 1)  # right ear outline

    #eyes

    ellipse(screen, (255, 255, 255), (x0 + scale * (-11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5))
    ellipse(screen, (0, 0, 0), (x0 + scale * (-11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5), 1)
    ellipse(screen, (0, 0, 0), (x0 + scale * (-11 + (-3) + 30), y0 + scale * (25 + 0.5), scale * 6, scale * 4))

    ellipse(screen, (255, 255, 255), (x0 + scale * (11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5))
    ellipse(screen, (0, 0, 0), (x0 + scale * (11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5), 1)
    ellipse(screen, (0, 0, 0), (x0 + scale * (11 + (-3) + 30), y0 + scale * (25 + 0.5), scale * 6, scale * 4))

    #mouth

    arc(screen, (0, 0, 0), (x0 + scale * (30 - 21), y0 + scale * (65 - 15), 42 * scale, 30 * scale), 0.45, 2.69, 2)

#background

rect(screen, (60, 189, 215), (0, 0, 800, 170))
rect(screen, (203, 174, 0), (0, 170, 800, 470))
rect(screen, (0, 209, 107), (0, 640, 800, 460))

#fence

line(screen, (0, 0, 0), (x, y1), (l, y1))
line(screen, (0, 0, 0), (x, y2), (l, y2))
h = l / (N - 1)

for i in range(N):
    line(screen, (0, 0, 0), (x, y1), (x, y2))
    x += h

#cab

polygon(screen, (217, 173, 0), [(512, 684), (586, 590), (652, 716), (512, 684)])
polygon(screen, (217, 173, 0), [(586, 590), (636, 562), (696, 672), (652, 716), (586, 590)])
polygon(screen, (203, 174, 0), [(512, 684), (512, 830), (652, 900), (652, 716), (512, 684)])
polygon(screen, (203, 174, 0), [(652, 716), (696, 672), (696, 806), (652, 900), (652, 716)])

polygon(screen, (0, 0, 0), [(586, 590), (636, 562), (696, 672), (652, 716), (586, 590)], 1)
polygon(screen, (0, 0, 0), [(512, 685), (586, 590), (652, 716), (512, 684)], 1)
polygon(screen, (0, 0, 0), [(512, 684), (512, 830), (652, 900), (652, 716), (512, 685)], 1)
polygon(screen, (0, 0, 0), [(652, 716), (696, 672), (696, 806), (652, 900), (652, 716)], 1)

#chain

ellipse(screen, (0, 0, 0), (534, 814, 26, 14), 1)
ellipse(screen, (108, 104, 81), (530, 818, 18, 30))
ellipse(screen, (0, 0, 0), (530, 818, 18, 30), 1)
ellipse(screen, (0, 0, 0), (514, 832, 30, 24), 1)
ellipse(screen, (0, 0, 0), (498, 842, 30, 14), 1)
ellipse(screen, (0, 0, 0), (494, 846, 18, 18), 1)
ellipse(screen, (0, 0, 0), (454, 856, 50, 16), 1)
ellipse(screen, (0, 0, 0), (440, 862, 28, 14), 1)
ellipse(screen, (0, 0, 0), (412, 864, 34, 8), 1)
ellipse(screen, (0, 0, 0), (400, 850, 24, 32), 1)
ellipse(screen, (0, 0, 0), (378, 872, 34, 10), 1)
ellipse(screen, (0, 0, 0), (350, 874, 34, 16), 1)


rect = pygame.Rect(0, 0, 100, 150)
surf = pygame.Surface(rect.size).convert_alpha()
pygame.draw.ellipse(surf, (255, 0, 0), rect, 5)
rotated_surf = pygame.transform.rotate(surf, 70)
screen.fill((0, 0, 0))
screen.blit(rotated_surf, (200, 300))
pygame.display.flip()




dog(100, 720, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()