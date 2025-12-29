import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define as constantes da janela
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

# 2 - Inicializa o mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
""" Um exemplo simples de uso do SimpleButton """
oButton = SimpleButton(window, (50, 50), 
                       "button_up.png", 
                       "button_down.png")


# 6 - Loop Principal do Jogo
while True:
    # 6.1 - Trata Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if oButton.handleEvent(event):
            print("Botão clicado!")

    # 6.2 - Atualiza o estado do jogo


    # 6.3 - Desenha o novo frame
    window.fill(GRAY)  # Preenche a janela com a cor cinza
    oButton.draw()    # Desenha o botão na janela
    pygame.display.update()  # Atualiza a tela

    clock.tick(FRAMES_PER_SECOND) # Controla os frames por segundo