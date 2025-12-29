"""
Exemplo 3: Capturando entrada do usuário usando Pygame

Este exemplo demonstra como capturar eventos de teclado e mouse
para controlar objetos na tela.
"""
import pygame
from pygame.locals import *
import sys

# Definindo constantes
preto = (0, 0, 0)
azul = (0, 0, 255)
window_width = 640
window_height = 480
frames_por_segundo = 30

# Inicializando o pygame
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Demo 3: Entrada do Usuário')
relogio = pygame.time.Clock()

# Variáveis do objeto controlável
x = 320
y = 240
velocidade = 5

# Loop principal
while True:
    # Tratando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        x -= velocidade
    if keys[K_RIGHT] or keys[K_d]:
        x += velocidade
    if keys[K_UP] or keys[K_w]:
        y -= velocidade
    if keys[K_DOWN] or keys[K_s]:
        y += velocidade
    
    # Manter o objeto dentro da tela
    x = max(30, min(x, window_width - 30))
    y = max(30, min(y, window_height - 30))
    
    # Limpar a tela
    window.fill(preto)
    
    # Desenhar objeto controlável (um círculo azul)
    pygame.draw.circle(window, azul, (x, y), 30)
    
    # Atualizar a tela
    pygame.display.update()
    
    # Controlar FPS
    relogio.tick(frames_por_segundo)
