import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pirates")

while True:    
    pygame.draw.rect(screen, (200, 200, 200), (225, 225, 50, 50))
    pygame.display.update()
