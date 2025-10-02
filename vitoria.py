import pygame
import os
import time
from sys import exit
from PIL import Image
from constantes import VITORIA

diretorio_audios = os.path.join(os.getcwd(),'audios')

def tela_vitoria(tela, relogio):
    caminho = os.path.join("imagens", "vitoria.gif")
    gif = Image.open(caminho)

    frames = []
    durations = []
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_img = gif.convert("RGBA")
        durations.append(gif.info.get("duration", 100))  
        mode = frame_img.mode
        size = frame_img.size
        data = frame_img.tobytes()
        py_image = pygame.image.fromstring(data, size, mode)
        frames.append(py_image)

    # 🔊 toca a música apenas 1 vez
    pygame.mixer.music.load(os.path.join(diretorio_audios, VITORIA))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(start=1.0)

    inicio = time.time()
    i = 0
    while time.time() - inicio < 10:  # tela dura 15s
        if time.time() - inicio >= 10:
            pygame.mixer.music.stop()

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

        delay = durations[i % len(durations)] / 1000.0
        relogio.tick(30)
        time.sleep(delay)

        i += 1

    pygame.mixer.music.stop()
    return "restart"

        

    
