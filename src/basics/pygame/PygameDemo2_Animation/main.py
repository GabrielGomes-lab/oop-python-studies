"""
Exemplo 2: Criando uma animação simples usando Pygame

Este exemplo demonstra como criar uma animação básica movendo
um objeto na tela.
"""
import pygame
from pygame.locals import *
import sys

# Definindo constantes
preto = (0, 0, 0)
vermelho = (255, 0, 0)
window_width = 640
window_height = 480
frames_por_segundo = 30

# Inicializando o pygame
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Demo 2: Animação Simples')
relogio = pygame.time.Clock()

# Variáveis de animação
circulo_raio = 30
x = -circulo_raio
y = 240
velocidade = 5

# Loop principal
while True:
    # Tratando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Atualizar posição (animação)
    x += velocidade
    if x > window_width + circulo_raio:
        x = -circulo_raio
    
    # Limpar a tela
    window.fill(preto)
    
    # Desenhar objeto animado (um círculo vermelho)
    pygame.draw.circle(window, vermelho, (x, y), circulo_raio)
    
    # Atualizar a tela
    pygame.display.update()
    
    # Controlar FPS
    relogio.tick(frames_por_segundo)
