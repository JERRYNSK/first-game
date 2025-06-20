import pygame
import random
from pygame.locals import *
pygame.init()
largura_tela = 640
altura_tela = 480

tela = pygame.display.set_mode((largura_tela, altura_tela))
posx = 0
diry = 1
dirx = 1
timer = 0
posballx = largura_tela / 2
posbally = altura_tela / 2
posenemyx = 0
colorenemy= (255,0,0)
def move_bola():
    bola = pygame.draw.circle(tela, (0, 255, 0), (posballx, posbally), 20)

        
while True:
    tela.fill((0,0,0))
    posx = pygame.mouse.get_pos()[0] - 150/2
    player = pygame.draw.rect(tela, (0,0, 255), (posx, tela.get_height() - 100, 150, 50)) 
    enemy = pygame.draw.rect(tela, colorenemy, (posenemyx - 150/2, 0, 150, 50))
    if posbally > tela.get_height() or posbally < 0: 
        posbally =  tela.get_height()/2
        posballx = tela.get_width()/2
        diry *= -1
        timer = 0
    if timer < 3:
        posbally =  tela.get_height()/2
        posballx = tela.get_width()/2
        timer += 1/60
    if posballx > 0 and posballx > tela.get_width():
        dirx = -1
    if  posballx < 0 and posballx < tela.get_width():
        dirx = 1
    posbally += 11 * diry
    posballx += 11 * dirx
    if player.collidepoint(posballx, posbally):
        diry = -1
        
    if enemy.collidepoint(posballx, posbally):
        diry = 1
        
    move_bola()
    if posballx > posenemyx:
        posenemyx += 9
    elif posballx < posenemyx:
        posenemyx -= 9
    
    pygame.time.Clock().tick(60)
    pygame.display.update()