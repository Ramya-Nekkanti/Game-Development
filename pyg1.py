import pygame
pygame.init()
display= pygame.display.set_mode((800,600))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
