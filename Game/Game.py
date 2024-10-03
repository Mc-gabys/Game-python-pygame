import pygame
import os
import time

# Initialiser Pygame
pygame.init()

screen = pygame.display.set_mode((1207, 858))

pygame.display.set_caption("Pygame")

# Charger l'image
path_image = os.path.join('/storage/emulated/0/GamePython/sans_no_background.png')
image = pygame.image.load(path_image)
image_rect = image.get_rect()

# Charger le background
fond11 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale11.jpg'))

fond12 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale12.jpg'))

fond13 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale13.jpg'))

fond14 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale14.jpg'))

fond21 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale21.jpg'))

fond22 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale22.jpg'))

fond23 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale23.jpg'))

fond24 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale24.jpg'))

fond31 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale31.jpg'))

fond32 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale32.jpg'))

fond33 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale33.jpg'))

fond34 = pygame.image.load(os.path.join('/storage/emulated/0/GamePython/undertale34.jpg'))

# Obtenir les dimensions de l'écran
width, height = 1207, 858

# Position initiale de l'image
image_rect.center = (1207 // 2, 858 // 2)

# Définir la vitesse de déplacement
speed = 10

background = fond11

# Remplir l'écran avec le background
screen.blit(background, (0, 0))

# Initialiser pygame mixer
pygame.mixer.init()
    
# Charger et jouer le fichier audio
pygame.mixer.music.load(os.path.join('/storage/emulated/0/GamePython/Last_Breath_Sans_Phase_3_An_Enigmatic_Encounter_FDY_Remastered.mp3'))
pygame.mixer.music.play()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtenir les touches pressées
    keys = pygame.key.get_pressed()
    
    # Déplacer l'image en fonction des touches pressées
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed
    if keys[pygame.K_ESCAPE]:
        running = False

    # Vérifier si l'image touche les bords de l'écran
    if image_rect.left < 0:
        if background == fond12:
            background = fond11
            image_rect.right = width
        elif background == fond13:
            background = fond12
            image_rect.right = width
        elif background == fond14:
            background = fond13
            image_rect.right = width
        elif background == fond22:
            background = fond21
            image_rect.right = width
        elif background == fond23:
            background = fond22
            image_rect.right = width
        elif background == fond24:
            background = fond23
            image_rect.right = width
        elif background == fond32:
            background = fond31
            image_rect.right = width
        elif background == fond33:
            background = fond32
            image_rect.right = width
        elif background == fond34:
            background = fond33
            image_rect.right = width
        else:
            image_rect.left = 0
        
    if image_rect.right > width:
        if background == fond11:
            background = fond12
            image_rect.left = 0
        elif background == fond12:
            background = fond13
            image_rect.left = 0
        elif background == fond13:
            background = fond14
            image_rect.left = 0
        elif background == fond21:
            background = fond22
            image_rect.left = 0
        elif background == fond22:
            background = fond23
            image_rect.left = 0
        elif background == fond23:
            background = fond24
            image_rect.left = 0
        elif background == fond31:
            background = fond32
            image_rect.left = 0
        elif background == fond32:
            background = fond33
            image_rect.left = 0
        elif background == fond33:
            background = fond34
            image_rect.left = 0
        else:
            image_rect.right = width

    #Touche le haut
    if image_rect.top < 0:
        if background == fond21:
            background = fond11
            image_rect.bottom = height
        elif background == fond22:
            background = fond12
            image_rect.bottom = height
        elif background == fond23:
            background = fond13
            image_rect.bottom = height
        elif background == fond24:
            background = fond14
            image_rect.bottom = height
        elif background == fond31:
            background = fond21
            image_rect.bottom = height
        elif background == fond32:
            background = fond22
            image_rect.bottom = height
        elif background == fond33:
            background = fond23
            image_rect.bottom = height
        elif background == fond34:
            background = fond24
            image_rect.bottom = height
        else:
            image_rect.top = 0

    if image_rect.bottom > height:
        if background == fond11:
            background = fond21
            image_rect.top = 0
        elif background == fond12:
            background = fond22
            image_rect.top = 0
        elif background == fond13:
            background = fond23
            image_rect.top = 0
        elif background == fond14:
            background = fond24
            image_rect.top = 0
        elif background == fond21:
            background = fond31
            image_rect.top = 0
        elif background == fond22:
            background = fond32
            image_rect.top = 0
        elif background == fond23:
            background = fond33
            image_rect.top = 0
        elif background == fond24:
            background = fond34
            image_rect.top = 0
        else:
            image_rect.bottom = height

    # Remplir l'écran avec le background
    screen.blit(background, (0, 0))
    
    # Dessiner l'image à sa nouvelle position
    screen.blit(image, image_rect)

    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter le nombre de frames par seconde
    pygame.time.Clock().tick(60)

# Quitter Pygame
pygame.quit()
