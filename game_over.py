import pygame
import os
import time
from sys import exit
from PIL import Image
from constantes import DERROTA

diretorio_audios = os.path.join(os.getcwd(),'audios')

def tela_game_over(tela, relogio):
    
    caminho = os.path.join("imagens", "game_over.gif")
    gif = Image.open(caminho)

    frames = []
    durations = []  # duração de cada frame (ms)
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_img = gif.convert("RGBA")
        durations.append(gif.info.get("duration", 100))  
        mode = frame_img.mode
        size = frame_img.size
        data = frame_img.tobytes()
        py_image = pygame.image.fromstring(data, size, mode)
        frames.append(py_image)
    vit = pygame.mixer.Sound(os.path.join(diretorio_audios,DERROTA))
    vit.set_volume(0.3)
    vit.play()
    
    # Tempo total de exibição
    inicio = time.time()
    i = 0 
    
    while time.time() - inicio < 6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # pega frame atual
        frame = frames[i % len(frames)]
        tela.fill((0, 0, 0))
        rect = frame.get_rect(center=(tela.get_width()//2, tela.get_height()//2))
        tela.blit(frame, rect)
        pygame.display.flip()

        # espera o tempo do frame
        delay = durations[i % len(durations)] / 1000.0
        relogio.tick(30)  
        time.sleep(delay)

        i += 1

      # só mantém a tela atualizada
        pygame.display.flip()
        relogio.tick(30)
 
    return "restart"


    
