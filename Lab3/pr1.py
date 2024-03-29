import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

#background
rect(screen, (217, 217, 217), (0, 0, 400, 400))
#face
circle(screen, (251, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
#eyes
circle(screen, (255, 0, 0), (250, 180), 16)
circle(screen, (255, 0, 0), (150, 180), 19)
circle(screen, (0, 0, 0), (250, 180), 16, 1)
circle(screen, (0, 0, 0), (150, 180), 19, 1)
circle(screen, (0, 0, 0), (250, 180), 8)
circle(screen, (0, 0, 0), (150, 180), 8)
#mouth
rect(screen, (0, 0, 0), (150, 250, 100, 20))

#right eyebrow
rect = pygame.Rect(0, 0, 80, 13)
surf = pygame.Surface(rect.size).convert_alpha()
pygame.draw.rect(surf, (0, 0, 0), rect)
rotated_surf = pygame.transform.rotate(surf, 25)
screen.blit(rotated_surf, (220, 131))
pygame.display.flip()
#left eyebrow
rect = pygame.Rect(0, 0, 90, 13)
surf = pygame.Surface(rect.size).convert_alpha()
pygame.draw.rect(surf, (0, 0, 0), rect)
rotated_surf = pygame.transform.rotate(surf, -35)
screen.blit(rotated_surf, (110, 119))
pygame.display.flip()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()