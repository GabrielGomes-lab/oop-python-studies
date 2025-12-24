""" Construindo um modelo de software de objetos físicos. 
Para descrever objetos fisicos no mundo real, nós fazemos referências aos seus atributos. 
Quando falamos sobre uma mesa, podemos descrever sua cor, tamanho, peso, material. Um carro pode ser descrito por seu numero de portas, mas uma camiseta não. Então existem caracteristicas que servem para
alguns objetos e para outros não. 
Além disso, alguns objetos são capazes de perfomar ações, um carro por de ir para frente, para trás, cima, baixo, esquerda e direita. 
Para modelarmos um objeto do mundo real em código, nós precisamos decidir que dados vamos representar os objetos e quais atributos e operações eles podem performar. 
Esse são dois conceitos;
Esses dois conceitos são chamados de state e behavior (estado e comportamento).
O estado são dados que o objeto lembra e comportamento são ações que o objeto pode realizar.

Estado e comportamento: Exemplo do mundo real: Um interruptor"""

def ligar():
    global swithIsOn
    # Muda o estado do interruptor para ligado
    switchIsOn = True

def desligar():
    global switchIsOn
    # Muda o estado do interruptor para desligado
    switchIsOn = False

# Código Principal
switchIsOn = False # variavel global boleana que guarda o estado do interruptor

# Código de teste
print(switchIsOn) # Deve imprimir False
ligar()
print(switchIsOn) # Deve imprimir True
desligar()
print(switchIsOn) # Deve imprimir False
ligar()
print(switchIsOn) # Deve imprimir True
desligar()

""" O interruptor pode estar em dois estados, ligado ou desligado.
Para modelar o estado nós precisamos apenas de um simples dado boleano. O nome da variável é switchIsOn.
and nós dizemos que está ligado quando switchIsOn é True e desligado quando switchIsOn é False. 

Agora o comportamento. O Interruptor pode perfomar duas ações: ligar e desligar. Portanto nós construimos 
duas funções, ligar() e desligar(). Cada função muda o estado do interruptor.
"""


"""Introdução a classes e objetos

A classe pode ser entendida coo um modelo ou um projeto que define a aparência de um objeto quando ele for criado.
Nós criamos objetos a partir de uma classe.

Como analogia: imagina se criássemos um negócio de bolos sob encomenda. Sendo "sob encomenda", 
só fazemos bolo quando recebemos um pedido. Somos especializados em bolos Bundt e dedicamos muito tempo ao desenvolvimento da forma de bolo para
garantir que nossos bolos não sejam apenas saborosos, mas bonitos e consistentes. 
A forma define a aparencia do bolo, mas não é um bolo em si. A forma representa a classe.
Quando recebemos um pedido criamos o bolo a partir da forma. O bolo é um objeto usando a forma. 
Usando a forma podemos criar qualquer número de bolos. Nossos bolos podem ter atributos diferentes como sabores, tipos, texturas, coberturas, mas ainda sim, todos sairão da mesma forma. 

Então a nossa definição seria:
class: Código que define o que um objeto irá memorizar (seus dados ou estado) e as coisas que ele poderá fazer (suas funções ou comportamento).
 vamos olhar como uma classe se parece"""

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False # atributo que guarda o estado do interruptor
    def turnOn(self):
        self.switchIsOn = True # método que liga o interruptor
    def turnOff(self):
        self.switchIsOn = False # método que desliga o interruptor

""" Vamos observar que o código define uma única variável, 'switchIsOn', que guarda o estado do interruptor.', que é inicializada em uma função
e contem outras duas funções para o comportamento turnOn() e turnOff().

Se escrevermos o código de uma classe e tentar executa-lo, nada acontece, da mesma forma quando você executa um programa em python
que consiste apenas em funções e nenhuma chamada de função. Você precisa dizer para o python criar um objeto a partir de uma classe. Então vamos criar um objeto a partir da classe LightSwitch."""

oLightSwitch = LightSwitch() # cria um objeto a partir da classe LightSwitch

""" Aqui estamos dizendo: encontre a classe LightSwitch, crie um bojeto a partir dessa clase e armazene o resultado do objeto na variável oLightSwitch." Geralmente iremos utilizar o o mínusculo 'o' para indicar que a variável é um objeto."""

"""Outra palavra que você encontrará em POO é instância. As palavras
instância e objeto são essencialmente intercambiáveis; no entanto, para sermos precisos,
diríamos que um objeto LightSwitch é uma instância da classe LightSwitch.

Vamos discutir as diferentes partes de uma classe e os detalhes da instanciação e do uso de um objeto. """

class primeiraclasse():
    def __init__(self): # Toda inicialização do código começa aqui, além do self podemos colocar outros parametros
    # Qualqer número de funções para acessar os dados tem essa forma:
    def minhaFuncao(self, parametro1, parametro2):
        # código da função aqui
        pass
    def minhaFuncaoN(self):
        # código da função aqui
        pass

""" Começamos definindo com a class statement (declaração de classe) o nome da classe. Com o corpo da classe, podemos definir qualquer número de funções
todas as funções são consideradas partes da classe e o código define a modelagem de objetos físicos. Cada função
representa algum comportamento que um objeto criado a partir da classe pode executar. Todas as funções devem ter pelo menos um prametro que por coneção é chamado de self.


O primeiro method que definimos em uma classe é o método __init__(). Sempre que você cria um objeto a partir de uma classe, este método será executado automaticamente. Portando esse método é local, lógico para colocar qualquer código de inicialização que você queria executar sempre que instanciar um objeto de uma classe. 
O Nome __init__ é reservado pelo python para esta tarefa especifica e deve ser escrito exatamente dessa forma, com dois underscores antes e depois da palavra init.

o init é onde eu defino como todo objeto da classe nasce, para op exemplo do interruptor, o papel do __init__ é o seguinte: "Toda vez que um intrruptor for criado, ele começa desligado". Isso é importante, já que sem isso o interruptor não teria um estado inicial, então um objeto não pode nascer sem estado e o init é o que garante isso
Então quando fazemos o light_switch = LightSwitch(), o init é chamado automaticamente e o atributo switchIsOn é inicializado como False, ou seja, já representa um interruptor real desligado."""

""" Escopo e Instancia de Variaveis" Temos dois principais níveis de escopos, variaveis criadas no código principal tem 
global scope (escopo global) e variaveis criadas dentro de funções tem local scope (escopo local). Variaveis com escopo local só podem ser acessadas dentro da função onde foram criadas. Variaveis com escopo global podem ser acessadas de qualquer lugar do código, incluindo dentro de funções.
Orientação a objetos e classes introduziram um terceiro nivel de escopo, chamado "object scope" (escopo de objeto). 
Em um método qualquer variável que não comece com 'self' é uma variável local e será descartada quando o método terminar, o que significa que outros métodos dentro da classe não poderão utilizar mais essa variável. As variáveis de instância tem escolpo de objeto, o que significa que estão disponíveis para todos os métodos definidos em uma classe."""

class MinhaClasse:
    def __init__(self):
        self.count = 0  # variável de instância com escopo de objeto, disponível para todos os métodos da classe e indica que irá iniciar em 0, é o estado inicial. 
    def incrementar(self):
        self.count += 1  # acessa a variável de instância e incrementa seu valor em 1

""" Diferenças entre funções e métodos:
1. Todos os métodos de uma classe devem ser indentados abaixo da declaração da classe.
2. Todos os métodos têm um primeiro parâmetro especial é chamado __self__
3. Os métodos em uma classe podem usar variáveis de instância que são escritas no formato self.<nomeDaVariavel>.

Criando um objeto de uma classe
Como dito anteriomemente, uma classe apenas define como o objeto se parece, para usar a classe precisamos dizer ao python para criar um objeto a partir da classe da seguinte forma:
nomeDoObjeto = NomeDaClasse(argumentosopcionais).


Chamando métodos em um objeto
Depois de criar um objeto a partir de uma classe, podemos chamar os métodos definidos na classe usando a seguinte sintaxe:
nomeDoObjeto.nomeDoMetodo(argumentosopcionais) Vamos ao exemplo do interruptor."""

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False # Atributo que guarda o estado do interruptor e como ele começa
    def turnOn(self):
        self.switchIsOn = True # Função que liga o switch
    def turnOff(self):
        self.switchIsOn = False # Função que desliga o switch
    def show(self): # Função que mostra o estado do switch
        print(self.switchIsOn)

# Código principal
oLightSwitch = LightSwitch() # Cria um objeto a partir da classe LightSwitch

# Chamando os métodos
oLightSwitch.show() # Deve imprimir False
oLightSwitch.turnOn() # Liga o interruptor
oLightSwitch.show() # Deve imprimir True
oLightSwitch.turnOff() # Desliga o interruptor
oLightSwitch.show() # Deve imprimir False
oLightSwitch.turnOn() # Liga o interruptor
oLightSwitch.show() # Deve imprimir True

""" Criando multipasl instancias da mesma classe"""
""" Uma das chaves é que podemos instanciar muits objetos a partir de uma mesma classe. Então se nós quisermos dois objetos interruptores, nós podemos criar objetos adicionais:
oLightSwitch1 = LightSwitch() # Cria o primeiro objeto a partir da classe LightSwitch
oLightSwitch2 = LightSwitch() # Cria o segundo objeto a partir da classe Light

Um importante ponto é que cada objeto mantém seu próprio estado independente dos outros objetos. Então se nós ligarmos o primeiro interruptor, o segundo permanecerá desligado."""


""" Definição formal de objeto:
Dado, mas codigo que define o estado e comportamento de um objeto físico no mundo real. Um objeto é uma instancia de uma classe.""""

""" Construindo uma classe um pouco mais complicada:
Vamos fazer um dimmer switch (interruptor com regulagem de intensidade de luz). class. 
Esse tipo de interruptor tem o ligar e desligar, mas também tem múltiplas posições de slides para ajustar a luminosidade. 
Então, temos 11 posições, indo de 0 a 10, onde 0 é desligado e 10 é o mais brilhante.
Então o dimmer swith tem mais funcionalidades que o interruptor simples.
O ligado e desligado
e o nível de luminosidade. 

E os comportamentos que o objeto pode perfomar:
ligar
desligar
diminuir a luminosidade
aumentar a luminosidade
mostrar o estado atual"""

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False # Atributo que guarda o estado do interruptor desligado
        self.brightnessLevel = 0 # Atributo que guarda o nível de luminosidade, começa em 0
    def turnOn(self):
        self.switchIsOn = True # Função que liga o interruptor
    def turnOff(self):
        self.switchIsOn = False # Função que desliga o interruptor
    def aumentarnivel(self):
        if self.brightnessLevel < 10:
            self.brightnessLevel += 1 # Aumenta o nível de luminosidade em 1
    def diminuirnivel(self):
        if self.brightnessLevel > 0:
            self.brightnessLevel -= 1 # Diminui o nível de luminosidade em 1
    def show(self): # Função que mostra o estado do interruptor e o nível de luminosidade
        print("Switch is On:", self.switchIsOn, "Brightness Level:", self.brightnessLevel)

odimer = DimmerSwitch() # Cria um objeto a partir da classe DimmerSwitch
odimer.show() # Deve imprimir Switch is On: False Brightness Level: 0
odimer.turnOn() # Liga o interruptor
odimer.aumentarnivel() # Aumenta o nível de luminosidade

""" nesse __init__ metodo nós tems duas instancias de variavel: self.switchIsOn e self.brightnessLevel.
a primeira guarda o estado do interruptor e a segunda guarda o nível de luminosidade.
Além dos métodos turnOn() e turnOff() que ligam e desligam o interruptor, nós temos dois novos métodos: aumentarnivel() e diminuirnivel()"""

""" Representando um objeto físico mais complicado"

Controle Remoto de televisão"""

class TV():
    def __init__(self):
        self.powerIsOn = False # Atributo que guarda o estado da TV desligada
        self.ismuted = False # Atributo que guarda o estado do mudo desligado
        self.channelList = [2, 4, 5, 7, 9, 11, 13, 14, 15, 18, 20, 22, 24, 26, 28, 30] # Lista de canais disponíveis
        self.nChannels = len(self.channelList) # Número de canais disponíveis
        self.currentChannelIndex = 0 # Índice do canal atual na lista de canais
        self.VOLUME_MAX = 10 # Volume máximo
        self.volume_MIN = 0 # Volume mínimo
        self.volume = self.VOLUME_MAX // 2 # Volume inicial no meio do máximo
    def power(self):
        self.powerIsOn = not self.powerIsOn # Alterna o estado da TV
    def volumeUp(self):
        if not self.powerIsOn:
            return
        if self.ismuted:
            self.ismuted = False # Desliga o mudo se estiver ligado
        if self.volume < self.VOLUME_MAX:
            self.volume += 1 # Aumenta o volume em 1
    def volumeDown(self):
        if not self.powerIsOn:
            return
        if self.ismuted:
            self.ismuted = False # Desliga o mudo se estiver ligado
        if self.volume > self.volume_MIN:
            self.volume -= 1 # Diminui o volume em 1
    def channelUp(self):
        if not self.powerIsOn:
            return
        self.channelIndex = self.currentChannelIndex + 1 # Incrementa o índice do canal
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 # Volta ao primeiro canal se ultrapassar o número de canais
    def channelDown(self):
        if not self.powerIsOn:
            return
        self.channelIndex = self.currentChannelIndex - 1 # Decrementa o índice do canal
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # Vai para o último canal se for menor que 0
    def mute(self):
        if not self.powerIsOn:
            return
        self.ismuted = not self.ismuted # Alterna o estado do mudo
    def setChannel(self, newChannel):
        if not self.powerIsOn:
            return
        if newChannel in self.channelList:
            self.currentChannelIndex = self.channelList.index(newChannel) # Define o canal atual pelo índice
    def show(self):
        print('')
        print('TV STATUS')
        if self.powerIsOn:
            print('Power: ON')
            print('Channel:', self.channelList[self.currentChannelIndex])
            if self.ismuted:
                print('Volume: MUTED')
            else:
                print('Volume:', self.volume)
        else:
            print('Power: OFF')

""" O __init__ método inicializa vários atributos para representar o estado da TV, incluindo powerIsOn, ismuted, channelList, currentChannelIndex e volume.
Uma boa pratica de programação é definir todas as variáveis de instância no __init__ método para que fique claro quais dados o objeto irá armazenar."""

# Código principal para testar a classe TV
oTV = TV() # Cria um objeto a partir da classe TV
oTV.show() # Deve imprimir o estado inicial da TV
oTV.power() # Liga a TV
oTV.show() # Deve imprimir o estado da TV ligada
oTV.volumeUp() # Aumenta o volume

""" Passando argumentos para um método
Quando chamamos qualquer funçõa, o número de argumentos passados deve ser igual ao número de parametros listados na definição da função.
O mesmo vale para métodos em uma classe. O primeiro parâmetro de qualquer método é sempre self
Por exemplo na definição do power(), quando criamos a função usamos o def power(self):, mas quando chamamos o método usamos oTV.power() sem passar nenhum argumento, isso parece estranho
se compararmos com a setChannel(), que aceita dois parametros, mas quando chamamos a função passamos apenas um oTV.setChannel(11).
A razão para isso é que o python passa automaticamente o objeto chamador como o primeiro argumento para o método.
Então quando chamamos oTV.power(), o python automaticamente passa o objeto oTV como o primeiro argumento para o método power(self), então dentro do método, self se refere ao objeto oTV.

Então quando fazemos def setChanel(self, newChannel): e chamamos oTV.setChannel(11), o python passa automaticamente o objeto oTV como o primeiro argumento (self) e 11 como o segundo argumento (newChannel).

A capacidade de passar argumentos para chamadas de método também funciona ao instanciar um objeto. Até agora, ao criarmos nossos objetos, sempre definimos suas
variáveis ​​de instância com valores constantes. No entanto, você frequentemente desejará criar
instâncias diferentes com valores iniciais diferentes. Por exemplo, imagine que
queremos instanciar diferentes TVs e identificá-las usando sua marca
e localização. Dessa forma, podemos diferenciar entre uma televisão Samsung
na sala de estar e uma televisão Sony no quarto. Valores constantes
não funcionariam para nós nessa situação.

Para inicializar um objeto com valores diferentes, adicionamos parâmetros à
definição do método __init__(), assim:"""
class TV():
 def __init__(self, brand, location): # Adiciona parâmetros brand e location
     self.brand = brand # Atributo que guarda a marca da TV
     self.location = location # Atributo que guarda a localização da TV

""" Usando esse desenvolvimento podemos criar diferentes objetos TV com marcas e localizações diferentes:"""
tv1 = TV("Samsung", "Living Room") # Cria um objeto TV com marca
tv2 = TV("Sony", "Bedroom") # Cria outro objeto TV com marca diferente

""" Agora podemos modificar o showInfo() para reportar o nome e localização da tv:"""
    def showInfo(self):
        print("TV Brand:", self.brand, "Location:", self.location)
        