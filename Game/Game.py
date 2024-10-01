import pygame

# Initialiser Pygame
pygame.init()

fullscreen = input("Full screen ? ")

# Créer une fenêtre en plein écran
if fullscreen == "Yes":
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((1207, 858))

# Charger l'image
image = pygame.image.load('sans_no_background.png')
image_rect = image.get_rect()

# Charger le background
fond11 = pygame.image.load('undertale11.jpg')
fond11 = fond11.convert()

fond12 = pygame.image.load('undertale12.jpg')
fond12 = fond12.convert()

fond13 = pygame.image.load('undertale13.jpg')
fond13 = fond13.convert()

fond14 = pygame.image.load('undertale14.jpg')
fond14 = fond14.convert()

fond21 = pygame.image.load('undertale21.jpg')
fond21 = fond21.convert()

fond22 = pygame.image.load('undertale22.jpg')
fond22 = fond22.convert()

fond23 = pygame.image.load('undertale23.jpg')
fond23 = fond23.convert()

fond24 = pygame.image.load('undertale24.jpg')
fond24 = fond24.convert()

fond31 = pygame.image.load('undertale31.jpg')
fond31 = fond31.convert()

fond32 = pygame.image.load('undertale32.jpg')
fond32 = fond32.convert()

fond33 = pygame.image.load('undertale33.jpg')
fond33 = fond33.convert()

fond34 = pygame.image.load('undertale34.jpg')
fond34 = fond34.convert()

# Obtenir les dimensions de l'écran
width, height = screen.get_size()

# Position initiale de l'image
image_rect.center = (width // 2, height // 2)

# Définir la vitesse de déplacement
speed = 5

background = fond11

# Remplir l'écran avec le background
screen.blit(background, (0, 0))

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
        running = False  # Utiliser False avec une majuscule

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
            image_rect.right = 0
        
    if image_rect.right > width:
        if background == fond11:
            background = fond12
            image_rect.right = 0
        elif background == fond12:
            background = fond13
            image_rect.right = 0
        elif background == fond13:
            background = fond14
            image_rect.right = 0
        elif background == fond21:
            background = fond22
            image_rect.right = 0
        elif background == fond22:
            background = fond23
            image_rect.right = 0
        elif background == fond23:
            background = fond24
            image_rect.right = 0
        elif background == fond31:
            background = fond32
            image_rect.right = 0
        elif background == fond32:
            background = fond33
            image_rect.right = 0
        elif background == fond33:
            background = fond34
            image_rect.right = 0
        else:
            image_rect.right = width

    if image_rect.top < 0:
        image_rect.top = 0

    if image_rect.bottom > height:
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
