import pygame
pygame.init()
screen= pygame.display.set_mode((500, 300))  
# Fill the screen with white
screen.fill((255, 255, 255))

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()

# This line says "Draw surf onto the screen at the center"
screen.blit(surf, (250, 150))
pygame.display.flip()