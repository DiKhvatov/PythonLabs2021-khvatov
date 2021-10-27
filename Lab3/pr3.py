import pygame
from pygame.draw import *

def draw_a_fence(x0, y0, scale):
	#рисует забор 300 на 180 в левым верхним краем в точке x0 y0 в масштабе scale
	rect(screen, (203, 174, 0), (x0, y0, 300 * scale, 180 * scale))
	h = (300 * scale) / 16
	for i in range(16 + 1):
		line(screen, (0, 0, 0), (x0 + i * h, y0), (x0 + i * h, y0 + 180 * scale))

def dog_left(x0, y0, scale):
    #body

    ellipse(screen, (107, 103, 85), (x0 + scale * (60 - 55), y0 + scale * 24, 2 * 55 * scale, 62 * scale))
    ellipse(screen, (107, 103, 85), (x0 + scale * (60 - 52 + 67), y0 + scale * (24 - 12), 2 * 0.75 * 52 * scale, 0.75 * 62 * scale))

    #front legs

    ellipse(screen, (107, 103, 85), (x0 + scale * (-5), y0 + scale * (44), scale * 30, scale * 75))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-23), y0 + scale * (110), scale * 42, scale * 17))
    #front legs outline
    ellipse(screen, (107, 103, 85), (x0 + scale * (-5 + 55), y0 + scale * (44 + 23), scale * 30, scale * 75))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-23 + 55), y0 + scale * (110 + 23), scale * 42, scale * 17))

    #back legs

    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20), y0 + scale * (14), scale * 40, scale * 47))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 31), y0 + scale * (14 + 30), scale * 12, scale * 45))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 12), y0 + scale * (14 + 30 + 40.5), scale * 25, scale * 12))
    #back legs outline
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 59), y0 + scale * (14 + 19), scale * 40, scale * 47))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 31 + 59), y0 + scale * (14 + 30 + 19), scale * 12, scale * 45))
    ellipse(screen, (107, 103, 85), (x0 + scale * (84 - 20 + 12 + 59), y0 + scale * (14 + 30 + 40.5 + 19), scale * 25, scale * 12))

    #head

    pygame.draw.rect(screen, (107, 103, 85), (x0, y0, 60 * scale, 70 * scale)) #head
    pygame.draw.rect(screen, (0, 0, 0), (x0, y0, 60 * scale, 70 * scale), 1) #head outline
    ellipse(screen, (107, 103, 85), (x0 - 7 * scale, y0, 14 * scale, 20 * scale)) #left ear
    ellipse(screen, (0, 0, 0), (x0 - 7 * scale, y0, 14 * scale, 20 * scale), 1)  # left ear outline
    ellipse(screen, (107, 103, 85), (x0 + 60 * scale - 7 * scale, y0, 14 * scale, 20 * scale)) #right ear
    ellipse(screen, (0, 0, 0), (x0 + 60 * scale - 7 * scale, y0, 14 * scale, 20 * scale), 1)  # right ear outline

    #eyes

    #left eye
    ellipse(screen, (255, 255, 255), (x0 + scale * (-11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5))
    ellipse(screen, (0, 0, 0), (x0 + scale * (-11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5), 1)
    ellipse(screen, (0, 0, 0), (x0 + scale * (-11 + (-3) + 30), y0 + scale * (25 + 0.5), scale * 6, scale * 4))
    #right eye
    ellipse(screen, (255, 255, 255), (x0 + scale * (11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5))
    ellipse(screen, (0, 0, 0), (x0 + scale * (11 - 6.5 + 30), y0 + scale * 25, scale * 13, scale * 5), 1)
    ellipse(screen, (0, 0, 0), (x0 + scale * (11 + (-3) + 30), y0 + scale * (25 + 0.5), scale * 6, scale * 4))

    #mouth

    arc(screen, (0, 0, 0), (x0 + scale * (30 - 21), y0 + scale * (65 - 15), 42 * scale, 30 * scale), 0.45, 2.69, 2)
    polygon(screen, (255, 255, 255), [(x0 + scale * (15), y0 + scale * (54)), (x0 + scale * (17), y0 + scale * (44)), (x0 + scale * (19), y0 + scale * (52)), (x0 + scale * (15), y0 + scale * (54))])
    polygon(screen, (255, 255, 255), [(x0 + scale * (45), y0 + scale * (54)), (x0 + scale * (43), y0 + scale * (44)), (x0 + scale * (41), y0 + scale * (52)), (x0 + scale * (45), y0 + scale * (54))])
    polygon(screen, (0, 0, 0), [(x0 + scale * (15), y0 + scale * (54)), (x0 + scale * (17), y0 + scale * (44)), (x0 + scale * (19), y0 + scale * (52)), (x0 + scale * (15), y0 + scale * (54))], 1)
    polygon(screen, (0, 0, 0), [(x0 + scale * (45), y0 + scale * (54)), (x0 + scale * (43), y0 + scale * (44)), (x0 + scale * (41), y0 + scale * (52)), (x0 + scale * (45), y0 + scale * (54))], 1)

def dog_right(x0, y0, scale):
    #body

    ellipse(screen, (107, 103, 85), (x0 + scale * (-115), y0 + scale * 24, 2 * 55 * scale, 62 * scale))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-153), y0 + scale * (24 - 12), 2 * 0.75 * 52 * scale, 0.75 * 62 * scale))

    #front legs

    ellipse(screen, (107, 103, 85), (x0 + scale * (-25), y0 + scale * (44), scale * 30, scale * 75))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-19), y0 + scale * (110), scale * 42, scale * 17))
    #front legs outline
    ellipse(screen, (107, 103, 85), (x0 + scale * (-80), y0 + scale * (44 + 23), scale * 30, scale * 75))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-74), y0 + scale * (110 + 23), scale * 42, scale * 17))

    #back legs

    ellipse(screen, (107, 103, 85), (x0 + scale * (-104), y0 + scale * (14), scale * 40, scale * 47))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-107), y0 + scale * (14 + 30), scale * 12, scale * 45))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-101), y0 + scale * (14 + 30 + 40.5), scale * 25, scale * 12))
    #back legs outline
    ellipse(screen, (107, 103, 85), (x0 + scale * (-163), y0 + scale * (14 + 19), scale * 40, scale * 47))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-166), y0 + scale * (14 + 30 + 19), scale * 12, scale * 45))
    ellipse(screen, (107, 103, 85), (x0 + scale * (-160), y0 + scale * (14 + 30 + 40.5 + 19), scale * 25, scale * 12))

    #head

    pygame.draw.rect(screen, (107, 103, 85), (x0 + scale * (-60), y0, 60 * scale, 70 * scale)) #head
    pygame.draw.rect(screen, (0, 0, 0), (x0 + scale*(-60), y0, 60 * scale, 70 * scale), 1) #head outline
    ellipse(screen, (107, 103, 85), (x0 + scale * (-67) , y0, 14 * scale, 20 * scale)) #left ear
    ellipse(screen, (0, 0, 0), (x0 + scale * (-67), y0, 14 * scale, 20 * scale), 1)  # left ear outline
    ellipse(screen, (107, 103, 85), (x0 + scale * (-7), y0, 14 * scale, 20 * scale)) #right ear
    ellipse(screen, (0, 0, 0), (x0 + scale * (-7), y0, 14 * scale, 20 * scale), 1)  # right ear outline
    #eyes

    #left eye
    ellipse(screen, (255, 255, 255), (x0 + scale * (-25.5), y0 + scale * 25, scale * 13, scale * 5))
    ellipse(screen, (0, 0, 0), (x0 + scale * (-25.5), y0 + scale * 25, scale * 13, scale * 5), 1)
    ellipse(screen, (0, 0, 0), (x0 + scale * (-22), y0 + scale * (25 + 0.5), scale * 6, scale * 4))
    #right eye
    ellipse(screen, (255, 255, 255), (x0 + scale * (-47.5), y0 + scale * 25, scale * 13, scale * 5))
    ellipse(screen, (0, 0, 0), (x0 + scale * (-47.5), y0 + scale * 25, scale * 13, scale * 5), 1)
    ellipse(screen, (0, 0, 0), (x0 + scale * (-44), y0 + scale * (25 + 0.5), scale * 6, scale * 4))

    #mouth

    arc(screen, (0, 0, 0), (x0 + scale * (30 - 21 - 60), y0 + scale * (65 - 15), 42 * scale, 30 * scale), 0.45, 2.69, 2)
    polygon(screen, (255, 255, 255), [(x0 + scale * (-45), y0 + scale * (54)), (x0 + scale * (-43), y0 + scale * (44)), (x0 + scale * (-41), y0 + scale * (52)), (x0 + scale * (-45), y0 + scale * (54))])
    polygon(screen, (255, 255, 255), [(x0 + scale * (-15), y0 + scale * (54)), (x0 + scale * (-17), y0 + scale * (44)), (x0 + scale * (-19), y0 + scale * (52)), (x0 + scale * (-15), y0 + scale * (54))])
    polygon(screen, (0, 0, 0), [(x0 + scale * (-45), y0 + scale * (54)), (x0 + scale * (-43), y0 + scale * (44)), (x0 + scale * (-41), y0 + scale * (52)), (x0 + scale * (-45), y0 + scale * (54))], 1)
    polygon(screen, (0, 0, 0), [(x0 + scale * (-15), y0 + scale * (54)), (x0 + scale * (-17), y0 + scale * (44)), (x0 + scale * (-19), y0 + scale * (52)), (x0 + scale * (-15), y0 + scale * (54))], 1)

pygame.init()
screen = pygame.display.set_mode((800, 1000))


#background

pygame.draw.rect(screen, (60, 189, 215), (0, 0, 800, 250))
pygame.draw.rect(screen, (0, 209, 107), (0, 250, 800, 750))

#рисуем заборы

draw_a_fence(240, 20, 1.9)
draw_a_fence(0, 190, 1.25)
draw_a_fence(400, 250, 1.3)
draw_a_fence(-32, 290, 1.3)

#пёсель за будкой

dog_right(760, 550, 1.1)

#cab

polygon(screen, (217, 173, 0), [(512, 684), (586, 590), (652, 716), (512, 684)])
polygon(screen, (217, 173, 0), [(586, 590), (636, 562), (696, 672), (652, 716), (586, 590)])
polygon(screen, (203, 174, 0), [(512, 684), (512, 830), (652, 900), (652, 716), (512, 684)])
polygon(screen, (203, 174, 0), [(652, 716), (696, 672), (696, 806), (652, 900), (652, 716)])
#cab outline
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

#cabhole

rect = pygame.Rect(0, 0, 65, 100)
surf = pygame.Surface(rect.size).convert_alpha()
pygame.draw.ellipse(surf, (0, 0, 0), rect)
rotated_surf = pygame.transform.rotate(surf, 20)
screen.blit(rotated_surf, (535, 710))
pygame.display.flip()

#пёсели

dog_left(50, 450, 1.25)
dog_left(550, 740, 4)
dog_right(350, 650, 1.5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()  