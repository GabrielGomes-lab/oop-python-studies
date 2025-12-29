import pygame
from pygame.locals import *
from src.basics.capi6.Ball import Ball
import sys
import random

# Definir as contantes da janela
preto = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_POR_SEGUNDO = 30

# INICIALIZA O MUNDO
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
relogio = pygame.time.Clock()

# 4 - Carrega imagens se necessário


# 5 - Inicializa Variáveis
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6- Loop Principal do Jogo
while True:
    # 6.1 - Trata Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 6.2 - Atualiza o estado do jogo
    oBall.update()

    # 6.3 - Desenha o novo frame
    window.fill(preto)  # Preenche a janela com a cor preta
    oBall.draw()       # Desenha a bola na janela
    pygame.display.update()  # Atualiza a tela

    relogio.tick(FRAMES_POR_SEGUNDO) # Controla os frames por segundo
    break 
""" Note que o código principal do jogo está bastante limpo se comparado com os anteriores.
Usamos o import para trazer a classe Ball que criamos em outro arquivo.
"""
""" Criando vários objetos Ball
Esse é um dos poderes da programação orientada a objetos: para criarmos três bolas
precsamos apenas instanciar três objetos da classe Ball.
"""
import pygame
from pygame.locals import *
from src.basics.capi6.Ball import Ball
import sys
import random

# Definir as contantes da janela
preto = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_POR_SEGUNDO = 30

# INICIALIZA O MUNDO
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
relogio = pygame.time.Clock()

# 4 - Carrega imagens se necessário


# 5 - Inicializa Variáveis
n_bolas = 3
ballList = []
for oBall in range(0, n_bolas):
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)
# 6- Loop Principal do Jogo
while True:
    # 6.1 - Trata Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 6.2 - Atualiza o estado do jogo
    for oBall in ballList:
        oBall.update()

    # 6.3 - Desenha o novo frame
    window.fill(preto)  # Preenche a janela com a cor preta
    for oBall in ballList:
        oBall.draw()       # Desenha a bola na janela
    pygame.display.update()  # Atualiza a tela

    relogio.tick(FRAMES_POR_SEGUNDO) # Controla os frames por segundo
    break 