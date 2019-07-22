import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pirates")

while True:

    for event in pygame.event.get():
        # Če je uporabnik kliknil na gumb za zaprtje okna, konča program
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), (225, 225, 50, 50))
    pygame.display.update()
