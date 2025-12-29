# pygame demo 2 - one image, click and move

import pygame
from pygame.locals import *
import sys
import random

# Definindo constantes
preto = (0, 0, 0)
window_width = 640
window_height = 480
frames_por_segundo = 30
ball_widt_height = 100  # assumindo tamanho da imagem da bola
max_width = window_width - ball_widt_height
max_height = window_height - ball_widt_height

# Inicializando o pygame
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
relogio = pygame.time.Clock()

# Carregando a imagem da bola
ballImage = pygame.image.load('C:\\Users\\gblgo\\Downloads\\ball.png')

# Inicialização variváveis
ballX = random.randrange(max_width)
ballY = random.randrange(max_height)
ballRect = pygame.Rect(ballX, ballY, ball_widt_height, ball_widt_height)

# Loop principal
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ballRect.collidepoint(event.pos):
                # Mover a bola para uma nova posição aleatória
                ballX = random.randint(0, max_width)
                ballY = random.randint(0, max_height)
                ballRect = pygame.Rect(ballX, ballY, ball_widt_height, ball_widt_height)

    # Limpar a tela
    window.fill(preto)

        # Desenhar a bola na nova posição
    window.blit(ballImage, (ballX, ballY))
        # Atualizar a tela
    pygame.display.update()

        # Controlar FPS
    relogio.tick(frames_por_segundo)