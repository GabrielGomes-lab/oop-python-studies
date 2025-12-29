import pygame
from pygame.locals import *
from src.basics.capi6.text_display.textdisplay import SimpleText
from src.basics.capi6.Ball import Ball
import sys
import random
from src.basics.capi6.button.SimpleButton import SimpleButton

# Definir as constantes
preto = (0, 0, 0)
branco = (255, 255, 255)
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
oFrameCountLabel = SimpleText(window, (10, 10), 'Programa está rodando', branco)
oFrameCountDisplay = SimpleText(window, (500, 20), '', branco )
oRestartButton = SimpleButton(window, (280, 60), 
                      'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if oRestartButton.handleEvent(event):
            frameCounter = 0  # clicked button, reset counter

    # 8 - Do any "per frame" actions
    oBall.update()  # tell the ball to update itself
    frameCounter = frameCounter + 1  # increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))

   # 9 - Clear the window before drawing it again
    window.fill(preto)
    
    # 10 - Draw the window elements
    oBall.draw()   # tell the ball to draw itself
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    relogio.tick(FRAMES_POR_SEGUNDO)  # make pygame wait 