import pygame
import sys

# Game window dimensions
screenW = 500
screenH = 500

# Image of the game world
world = pygame.image.load("world.png")
worldW = world.get_width()
worldH = world.get_height()

# Offset of the drawn image
# Initially set to show the center of the game world
offsetX = int(worldW / 2 - screenW / 2)
offsetY = int(worldH / 2 - screenH / 2)

pygame.init()

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Pirates")

while True:

    for event in pygame.event.get():
        # Kill the program when requested by the user
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0)) # Clears the screen
    screen.blit(world, (0, 0), (offsetX, offsetY, screenW, screenH))

    # Renders the minimap
    minimap = world.copy()
    pygame.draw.rect(minimap, (255, 0, 0), (offsetX, offsetY, screenW, screenH), 10)
    screen.blit(pygame.transform.scale(minimap, (100, 100)), (0, 0))
    
    pygame.display.update()
