import pygame
from pygame.locals import *
import constantes
import os
from random import choice

def criar_labirinto(labirinto,TILE):
    global paredes
    paredes = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 1:
                rect = pygame.Rect(j*TILE, i*TILE, TILE, TILE)
                paredes.append(rect)

def desenhar_labirinto(tela):
    for parede in paredes:
        pygame.draw.rect(tela, constantes.PINK, parede,1)

def mover_com_colisao(sprite, dx, dy):
    sprite.rect.x += dx
    for parede in paredes:
        if sprite.rect.colliderect(parede):
            if dx > 0: sprite.rect.right = parede.left
            if dx < 0: sprite.rect.left = parede.right

    sprite.rect.y += dy
    for parede in paredes:
        if sprite.rect.colliderect(parede):
            if dy > 0: sprite.rect.bottom = parede.top
            if dy < 0: sprite.rect.top = parede.bottom

def posicao_aleatoria_livre(labirinto,TILE):
    livres = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 0:  # só espaços
                livres.append((j*TILE, i*TILE))
    return choice(livres) if livres else (0,0)

def posicao_inicial_jogador(labirinto,TILE):
    for i in range(len(labirinto)):           # percorre linhas
        for j in range(len(labirinto[i])):   # percorre colunas
            if labirinto[i][j] == 0:         # achou espaço livre
                return (j*TILE, i*TILE)      # coordenada em pixels
    return (0,0)  # fallback (não deve acontecer)

def posicao_porta(labirinto,TILE):
    for i in range(len(labirinto)-1,-1,-1):           # percorre linhas
        for j in range(len(labirinto[i])-1,-1,-1):   # percorre colunas
            if labirinto[i][j] == 0:         # achou espaço livre
                return (j*TILE, i*TILE)      # coordenada em pixels
    return (0,0)  # fallback (não deve acontecer)

def desenhar_vidas(tela, vidas):
    icone = pygame.image.load(os.path.join("imagens", "icon.png")).convert_alpha()
    icone = pygame.transform.scale(icone, (15, 15))
    for i in range(vidas):
        tela.blit(icone, (10 + i * 20, 10))  # espaçamento entre ícones

def animar_morte(jogador, tela, relogio):
    sprites_dead = []
    for i in range(1, 11):
        caminho = os.path.join("imagens", "cat", f"Dead ({i}).png")
        img = pygame.image.load(caminho).convert_alpha()
        img = pygame.transform.scale(img, (40, 40))
        sprites_dead.append(img)

    for frame in sprites_dead:
        tela.fill(constantes.PRETO)
        desenhar_labirinto(tela)
        tela.blit(frame, jogador.rect)
        pygame.display.flip()
        relogio.tick(8)  # velocidade da animação

