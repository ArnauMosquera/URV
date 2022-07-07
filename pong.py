#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from random import randint

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 30

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Joc del pong")

fons = pygame.image.load("fonsPong.jpg").convert()
paletauser = pygame.image.load("paleta.png").convert_alpha()
paletabot = pygame.image.load("paleta.png").convert_alpha()
bola = pygame.image.load("bola.png").convert_alpha()
bolax = 309
bolay = 220
bolavx = 0
bolavy = 0 
boladir = 0
paletauserx = 10
paletausery = 190
paletabotx = 615
paletaboty = paletausery
direccio = 'QUIET'

rellotge=pygame.time.Clock()

screen.blit(fons,(0,0))
screen.blit(bola,(bolax,bolay))
screen.blit(paletauser,(paletauserx,paletausery))
screen.blit(paletabot,(paletabotx,paletaboty))

pygame.display.flip()

final = False
pygame.mouse.set_visible(True)

while not final:
	screen.blit(fons,(0,0))
	screen.blit(bola,(bolax,bolay))
	screen.blit(paletauser,(paletauserx,paletausery))
	screen.blit(paletabot,(paletabotx,paletaboty))
	
	#bola
	if boladir == 0: #dreta
		bolax += 2
		bolay += bolavy
		if bolax==paletabotx or bolax >= 0:
			bolavy = (randint(0,10))*1
			boladir = 1

	if boladir == 1: #esquerra
		bolax -= 2
		bolay -= bolavy
		if bolax==paletauserx-20 or bolax<=0:
			boladir = 0
			bolavy = (randint(0,10))*-1
	if bolay<=0 or bolay>=SCREEN_HEIGHT-20:
		bolavy = (randint(0,10))*-1
		
	
	#paletauser
	if direccio == 'AMUNT':
		paletausery -= 5
		if paletausery == 5:
			direccio = 'QUIET'
	if direccio == 'ABAIX':
		paletausery += 5
		if paletausery == SCREEN_HEIGHT-75:
			direccio = 'QUIET'
	if direccio == 'QUIET':
		paletausery = paletausery 
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			final = True
		if event.type == pygame.KEYDOWN:
			if event.key == K_UP or event.key == ord('w'):
				direccio = 'AMUNT'
			if event.key == K_DOWN or event.key == ord('s'):
				direccio = 'ABAIX'
		if event.type == pygame.KEYUP:
			if event.key == K_UP or event.key == ord('w'):
				direccio = 'QUIET'
			if event.key == K_DOWN or event.key == ord('s'):
				direccio = 'QUIET'
	
	#paletabot
	paletaboty=bolay+37.5
	
	
	pygame.display.flip()   
	rellotge.tick(FPS)

pygame.quit()
sys.exit(0)
