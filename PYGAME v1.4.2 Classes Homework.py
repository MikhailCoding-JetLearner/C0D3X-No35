
import pygame
import os
import time
import random
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.update()
bg = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/flower_field.png")
bg = pygame.transform.scale(bg, (800, 700))
bee = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/lil_bee.png")
bee = pygame.transform.scale(bee, (64, 64))
flower = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/flower.png")
flower = pygame.transform.scale(flower, (20, 20))
beeX = 200
beeY = 200
flowerX = random.randint(1, 800)
flowerY = random.randint(1, 700)
flowerRect = pygame.Rect(flowerX, flowerY, 20, 20)


def keys():
    global beeX, beeY
    beeRect = pygame.Rect(beeX, beeY, 64, 64)
    everykeyz = pygame.key.get_pressed()
    if everykeyz[pygame.K_a]:
        beeX += -2
    if everykeyz[pygame.K_d]:
        beeX -= -2
    if everykeyz[pygame.K_w]:
        beeY += -2
    if everykeyz[pygame.K_s]:
        beeY -= -2
    if beeRect.colliderect(flowerRect):
        flowerr()

def flowerr():
    global flowerX, flowerY, flowerRect
    flowerX = random.randint(1, 800)
    flowerY = random.randint(1, 700)
    flowerRect = pygame.Rect(flowerX, flowerY, 50, 50)

while 1 == 1:
    pygame.display.update()
    screen.blit(bg, (0, 0))
    keys()
    screen.blit(bee, (beeX, beeY))
    
    screen.blit(flower, (flowerX, flowerY))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
