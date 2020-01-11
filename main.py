import pygame
import random

# Initialize the pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('assets/images/background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/images/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('assets/images/enemy.png')
enemyX = random.randint(0, 740)
enemyY = random.randint(0, 100)
enemyX_change = 2.2
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

# Player Movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

# Enemy Movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2.2
        enemyY += enemyY_change
    elif enemyX >= 674:
        enemyX_change = -2.2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
