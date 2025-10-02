import pygame
from pygame.locals import *
from sys import exit
import constantes
import os
from random import choice
import funcoes_base
import time
from game_over import tela_game_over
from vitoria import tela_vitoria

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
pygame.display.set_caption("Fase 4")
clock = pygame.time.Clock()

# ---------------- LABIRINTO FIXO -----------------
# 1 = parede, 0 = espaço
labirinto = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1],
    [1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1],
    [1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

TILE = constantes.TILE_FASE4
paredes = []

# ---------------- JOGADOR -----------------
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walk_sprites = []
        for i in range(1, 11):
            caminho = os.path.join("imagens", "cat", f"Walk ({i}).png")
            img = pygame.image.load(caminho).convert_alpha()
            img = pygame.transform.scale(img, (13, 13))
            self.walk_sprites.append(img)

        # sprite Idle
        idle_path = os.path.join("imagens", "cat", "Idle.png")
        self.idle_sprite = pygame.image.load(idle_path).convert_alpha()
        self.idle_sprite = pygame.transform.scale(self.idle_sprite, (13, 13))

        self.atual = 0
        self.image = self.idle_sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = funcoes_base.posicao_inicial_jogador(labirinto,TILE)

        self.velocidade_animacao = 0.2
        self.contador = 0

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        funcoes_base.mover_com_colisao(self, self.vel_x, self.vel_y)

        if self.vel_x != 0 or self.vel_y != 0:
            self.contador += self.velocidade_animacao
            if self.contador >= 1:
                self.contador = 0
                self.atual = (self.atual + 1) % len(self.walk_sprites)
                self.image = self.walk_sprites[self.atual]
        else:
            self.image = self.idle_sprite

    def mover_direita(self):
        self.vel_x = 5

    def mover_esquerda(self):
        self.vel_x = -5

    def mover_baixo(self):
        self.vel_y = 5

    def mover_cima(self):
        self.vel_y = -5

    def parar_horizontal(self):
        self.vel_x = 0

    def parar_vertical(self):
        self.vel_y = 0

#CHAVE
class Chave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        caminho = os.path.join("imagens", "chave.gif")
        self.image = pygame.image.load(caminho).convert_alpha()
        self.image = pygame.transform.scale(self.image, (13, 13))
        self.rect = self.image.get_rect()
        self.rect.topleft = funcoes_base.posicao_aleatoria_livre(labirinto,TILE)
        
#PORTA
class Porta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        caminho = os.path.join("imagens", "porta.png")
        self.image_original = pygame.image.load(caminho).convert_alpha()
        self.image_original = pygame.transform.scale(self.image_original, (20, 20))
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()

        self.rect.topleft = funcoes_base.posicao_porta(labirinto,TILE)

        self.aberta = False

    def abrir(self):
        #Muda a cor da porta para indicar que está aberta
        if not self.aberta:
            self.aberta = True
            # cria uma cópia colorida da porta
            self.image = self.image_original.copy()
            # aplica um "tint" verde
            verde = (0, 130, 0)
            self.image.fill(verde, special_flags=pygame.BLEND_RGBA_MULT)

# ---------------- INIMIGOS -----------------
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.walk_sprites = []
        for i in range(1, 11):
            caminho = os.path.join("imagens", "dog", f"Walk ({i}).png")
            img = pygame.image.load(caminho).convert_alpha()
            img = pygame.transform.scale(img, (13, 13))  # menor que o jogador
            self.walk_sprites.append(img)

        self.atual = 0
        self.image = self.walk_sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocidade = 2
        self.direcao = choice(["direita", "esquerda", "cima", "baixo"])

        self.contador = 0
        self.velocidade_animacao = 0.2

    def mudar_direcao(self):
        self.direcao = choice(["direita", "esquerda", "cima", "baixo"])

    def update(self):
        dx, dy = 0, 0
        if self.direcao == "direita": dx = self.velocidade
        elif self.direcao == "esquerda": dx = -self.velocidade
        elif self.direcao == "cima": dy = -self.velocidade
        elif self.direcao == "baixo": dy = self.velocidade

        antes = self.rect.copy()
        funcoes_base.mover_com_colisao(self, dx, dy)
        if self.rect == antes:
            self.mudar_direcao()

        self.contador += self.velocidade_animacao
        if self.contador >= 1:
            self.contador = 0
            self.atual = (self.atual + 1) % len(self.walk_sprites)
            self.image = self.walk_sprites[self.atual]

# ---------------- LOOP -----------------
def jogar_fase4(tela, relogio):
    funcoes_base.criar_labirinto(labirinto,TILE)

    diretorio_audios = os.path.join(os.getcwd(), 'audios')
    pygame.mixer.music.load(os.path.join(diretorio_audios, constantes.MUSICA_FASE4))
    pygame.mixer.music.set_volume(0.05)  # música mais baixa
    pygame.mixer.music.play(-1, start=(3.0))

    todas_as_sprites = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()

    jogador = Jogador()
    chave = Chave()
    porta = Porta()

    # cria 3 inimigos em posições diferentes
    inimigo1 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo2 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo3 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo4 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo5 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo6 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo7 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo8 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo9 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo13 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo11 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo12 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo13 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))
    inimigo14 = Inimigo(*funcoes_base.posicao_aleatoria_livre(labirinto,TILE))

    inimigos.add(inimigo1, inimigo2, inimigo3, inimigo4, inimigo5, inimigo6,inimigo7,inimigo8,inimigo9,inimigo13,inimigo11,inimigo12,inimigo13,inimigo14)
    todas_as_sprites.add(jogador, chave, porta, inimigo1, inimigo2, inimigo3, inimigo4, inimigo5, inimigo6,inimigo7,inimigo8,inimigo9,inimigo13,inimigo11,inimigo12,inimigo13,inimigo14)

    chave_coletada = False
    vidas = 6
    jogando = True

    invencivel_ate = 0

    while jogando:
        relogio.tick(constantes.FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                jogando = False
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key in [K_RIGHT, K_d]:
                    jogador.mover_direita()
                if event.key in [K_LEFT, K_a]:
                    jogador.mover_esquerda()
                if event.key in [K_UP, K_w]:
                    jogador.mover_cima()
                if event.key in [K_DOWN, K_s]:
                    jogador.mover_baixo()

            if event.type == KEYUP:
                if event.key in [K_RIGHT, K_LEFT, K_d, K_a]:
                    jogador.parar_horizontal()
                if event.key in [K_UP, K_DOWN, K_w, K_s]:
                    jogador.parar_vertical()

        todas_as_sprites.update()

        # colisão jogador x chave
        if not chave_coletada and jogador.rect.colliderect(chave.rect):
            som_chave = pygame.mixer.Sound(os.path.join(diretorio_audios, "chave.mp3"))
            som_chave.set_volume(0.7)
            som_chave.play()
            chave.kill()
            chave_coletada = True
            porta.abrir()

        # colisão jogador x porta
        if chave_coletada and jogador.rect.colliderect(porta.rect):
            pygame.mixer_music.stop()
            som_porta = pygame.mixer.Sound(os.path.join(diretorio_audios, "porta_abrindo.mp3"))
            som_porta.set_volume(0.7)
            som_porta.play()
            pygame.mixer.music.stop()
            resultado = tela_vitoria(tela, relogio)

            if resultado == "restart":
                return

        # colisão jogador x inimigos
        if pygame.sprite.spritecollideany(jogador, inimigos):
            agora = time.time()
            if agora > invencivel_ate:   # só perde vida se já não estiver invencível
                vidas -= 1
                if vidas > 0:
                    jogador.rect.topleft = funcoes_base.posicao_inicial_jogador(labirinto,TILE)
                    invencivel_ate = agora + 2  # 2 segundos de invencibilidade
                else:
                    funcoes_base.animar_morte(jogador, tela, relogio)
                    pygame.mixer.music.stop()
                    resultado = tela_game_over(tela, relogio)
                    if resultado == "restart":
                        return

        # --- DESENHO ---
        tela.fill(constantes.PRETO)
        funcoes_base.desenhar_labirinto(tela)
        todas_as_sprites.draw(tela)
        funcoes_base.desenhar_vidas(tela, vidas)

        pygame.display.flip()