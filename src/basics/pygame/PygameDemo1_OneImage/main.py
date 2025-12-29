"""
Exemplo 1: Exibindo uma imagem simples usando Pygame

Este exemplo demonstra como carregar e exibir uma imagem estática
em uma janela do Pygame.
"""
import pygame
from pygame.locals import *
import sys

# Definindo constantes
preto = (0, 0, 0)
window_width = 640
window_height = 480
frames_por_segundo = 30

# Inicializando o pygame
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Demo 1: Exibindo uma Imagem')
relogio = pygame.time.Clock()

# Loop principal
while True:
    # Tratando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Limpar a tela
    window.fill(preto)
    
    # Aqui você pode adicionar código para desenhar uma imagem
    # Por exemplo: window.blit(imagem, (x, y))
    
    # Atualizar a tela
    pygame.display.update()
    
    # Controlar FPS
    relogio.tick(frames_por_segundo)
