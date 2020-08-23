import pygame
import random
import math
from pygame import mixer # for music

#initialize the pygame
pygame.init()

#create the Screen
screen = pygame.display.set_mode((800,600))

#background-----
background = pygame.image.load("bg.jpg").convert_alpha()
bg = pygame.transform.scale(background,(800,600))
# background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#Title and icon
pygame.display.set_caption("Space War by Shakir Azim")
icon = pygame.image.load("player.png")
pygame.display.set_icon(icon)

#----------player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#----------enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 8
for i in range(num_of_enemies):

    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.5)
    enemyY_change.append(50)

#----------bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready" # ready--> We can't see the bullet on screen ! Fire --> Bullet is currently moving.
# score---
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# game over text---
over_font = pygame.font.Font('freesansbold.ttf',70)



def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True,(255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))

#Collision--- finding distance btwn enemy and bullet--
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#----------game loop----------#
running = True
while running:
    # RGB Red, Green, Blue (background)
    screen.fill((0,0,0))  #it should be at top// order matters a lot.
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # boundaries for player
    playerX +=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    # enemy movement and boundaries.
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] +=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]= 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]= -0.5
            enemyY[i] += enemyY_change[i]

        # collision-------
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()       
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i) # Order matters a lot.

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    player(playerX,playerY)
    
    show_score(textX,textY)

    pygame.display.update() # we need to update to see the changes occurring...