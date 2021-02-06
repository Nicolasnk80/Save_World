import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
	os.chdir(sys._MEIPASS)
####


import pygame
import sys
import random
from pygame.locals import *
from player import Nave
from asteroid import Asteroid
from shot import Shot

try:
    pygame.init()
except:
    print('erro ao iniciar o pygame')

decisao = 'inicio'
pontos = 0

def texto(tamanho,texto,posx,posy,tela):
    fonte = pygame.font.get_default_font()
    texto_font = pygame.font.SysFont(fonte, tamanho)
    text = texto_font.render(texto, True, (255,255,255))
    tela.blit(text, (posx,posy))

def fim(pontos):
    tela = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Save World - AppGame Tecnologia')

    fundo = pygame.image.load('data/fundo.png')
    fundo = pygame.transform.scale(fundo, (800,600))

    pygame.mixer.music.load('data/music.mp3')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    click = False
    game = True
    while game:
        posx,posy = pygame.mouse.get_pos()

        botao1 = pygame.Rect(300,350,200,80)
        botao2 = pygame.Rect(300,450,200,80)

        if botao1.collidepoint(posx,posy):
            if click == True:
                global decisao
                decisao = 'meio'
                game = False
        if botao2.collidepoint(posx,posy):
            if click == True:
                pygame.quit()
                sys.exit()
        
        pygame.draw.rect(tela,(255,0,0),botao1)
        pygame.draw.rect(tela,(255,0,0),botao2)

        texto(30, 'GAME', 365, 378, tela)
        texto(30, 'SAIR', 368, 478, tela)
        texto(70, 'quantidade de pontos: '+str(pontos), 150, 150, tela)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        tela.blit(fundo, (0,0))
        pygame.draw.rect(tela,(255,0,0),botao1)
        pygame.draw.rect(tela,(255,0,0),botao2)

        texto(30, 'GAME', 365, 378, tela)
        texto(30, 'SAIR', 368, 478, tela)
        texto(70, 'quantidade de pontos: '+str(pontos), 150, 150, tela)

        pygame.display.update()
def inicio():
    tela = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Save World - AppGame Tecnologia')

    fundo = pygame.image.load('data/fundo.png')
    fundo = pygame.transform.scale(fundo, (800,600))

    pygame.mixer.music.load('data/music.mp3')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    click = False
    game = True
    while game:
        posx,posy = pygame.mouse.get_pos()

        botao1 = pygame.Rect(300,350,200,80)
        botao2 = pygame.Rect(300,450,200,80)

        if botao1.collidepoint(posx,posy):
            if click == True:
                global decisao
                decisao = 'meio'
                game = False
        if botao2.collidepoint(posx,posy):
            if click == True:
                pygame.quit()
                sys.exit()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        tela.blit(fundo, (0,0))
        pygame.draw.rect(tela,(255,0,0),botao1)
        pygame.draw.rect(tela,(255,0,0),botao2)

        texto(30, 'GAME', 365, 378, tela)
        texto(30, 'SAIR', 368, 478, tela)
        texto(80, 'Save World!', 240, 100, tela)
        texto(55, 'AppGame - Tecnologia', 200, 200, tela)

        pygame.display.update()
def game():
    global pontos
    run = True
    timer = 20
    clock = pygame.time.Clock()
    largura = 800
    altura = 600
    screen = (largura,altura)

    tela = pygame.display.set_mode(screen)
    pygame.display.set_caption('Save World - AppGame Tecnologia')

    fundo = pygame.image.load('data/fundo.png')
    fundo = pygame.transform.scale(fundo, (screen))

    grupoA = pygame.sprite.Group()
    grupoB = pygame.sprite.Group()
    grupoC = pygame.sprite.Group()
    player = Nave(grupoA)
    asteroid = Asteroid(grupoB)

    fonte = pygame.font.get_default_font()
    fonte_pontos = pygame.font.SysFont(fonte, 30)
    pontos = 0
    text = fonte_pontos.render('pontos: '+str(pontos),True,(255,255,255),(0,0,0))
    
    bum = pygame.mixer.Sound('data/explosion.wav')

    pygame.mixer.music.load('data/music.mp3')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    newShot = Shot(grupoA,grupoC)
                    newShot.rect.center = player.rect.center

        tela.blit(fundo, (0,0))
        tela.blit(text, (700, 20))

        timer += 1

        if timer > 30:
            if random.random() < 0.5:
                newAsteroid = Asteroid(grupoB)
                timer = 0

        colisao = pygame.sprite.spritecollide(player,grupoB,False,pygame.sprite.collide_mask)
        hint = pygame.sprite.groupcollide(grupoB,grupoC,True,True,pygame.sprite.collide_mask)

        if hint:
            pontos += 1
            text = fonte_pontos.render('pontos: '+str(pontos),True,(255,255,255),(0,0,0))

        if colisao:
            global decisao
            pygame.mixer.music.stop()
            bum.play()
            player.image = pygame.image.load('data/explosao.png')
            decisao = 'fim'
            run = False

        grupoB.draw(tela)
        grupoA.draw(tela)
        grupoA.update()
        grupoB.update()
        pygame.display.update()

while True:
    if decisao == 'inicio':
        inicio()
    elif decisao == 'meio':
        game()
    elif decisao == 'fim':
        fim(pontos)
