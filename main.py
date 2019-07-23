import pygame
import sys

# Game window dimensions
screenW = 500
screenH = 500

# Player dimensions
playerW = 25
playerH = 25

# Player speed
playerS = 1

# Player position (coordinates of player's top left corner)
playerX = screenW / 2 - playerW / 2
playerY = screenH / 2 - playerH / 2

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

    if keys[pygame.K_a]:  # move player left
        if offsetX == worldW - screenW:  # If the player is on the far right side of the map
            if playerX - playerS >= screenW / 2 - playerW / 2:
                playerX -= playerS
            else:
                playerX = screenW / 2 - playerW / 2
                offsetX -= offsetAmount
        elif offsetX == 0:  # If the player is on the far left side of the map
            if playerX - playerS >= 0:  # The player moves to the left, but the background doesn't move
                playerX -= playerS
            else:
                playerX = 0

        else:
            offsetX -= offsetAmount

    if keys[pygame.K_d]:  # move player right
        if offsetX == worldW - screenW:  # If the player is on the far right side of the map
            if playerX + playerS <= screenW - playerW:  # The player moves to the right, but the background doesn't move
                playerX += playerS
            else:
                playerX = screenW - playerW
        elif offsetX == 0:  # If the player is on the far left side of the map
            if playerX + playerS <= screenW / 2 - playerW / 2:
                playerX += playerS
            else:
                playerX = screenW / 2 - playerW / 2
                offsetX += offsetAmount
        else:
            offsetX += offsetAmount

    if keys[pygame.K_w]:  # move player up
        if offsetY == worldH - screenH:  # If the player is on the far upper side of the map
            if playerY - playerS >= screenH / 2 - playerH / 2:
                playerY -= playerS
            else:
                playerY = screenH / 2 - playerH / 2
                offsetY -= offsetAmount
        elif offsetY == 0:  # If the player is on the far left side of the map
            if playerY - playerS >= 0:  # The player moves up, but the background doesn't move
                playerY -= playerS
            else:
                playerY = 0
        else:
            offsetY -= offsetAmount

    if keys[pygame.K_s]:  # move player down
        if offsetY == worldH - screenH:  # If the player is on the far right side of the map
            if playerY + playerS <= screenH - playerH:  # The player moves to the right, but the background doesn't move
                playerY += playerS
            else:
                playerY = screenH - playerH
        elif offsetY == 0:  # If the player is on the far left side of the map
            if playerY + playerS <= screenH / 2 - playerH / 2:
                playerY += playerS
            else:
                playerY = screenH / 2 - playerH / 2
                offsetY += offsetAmount
        else:
            offsetY += offsetAmount

    for event in pygame.event.get():
        # Kill the program when requested by the user
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Clears the screen
    screen.blit(world, (0, 0), (offsetX, offsetY, screenW, screenH))  # Draws the world
    pygame.draw.rect(screen, (0, 0, 0), (playerX, playerY, playerW, playerH))

    pygame.display.update()
