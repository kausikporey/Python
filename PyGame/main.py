import pygame
import random
import math
import time
from pygame import mixer

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") #set the name
icon = pygame.image.load('images/ufo.png') #load the icon
pygame.display.set_icon(icon) #set the icon

#Adding Background Image
background = pygame.image.load('images/background.png')

#player Area
playerImg = pygame.image.load('images/space-invaders.png') #load the image into the game window
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))

#Enemy Area for multiple enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 3
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(10)
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

#Background Music  
mixer.music.load('images/background.wav') 
mixer.music.play(-1) 

#Bullet Area
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 3
bullet_state = 'ready'
def fire_bullet(x,y):
       global bullet_state
       bullet_state = 'fire'
       screen.blit(bulletImg,(x+16,y+10))

#Collision between enemy and bullet
def isCollision(w,x,y,z):
    distance = math.sqrt((math.pow(w-y,2))+math.pow(x-z,2))
    if distance < 27:
        return True
    else:
        return False  

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
def Score(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


#Game Over
def gameOver():
    over = pygame.font.Font('freesansbold.ttf',64)
    game_over = over.render("Game Over!",True,(255,255,255))
    screen.blit(game_over,(220,200))


running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletsound = mixer.Sound('images/laser.wav')
                    bulletsound.play()
                    bulletX = playerX  
                    fire_bullet(bulletX,bulletY)   


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0 

                  
    playerX += playerX_change 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    # screen.fill((0,0,0)) #RGB ,change the background colour
    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    if bulletY <= 50:
        bullet_state = 'ready' 
        bulletX = 0
        bulletY = 480       



    for i in range(no_of_enemies):
        #gameover
        if enemyY[i] >= 410:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            gameOver()
            Score(320,300)
            #pygame.display.update()
            break
        enemyX[i] += enemyX_change[i] 
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY) 
        if collision:
            collisionsound = mixer.Sound('images/explosion.wav')
            collisionsound.play()
            score_value += 10 
            bullet_state = 'ready'
            bulletY = 480   
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    Score(600,15)                         
    player(playerX,playerY)
    pygame.display.update()
