import pygame
import random
import math

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
score = 0

# Enemy
enemyImg = pygame.image.load('assets/images/enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(0, 100)
enemyX_change = 2.2
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('assets/images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) +
                         math.pow(enemyY-bulletY, 2))
    if distance <= 25:
        return True
    else:
        return False


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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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

# Bullet Movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

# Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletX = 480
        bullet_state = "ready"
        score += 10
        enemyX = random.randint(0, 735)
        enemyY = random.randint(0, 100)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
