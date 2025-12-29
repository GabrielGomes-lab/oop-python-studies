# 1- Importando os pacotes
import pygame 
from pygame.locals import *
import sys

# Definindo constantes 
preto = (0, 0, 0)
window_width = 640
window_height = 480
frames_por_segundo = 30

# 3- Inicializando o mundo 
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
relogio = pygame.time.Clock()

# 4 - Load assets: images, sounds, etc
ballImage = pygame.image.load('src/basics/pygame/PygameDemo1_OneImage/images/ball.png')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8  Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(preto)
    
    # 10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    relogio.tick(frames_por_segundo)  # make pygame wait