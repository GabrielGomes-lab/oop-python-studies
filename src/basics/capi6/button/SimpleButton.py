""" Construindo um botão reutilizavel com OOP"""

import pygame
from pygame.locals import *

class SimpleButton():

    state_idle = 'idle'
    state_armed = 'armed'
    state_disarmed = 'disarmed'

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # 
        self.rect = self.surfaceUp.get_rect() #@ obtém o retângulo da imagem do botão
        self.rect[0] = loc[0] #@ posição x do botão
        self.rect[1] = loc[1] #@ posição y do botão
        self.state = SimpleButton.state_idle #@ estado inicial do botão

    def handleEvent(self, eventObj):
        # Trata um evento do Pygame e atualiza o estado do botão
        # Normalmente retorna falso

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # O botão só se importa com eventos relacionados ao mouse
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.state_idle:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True  # clicado!

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False
            
    def draw(self):
        # Desenha o botão na janela dependendo do seu estado
        if self.state == SimpleButton.state_armed:
            self.window.blit(self.surfaceDown, self.loc)
        else:  # IDLE or DISARMED
            self.window.blit(self.surfaceUp, self.loc)