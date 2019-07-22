import pygame
import sys

# Dimenziji okna
screenW = 500
screenH = 500

# Slika sveta oz. igralnega polja
world = pygame.image.load("world.png")
worldW = world.get_width()
worldH = world.get_height()

# Zamik zgornjega levega kota izrisane slike
# Na začetku je nastavljen tako, da okno prikazuje sredino sveta
offsetX = int(worldW / 2 - screenW / 2)
offsetY = int(worldH / 2 - screenH / 2)

offsetAmount = 1 # Za koliko se ob pritisku puščice zamakne pogled

pygame.init()

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Pirates")

while True:

    for event in pygame.event.get():
        # Če je uporabnik kliknil na gumb za zaprtje okna, konča program
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
        
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
                            

    screen.fill((0, 0, 0))
    screen.blit(world, (0, 0), (offsetX, offsetY, screenW, screenH))
    pygame.display.update()
