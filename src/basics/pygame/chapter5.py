"""
Detalhes da tela e seus pixeis.

Uma tela de computador é omposta por um grande numero de linhas e colunas e pequenos quadrados chamados pixels, que vem da palavra
picture element (elemento de imagem). Um usuário interage com a GUI (Graphical User Interface - Interface Gráfica do Usuário) através de uma ou mais telas. 
Uma tela pode ser definida pelo plano cartesiano de coordenadas x e y, então podemos encontrar qualquer ponto na tela utilizando (x, y) onde x é a coordenada horizontal e y é a coordenada vertical.
O ponto (0, 0) está localizado no canto superior esquerdo da tela. A coordenada x aumenta à medida que nos movemos para a direita e a coordenada y aumenta à medida que nos movemos para baixo.
O eixo y é invertido em relação ao plano cartesiano tradicional, onde o valor y aumenta à medida que nos movemos para cima.  
O eixo x e y são sempre inteiros não negativos. A largura e a altura da tela são medidas em pixels.
"""

""" Quando escrevemos um progrma com o pygame precisamos especificar o tamanho da janela que queremos criar"""

""" 
Cores dos pixeis

Todos os pixeis são combinações de três cores primárias: vermelho, verde e azul (RGB - Red, Green, Blue). Cada cor primária pode ter um valor entre 0 e 255, onde 0 significa que a cor não está presente e 
255 significa que a cor está na sua intensidade máxima.
Podemos escrever no pygame as cores utilizando tuplas de três valores inteiros, por exemplo:
black = (0, 0, 0)       # preto
white = (255, 255, 255) # branco
red   = (255, 0, 0)     # vermelho
green = (0, 255, 0)     # verde
blue  = (0, 0, 255)     # azul
yellow= (255, 255, 0)   # amarelo
cyan  = (0, 255, 255)   # ciano
magenta=(255, 0, 255)   # magenta
"""

""" Event-Driven Programming
Em interfaces de usuário, nós não utilizamos input() para receber dados do usuário ou até mesmo print() para mostrar informações, 
em vez disso, utilizamos eventos (events). Eventos são ações que ocorrem na interface do usuário, como clicar em um botão, mover o mouse ou pressionar uma tecla.

O conceito central de event-drive é o conceito de eventos. Eventos são dificeis de definir e são melhores descritos com exemplo, como um clique do mouse e pressionar uma tecla. 
"""

""" Usando o Pygame - Abrindo uma janela em branco

Como dito anteriormente, pygame roda em um loop infinito, onde ele fica verificando os eventos. 
Vamos ao template básico que pode ser utilizado em quase todos os programas em pygame.
"""
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


# 4- Carregar recursos do jogo (imagens, sons, etc)


# 5- Variaveis iniciais do jogo


# 6- Loop principal do jogo
"""while True:
    # 6.1- Tratando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()"""

# 7 - Do any "per frame" actions


# 8 - Limpar a tela

window.fill(preto)

# 9 - Desenhar na tela

#10- Atualizar a tela
pygame.display.update()

# Diminuindo o ritmo

relogio.tick(frames_por_segundo)


""" Explicação do código acima:
1- Importando os pacotes: Importamos o pygame e outros pacotes necessários.
2- Definindo constantes: Definimos algumas constantes que serão usadas no jogo, como a cor preta, largura e altura da janela e frames por segundo.
3- Inicializando o mundo: Inicializamos o pygame e criamos a janela do jogo.
4- Carregar recursos do jogo: Aqui é onde carregaríamos imagens, sons e outros recursos
5- Aqui, eventualmente, inicializaremos quaisquer variáveis ​​que nosso programa usará. Atualmente, não temos nenhuma, portanto, não há código aqui.
6- Loop principal do jogo: Este é o loop infinito onde o jogo roda. Dentro deste loop, tratamos os eventos, atualizamos o estado do jogo, limpamos a tela, desenhamos na tela e atualizamos a tela.
6.1- Tratando eventos: Aqui, verificamos os eventos que ocorrem na
 interface do usuário. Se o evento for QUIT (fechar a janela), encerramos o pygame e saímos do programa.
7- Do any "per frame" actions: Nesta seção, eventualmente, incluiremos qualquer código que precise ser executado em cada
frame. Isso pode envolver mover objetos na janela ou verificar
colisões entre elementos. Neste programa minimalista, não temos nada
a fazer aqui.
8- Limpar a tela:Em cada iteração do loop principal, nosso programa precisa redesenhar
tudo na janela, o que significa que precisamos limpá-la primeiro. A
abordagem mais simples é apenas preencher a janela com uma cor, o que fazemos aqui
com uma chamada a window.fill(), especificando um fundo preto. Também poderíamos
desenhar uma imagem de fundo, mas vamos deixar isso para depois.

9- Desenhar na tela: Aqui, vamos inserir o código para desenhar tudo o que queremos mostrar em nossa janela. Neste programa de exemplo, não há nada para desenhar.
Em programas reais, os elementos são desenhados na ordem em que aparecem no
código, em camadas, da mais posterior para a mais anterior. Por exemplo, suponha que
queremos desenhar dois círculos parcialmente sobrepostos, A e B. Se desenharmos A
primeiro, A aparecerá atrás de B e partes de A serão obscurecidas por B.
Se desenharmos B primeiro e depois A, o oposto acontece e vemos A na
frente de B. Este é um mapeamento natural equivalente às camadas em programas gráficos como o Photoshop.

10- Atualizar a tela: Esta linha instrui o pygame a pegar todo o desenho que incluímos e exibi-lo na janela. O pygame, na verdade, realiza todo o desenho nas etapas 8, 9 e
10 em um buffer fora da tela. Quando você instrui o pygame a atualizar, ele pega o
conteúdo desse buffer fora da tela e o coloca na janela real.
"""

