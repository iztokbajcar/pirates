import pygame
import sys
import time

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

scrollSpeed = 200  # in pixels per second

pygame.init()

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Pirates")

lastScrollUpdate = time.time()

while True:

    for event in pygame.event.get():
        # Kill the program when needed
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    scrollElapsed = time.time() - lastScrollUpdate

    offsetAmount = scrollSpeed * scrollElapsed
        
    if keys[pygame.K_LEFT]:
        if offsetX >= offsetAmount:
            offsetX -= offsetAmount
        else:
            offsetX = 0
    if keys[pygame.K_RIGHT]:
        if offsetX + offsetAmount <= worldW - screenW:
            offsetX += offsetAmount
        else:
            offsetX = worldW - screenW
    if keys[pygame.K_UP]:
        if offsetY >= offsetAmount:
            offsetY -= offsetAmount
        else:
            offsetY = 0
    if keys[pygame.K_DOWN]:
        if offsetY + offsetAmount <= worldH - screenH:
            offsetY += offsetAmount
        else:
            offsetY = worldH - screenH

    lastScrollUpdate = time.time()

    screen.fill((0, 0, 0)) # Clears the screen
    screen.blit(world, (0, 0), (offsetX, offsetY, screenW, screenH))

    pygame.display.update()
