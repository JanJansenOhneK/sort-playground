
import pygame
import random

pygame.init()
screen_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
running = True

bars = []

""" 
# 1 to 99
for i in range(1,100):
    bars.append(i)

# randomized
for i in range(99):
    bars.append(random.randint(1,99))
"""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((50,50,50))
    for i in range(len(bars)):
        rect = pygame.Rect(10+i*15,screen_size[1]-(bars[i]*10)-80,10,bars[i]*10)
        pygame.draw.rect(screen,(255,255,255),rect)

    pygame.display.flip()


pygame.quit()