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
target_x = 400
target_y = 320
target_width_height = 120
n_pixels_move = 3

# Inicializando o pygame
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
relogio = pygame.time.Clock()

# Carregando a imagem da bola
ballImage = pygame.image.load('C:\\Users\\gblgo\\Downloads\\ball.png')
targetImage = pygame.image.load('C:\\Users\\gblgo\\Downloads\\target.jpg')
# Inicialização variváveis
ballX = random.randrange(max_width)
ballY = random.randrange(max_height)
targetRect = pygame.Rect(target_x, target_y, target_width_height, target_width_height)
# Loop principal
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - n_pixels_move
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + n_pixels_move
            elif event.key == pygame.K_UP:
                ballY = ballY - n_pixels_move
            elif event.key == pygame.K_DOWN:
                ballY = ballY + n_pixels_move

    # 8- Do any per frame 
    keypressedtuple = pygame.key.get_pressed()
    if keypressedtuple[pygame.K_LEFT]:
        ballX = ballX - n_pixels_move
    if keypressedtuple[pygame.K_RIGHT]:
        ballX = ballX + n_pixels_move
    if keypressedtuple[pygame.K_UP]:
        ballY = ballY - n_pixels_move
    if keypressedtuple[pygame.K_DOWN]:
        ballY = ballY + n_pixels_move
        
    ballRect = pygame.Rect(ballX, ballY, ball_widt_height, ball_widt_height)
    if ballRect.colliderect(targetRect):
        print('A bola atingiu o alvo!')

    # Limpar a tela
    window.fill(preto)

        # Desenhar a bola na nova posição
    window.blit(ballImage, (ballX, ballY))
    window.blit(targetImage, (target_x, target_y))
        # Atualizar a tela
    pygame.display.update()

        # Controlar FPS
    relogio.tick(frames_por_segundo)