import pygame
import sys

# Game window dimensions
screenW = 500
screenH = 500

# Player dimensions
playerW = 25
playerH = 25

# Image of the game world
world = pygame.image.load("world.png")
worldW = world.get_width()
worldH = world.get_height()

# Offset of the drawn image
# Initially set to show the center of the game world
offsetX = int(worldW / 2 - screenW / 2)
offsetY = int(worldH / 2 - screenH / 2)

offsetAmount = 1

pygame.init()

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Pirates")

while True:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]: # move player left
        if offsetX >= offsetAmount:
            offsetX -= offsetAmount
        else:
            offsetX = 0
    if keys[pygame.K_d]: # move player right
        if offsetX + offsetAmount <= worldW - screenW:
            offsetX += offsetAmount
        else:
            offsetX = worldW - screenW
    if keys[pygame.K_w]: # move player up
        if offsetY >= offsetAmount:
            offsetY -= offsetAmount
        else:
            offsetY = 0
    if keys[pygame.K_s]: # move player down
        if offsetY + offsetAmount <= worldH - screenH:
            offsetY += offsetAmount
        else:
            offsetY = worldH - screenH

    for event in pygame.event.get():
        # Kill the program when requested by the user
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0)) # Clears the screen
    screen.blit(world, (0, 0), (offsetX, offsetY, screenW, screenH)) # Draws the world
    pygame.draw.rect(screen, (0, 0, 0), (screenW / 2 - playerW / 2, screenH / 2 - playerH / 2, playerW, playerH))

    pygame.display.update()
