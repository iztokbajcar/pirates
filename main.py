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

offsetAmount = 1

pygame.init()

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Pirates")

# Frame rate
FPS = 3600
lastUpdate = time.time()

while True:

    currentTime = time.time()
    elapsed = currentTime - lastUpdate
    print(elapsed)

    for event in pygame.event.get():
        # Kill the program when requested by the user
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Clears the screen
    screen.blit(world, (0, 0), (offsetX, offsetY, screenW, screenH))

    # Only render the game if the right amount of
    # time (based on the FPS) has elapsed
    if elapsed >= 1 / FPS:
        pygame.display.update()
        lastUpdate = currentTime
