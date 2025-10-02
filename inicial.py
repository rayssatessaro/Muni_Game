import pygame 
import constantes
import os
from PIL import Image

def carregar_gif_pygame(arquivo):
    img = Image.open(arquivo)
    frames = []
    try:
        while True:
            frame = img.copy().convert("RGBA")
            pygame_image = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
            frames.append(pygame_image)
            img.seek(img.tell() + 1)  # vai para o próximo frame
    except EOFError:
        pass
    return frames


class Game:
    def __init__(self):
        #criando a tela
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA,constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False
            
    def atualizar_sprites(self):
        #atualiza os sprites
        self.todas_as_sprites.update()
    
    def desenhar_sprites(self):
        #desenha os sprites
        self.tela.fill(constantes.PRETO) #limpando a tela
        self.todas_as_sprites.draw(self.tela) #desenhando as sprites
        pygame.display.flip()
    
    def carregar_arquivos(self):
        #vai carregar audios e imagens
        diretorio_imagens = os.path.join(os.getcwd(),'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(),'audios')
        self.spritesheet = os.path.join(diretorio_imagens, constantes.SPRITEPRINCIPAL)
        self.start_logo = os.path.join(diretorio_imagens,constantes.START)
        
        # agora carrega o GIF animado
        self.start_logo_frames = carregar_gif_pygame(self.start_logo)

    def mostrar_texto(self, texto, tam, cor, x, y):
        #mostra o texto na tela
        fonte = pygame.font.Font(self.fonte,tam)
        texto = fonte.render(texto, False, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x,y)
        self.tela.blit(texto, texto_rect)

    def mostrar_logo_animado(self, x, y):
        # escolhe o frame baseado no tempo
        frame_atual = (pygame.time.get_ticks() // 100) % len(self.start_logo_frames)
        logo = self.start_logo_frames[frame_atual]
        logo_rect = logo.get_rect()
        logo_rect.midtop = (x, y)
        self.tela.blit(logo, logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constantes.MUSICA_START))
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play()  # toca em loop
        self.esperar_jogador()

    def esperar_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS)

            # eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                pygame.mixer.music.stop()
                efeito = pygame.mixer.Sound(os.path.join(self.diretorio_audios, constantes.FASE))
                efeito.set_volume(0.2)
                efeito.play()

            # redesenha a tela a cada frame
            self.tela.fill(constantes.PRETO)
            self.mostrar_logo_animado(constantes.LARGURA/2, 20)
            self.mostrar_texto('-Pressione uma tecla para jogar', 32, constantes.PINK, constantes.LARGURA/2,320)
            self.mostrar_texto('-Desenvolvido por Rayssa Tessaro', 15, constantes.PINK, constantes.LARGURA/2,570)
            
            pygame.display.flip()
    
g = Game()
g.mostrar_tela_start()

import fase1

while g.esta_rodando:
    g.mostrar_tela_start()

    resultado = fase1.jogar_fase1(g.tela, g.relogio)

    if resultado == "restart":
        continue

