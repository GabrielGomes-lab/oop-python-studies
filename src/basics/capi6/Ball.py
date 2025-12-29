""" Construindo o screensaver ball com OOP em Pygame 
Vamos começar criando a classe Ball que representará a bola do screensaver. Esta classe deve encapsular todas as propriedades e comportamentos da bola, como sua posição, velocidade, cor e métodos para atualizar sua posição e desenhá-la na tela.
"""

import pygame
from pygame.locals import *
import random



class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window #@ janela onde a bola será desenhada
        self.windowWidth = windowWidth #@ largura da janela
        self.windowHeight = windowHeight #@ altura da janela
        self.image = pygame.image.load("src/basics/capi6/images/ball.png")
        ballRect = self.image.get_rect() #@ obtém o retângulo da imagem da bola
        self.width = ballRect.width #@ largura da bola
        self.height = ballRect.height #@ altura da bola
        self.maxWidth = windowWidth - self.width #@ largura máxima que a bola pode alcançar
        self.maxHeight = windowHeight - self.height #@ altura máxima que a bola pode alcançar

        # Pega uma posição aleatória

        self.x = random.randrange(0, self.maxWidth) #@ posição x inicial aleatória
        self.y = random.randrange(0, self.maxHeight) #@ posição y inicial ale


        # Escolhe uma velocidade entre -4 e 4, exceto 0
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList) #@ velocidade x inicial aleatória
        self.ySpeed = random.choice(speedsList) #@ velocidade y inicial aleatória

        def update(self):
            """ Atualiza a posição da bola e verifica colisões com as bordas da janela """
            if (self.x < 0) or (self.x >= self.maxWidth):
                self.xSpeed = -self.xSpeed # Inverte a velocidade x se colidir com as
            if (self.y < 0) or (self.y >= self.maxHeight):
                self.ySpeed = -self.ySpeed # Inverte a velocidade y se colidir com as bordas

            # Atualiza a bola x e x usando a velocidade em duas direções
            self.x = self.x + self.xSpeed
            self.y = self.y + self.ySpeed
   
    def draw(self):
        self.window.blit(self.image, (self.x, self.y)) # Desenha a bola na janela na posição (x, y)
            
""" Quando instanciamos o objeto Ball, o metodo init recebe três dados, a janela onde será desenhado, a largura e a altura da janela.
A bola é carregada a partir de uma imagem e suas dimensões são obtidas. A posição inicial da bola é definida aleatoriamente dentro dos limites da janela, e a velocidade inicial em ambas as direções também é escolhida aleatoriamente a partir de uma lista de valores possíveis, essa velocidade
representa o número de pixels que a bola se moverá em cada atualização"""