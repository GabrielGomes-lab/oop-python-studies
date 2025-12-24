"""
Capitulo 1 - P R O C E D U R A L P Y T H O N
EXAMPLES" 

Primeiro exemplo: um cardgame simples, chamado Higher or Lowe, nesse jogo, oitro cartas são escolhidas aleatoriamente de um deck, a primeira carta está com a face para cima, o jogo pede para que o jogador 
adinhve se a próxima carta é maior ou menor que a carta atual, se o jogador escolher corretamente, ele ganha 20 pontos, e se escolher incorretamente ele perde 15 pontos, e se a próxima carta virada for o
 mesmo valor da carta atual, o jogador perde 15 pontos, e é considerado incorreto .

Repressentação das cartas:
O programa precisa representar um deck de 52 cartas, assim, vamos construir uma lista com 52 elementos, e dentro dessa lista haverá um dicionário (set of key/value pairs). 
Para representar qualquer carta, cada dicionario terá três chaves: 'suit' (naipe), 'rank' (valor) e 'value' (valor numérico).
o Rank é o nome da carta (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A), mas o valor usado para comparar as cartas são inteiros, por exemplo "The Jack of Clubs" deverá ser representado da seguinte forma pelo dicionário:
{'rank': 'Jack', 'suit': 'Clubs', 'value': 11}
Vamos ao código"
"""
import random

naipe_lista = ('Espadas', 'Copas', 'Ouros', 'Paus')
rank_lista = ('Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei')
ncards = 8

# Passe um baralho como parâmetro e esta função retorna uma carta aleatória do baralho.
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Remove a última carta do baralho e a retorna
    return thisCard # Retorna a carta removida

# Passe um baralho como parâmetro e esta função retorna uma cópia embaralhada do baralho.
def embaralhar(deckListIn):
    deckListOut = deckListIn.copyu() # Cria uma cópia do baralho original
    random.shuffle(deckListOut) # Embaralha o baralho copiado
    return deckListOut # Retorna o baralho embaralhado

# Main Code
print('Bem vindo ao jogo Higher or Lower!')
print('Você tem que escolher se a próxima carta é maior ou menor que a carta atual.')
print('Você ganha 20 pontos para cada resposta correta e perde 15 pontos para cada resposta incorreta.')
print('Você inicia com 50 pontos')
print()

# Cria o deck de cartas como uma lista de dicionários
startingDeckList = []  #Lista vazia para armazenar o deck de cartas

for naipe in naipe_lista:
    for thisValue, rank in enumerate(rank_lista): # Loop através dos valores e ranks usando enumerate para obter o índice (thisValue) e o valor (rank)
        cardDict = {'rank': rank, 'suit': naipe, 'value': thisValue + 1} # Cria o dicionário para a carta atual
        startingDeckList.append(cardDict) # Adiciona o dicionário da carta à lista do deck

pontos  = 50

while True:
    print()
    gameDeckList = embaralhar(startingDeckList) # Embaralha o deck de cartas
    currentCard = getCard(gameDeckList) # Pega a primeira carta do deck embaralhado
    currentCardRank = currentCard['rank'] # Obtém o rank da carta atual
    currentCardSuit = currentCard['suit'] # Obtém o naipe da carta atual
    currentCardValue = currentCard['value'] # Obtém o valor numérico da carta atual
    print(f'A carta inicial é: {currentCardRank} de {currentCardSuit}')
    print()

    for cardNumber in range(0, ncards): #Jogar um jogo of this many cards
        resposta = input('A próxima carta é maior ou menor que' + currentCardRank + 'de' + currentCardSuit + '? (Digite "m" para maior, "l" para menor): ')
        resposta = resposta.casefold() # Converte a resposta para minúsculas para facilitar a comparação
        nextCard = getCard(gameDeckList) # Pega a próxima carta do deck
        nextCardRank = nextCard['rank'] # Obtém o rank da próxima carta
        nextCardSuit = nextCard['suit'] # Obtém o naipe da próxima
        nextCardValue = nextCard['value'] # Obtém o valor numérico da próxima carta
        print(f'A próxima carta é: {nextCardRank} de {nextCardSuit}')
        if resposta = 'm':
            if nextCardValue > currentCardValue:
                pontos += 20
                print('Você acertou! Você ganhou 20 pontos.')
            else:
                pontos -= 15
                print('Você errou! Você perdeu 15 pontos.')
        elif resposta = 'l':
            if nextCardValue < currentCardValue:
                pontos += 20
                print('Você acertou! Você ganhou 20 pontos.')
            else:
                pontos -= 15
                print('Você errou! Você perdeu 15 pontos.')
        print(f'Seu total de pontos é: {pontos}')
        print()
        currentCardRank = nextCardRank # Atualiza a carta atual para a próxima carta
        currentCardSuit = nextCardSuit # Atualiza o naipe da carta atual para o naipe da próxima carta
        currentCardValue = nextCardValue # Atualiza o valor da carta atual para o valor da próxima carta

    jogar_novamente = input('Para Jogar novamente, pressione enter, ou "q" para sair: ')
    if jogar_novamente.casefold() = 'q':
        break

print('Obrigado por jogar Higher or Lower! Até a próxima.')


"""Código Reutilizável:
Se nós quisermos escrever outro cardgame, seria bom estar apto a usar o codigo para o deck e cartas. Em um procedural program, pode ser dificil de identificar todas as peças do codigo associadas a uma parte do programa. 
"""

"""Segundo exemplo de procedural coding. Iremos apresentar um numero de variações de um programa que 
simula um banco. em cada nova versão do programa nós iremos adicionar mais funcionalidades. 
Para iniciar, considere que operações um cliente pode querer fazer com uma conta no banco e que dados serão necessários para representar a conta.

Análise de Operações Requeridas e dados:
* Criar conta
* Deposito
* Retirada (saque)
* Checar saldo

Agora uma pequena lista de dados nós poderiamos precisar para representar uma conta:
* Nome do cliente
* Senha
* Saldo

Note que todas as operações são ações (verbos) e os dados são substantivos (nomes). Uma conta real poderia ser capaz de muitas outras operações, contendo 
outras formas de dados. Mas para começar iremos apenas com essas quatro ações e esses três dados.
"""
# Banco Simples - Versão 1

accountName = 'Joe' # Nome da conta
accountBalance = '100' # Saldo da conta
accountPassword = 's3cr3t'  # Senha da conta

while True: # Loop principal do programa
    print()
    print('Pressione b para checar o saldo') # Opção de checar saldo
    print('Pressione d para fazer um depósito') # Opção de depósito
    print('Pressione w para fazer um saque') # Opção de saque
    print('Pressione s para mostrar a conta') # Opção de mostrar detalhes da conta
    print('Pressione q para sair') # Opção de sair
    print() 

    action = input('O que você gostaria de fazer? ') # Solicita a ação do usuário
    action = action.casefold() # Converte a entrada para minúsculas
    action = action[0]  # Pega apenas o primeiro caractere da entrada do usuário
    print()

    if action == 'b':
        print('Seu saldo:')
        userPassword = input('Por favor, insira sua senha: ')
        if userPassword != accountPassword:
            print('Senha incorreta! Acesso negado.')
        else:
            print(f'Seu saldo é: ${accountBalance}')
    elif action == 'd':
        print('Depósito:')
        userDepositAmount = input('Quanto você gostaria de depositar? $')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Por favor, insira sua senha: ')

        if userDepositAmount < 0:
            print('Você não pode depositar um valor negativo!')
        elif userPassword != accountPassword:
            print('Senha incorreta! Acesso negado.')
        else:
            accountBalance += userDepositAmount
            print(f'Você depositou: ${userDepositAmount}')
            print(f'Seu novo saldo é: ${accountBalance}')
    elif action == 's':
        print('Show:')
        print('      Name', accountName)
        print('      Balance', accountBalance)
        print('      Password', accountPassword)
    elif action == 'q':
        print('Obrigado por usar o banco. Até a próxima!')
        break
    elif:
        action == 'w':
        print('Saque:')
        userWithdrawAmount = input('Quanto você gostaria de sacar? $')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Por favor, insira sua senha: ')
        if userWithdrawAmount < 0:
            print('Você não pode sacar um valor negativo!')
        elif userWithdrawAmount > accountBalance:
            print('Saldo insuficiente para este saque!')
        elif userPassword != accountPassword:
            print('Senha incorreta! Acesso negado.')
        else:
            accountBalance -= userWithdrawAmount
            print(f'Você sacou: ${userWithdrawAmount}')
            print(f'Seu novo saldo é: ${accountBalance}')


""" Nesse exemplo, todas as ações estão no nível principal, não há funções no código. O programa funciona, mas é um pouco longo
Uma abordagem típica para tornar programas mais longos mais claros é mover o código relacionado para funções e fazer chamadas para essas funções. Exploraremos isso na próxima implementação do programa bancário.
"""

# Banco simples - Versão 2 com funções

accountName = ''
accountBalance = 0
accountPassword = ''

def criarConta(nome, saldo, senha):
    global accountName, accountBalance, accountPassword
    accountName = nome
    accountBalance = saldo
    accountPassword = senha

def show():
    global accountName, accountBalance, accountPassword
    print('      Name', accountName)
    print('      Balance', accountBalance)
    print('      Password', accountPassword)
    print()

def getBalance(Password):
    global accountBalance, accountPassword, accountName
    if Password != accountPassword:
        print('Senha incorreta! Acesso negado.')
        return None
    return accountBalance

def deposit(qtdDeposito, password):
    global accountBalance, accountPassword, accountName
    if qtdDeposito < 0:
        print('Você não pode depositar um valor negativo!')
        return None
    if password != accountPassword:
        print('Senha incorreta! Acesso negado.')
        return None
    accountBalance += qtdDeposito
    return accountBalance

def saque(qtdSaque, password):
    global accountBalance, accountPassword, accountName
    if qtdSaque < 0:
        print('Você não pode sacar um valor negativo!')
        return None
    if qtdSaque > accountBalance:
        print('Saldo insuficiente para este saque!')
        return None
    if password != accountPassword:
        print('Senha incorreta! Acesso negado.')
        return None
    accountBalance -= qtdSaque
    return accountBalance

# Agora vamos criar uma conta
criarConta('Joe', 100, 's3cr3t')

while True: # Loop principal do programa
    print()
    print('Pressione b para checar o saldo') # Opção de checar saldo
    print('Pressione d para fazer um depósito') # Opção de depósito
    print('Pressione w para fazer um saque') # Opção de saque
    print('Pressione s para mostrar a conta') # Opção de mostrar detalhes da conta
    print('Pressione q para sair') # Opção de sair
    print() 

    action = input('O que você gostaria de fazer? ') # Solicita a ação do usuário
    action = action.casefold() # Converte a entrada para minúsculas
    action = action[0]  # Pega apenas o primeiro caractere da entrada do usuário
    print()

    if action == 'b':
        print('Seu saldo:')
        userPassword = input('Por favor, insira sua senha: ')
        balance = getBalance(userPassword)
        if balance is not None:
            print(f'Seu saldo é: ${balance}')
    elif action == 'd':
        print('Depósito:')
        userDepositAmount = input('Quanto você gostaria de depositar? $')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Por favor, insira sua senha: ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print(f'Você depositou: ${userDepositAmount}')
            print(f'Seu novo saldo é: ${newBalance}')
    elif action == 's':
        print('Show:')
        show()
    elif action == 'q':
        print('Obrigado por usar o banco. Até a próxima!')
        break
    elif action == 'w':
        print('Saque:')
        userWithdrawAmount = input('Quanto você gostaria de sacar? $')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Por favor, insira sua senha: ')
        newBalance = saque(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print(f'Você sacou: ${userWithdrawAmount}')
            print(f'Seu novo saldo é: ${newBalance}')

""" Nessa versão, nós construimos funções para cada operação que nós identificamos para a criação de uma conta no banco, e 
rearranjamos o código para que o código principal contenha chamadas para diferentes funções.
Como resultado, o programa está muito mais legivel. POr exemplo, se o usuário inserir d
para indicar que ele quer realizar um depósito, o código principal chama a função deposit() e o código relacionado ao depósito está todo dentro dessa função.

Se você observar em toda a extensão do código usamos declarações globais para acessar (obter ou definir) as variáveis que representam a conta. 
Em Python, uma declaração globl só é necessária se você quiser alterar o valor de uma variável global em uma função. 
Como princípio geral de programação, as funções nunca devem modificar variáveis 
​​globais. Uma função deve apenas usar os dados que lhe são passados,
 fazer cálculos com base nesses dados e, potencialmente, retornar um ou mais resultados. 
 A função `withdraw()` neste programa funciona, mas viola essa regra ao modificar o valor da variável global `accountBalance` 
(além de acessar o valor da variável global `accountPassword`)."""

# Banco simples - Versão 3/ Duas contas

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

        if accountNumber == 0:
    account0Name = name
    account0Balance = balance
    account0Password = password
        if accountNumber == 1:
    account1Name = name
    account1Balance = balance
    account1Password = password

def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if account0Name != '':
    print('Account 0')
    print(' Name', account0Name)
    print(' Balance:', account0Balance)
    print(' Password:', account0Password)
    print()
    if account1Name != '':
    print('Account 1')
    print(' Name', account1Name)
    print(' Balance:', account1Balance)
    print(' Password:', account1Password)
    print()
def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
    if password != account0Password:
    print('Incorrect password')
    return None
    return account0Balance
    if accountNumber == 1:
    if password != account1Password:
    print('Incorrect password')
    return None
    return account1Balance
def deposit(accountNumber, depositAmount, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if depositAmount < 0:
    print('You cannot deposit a negative amount!')
    return None
    if accountNumber == 0:
    if password != account0Password:
    print('Incorrect password')
    return None
    account0Balance += depositAmount
    return account0Balance
    if accountNumber == 1:
    if password != account1Password:
    print('Incorrect password')
    return None
    account1Balance += depositAmount
    return account1Balance
def withdraw(accountNumber, withdrawAmount, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if withdrawAmount < 0:
    print('You cannot withdraw a negative amount!')
    return None
    if accountNumber == 0:
    if withdrawAmount > account0Balance:
    print('Insufficient funds for this withdrawal!')
    return None
    if password != account0Password:
    print('Incorrect password')
    return None
    account0Balance -= withdrawAmount
    return account0Balance
    if accountNumber == 1:
    if withdrawAmount > account1Balance:
    print('Insufficient funds for this withdrawal!')
    return None
    if password != account1Password:
    print('Incorrect password')
    return None
    account1Balance -= withdrawAmount
    return account1Balance

while True:
    print()
    print('Press n to create a new account')
    print('Press b to check balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show accounts')
    print('Press q to quit')
    print()

    action = input('What would you like to do? ')
    action = action.casefold()
    action = action[0]
    print()

    if action == 'n':
        if nAccounts >= 2:
            print('Maximum number of accounts reached.')
        else:
            name = input('Enter account name: ')
            balance = int(input('Enter initial balance: $'))
            password = input('Enter account password: ')
            newAccount(nAccounts, name, balance, password)
            nAccounts += 1
            print(f'Account {nAccounts - 1} created successfully.')
    elif action == 'b':
        accountNumber = int(input('Enter account number (0 or 1): '))
        password = input('Please enter your password: ')
        balance = getBalance(accountNumber, password)
        if balance is not None:
            print(f'Your balance is: ${balance}')
    elif action == 'd':
        accountNumber = int(input('Enter account number (0 or 1): '))
        depositAmount = int(input('How much would you like to deposit? $'))
        password = input('Please enter your password: ')
        newBalance = deposit(accountNumber, depositAmount, password)
        if newBalance is not None:
            print(f'You deposited: ${depositAmount}')
            print(f'Your new balance is: ${newBalance}')
    elif action == 's':
        print('Show:')
        show()
    elif action == 'q':
        print('Thank you for using the bank. Goodbye!')
        break
    elif action == 'w':
        accountNumber = int(input('Enter account number (0 or 1): '))
        withdrawAmount = int(input('How much would you like to withdraw? $'))
        password = input('Please enter your password: ')
        newBalance = withdraw(accountNumber, withdrawAmount, password)
        if newBalance is not None:
            print(f'You withdrew: ${withdrawAmount}')
            print(f'Your new balance is: ${newBalance}')

""" Mesmo com apenas duas contas, vemos que essa abordagem rapidamente sai do controle. Primeiro, 
definimos três variaveis globais para cada conta. Além disso, cada função agora precisa de um IF para escolher qual conjunto
de variáveis globais acessar ou alterar. Sempre que quisermos adicionar outra conta, precisaremos 
adiconar outro conjunto de variáveis globais e mais instruções if em cada função. Então agora precisamos de uma 
abordagem diferente para lidar com um número arbitrário de contas."""

# Banco Simples - Versão 4/ Contas Múltiplas com listas de dicionários

""" Para ser mais simples de acomodar multiplas contas, nos iremos representar os dados usando
istas. Iremos usar três listas paralelas nessa versão do programa."""
accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def show():
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Accounts:', accountNumber)
    print(' Name:', accountNamesList[accountNumber])
    print(' Balance:', accountBalancesList[accountNumber])
    print(' Password:', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    global accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def deposit(accountNumber, depositAmount, password):
    global accountBalancesList, accountPasswordsList
    if depositAmount < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    accountBalancesList[accountNumber] += depositAmount
    return accountBalancesList[accountNumber]

def withdraw(accountNumber, withdrawAmount, password):
    global accountBalancesList, accountPasswordsList
    if withdrawAmount < 0:
        print('You cannot withdraw a negative amount!')
        return None
    if withdrawAmount > accountBalancesList[accountNumber]:
        print('Insufficient funds for this withdrawal!')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    accountBalancesList[accountNumber] -= withdrawAmount
    return accountBalancesList[accountNumber]

print('Joe, o número da sua conta é:', len(accountNamesList))
newAccount('Joe', 100, 's3cr3t')
print('Mary, o número da sua conta é:', len(accountNamesList))
newAccount('Mary', 50, 'p4ssw0rd')

while True:
    print()
    print('Press n to create a new account')
    print('Press b to check balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show accounts')
    print('Press q to quit')
    print()

    action = input('What would you like to do? ')
    action = action.casefold()
    action = action[0]
    print()

    if action == 'n':
        name = input('Enter account name: ')
        balance = int(input('Enter initial balance: $'))
        password = input('Enter account password: ')
        newAccount(name, balance, password)
        accountNumber = len(accountNamesList) - 1
        print(f'Account {accountNumber} created successfully.')
    elif action == 'b':
        accountNumber = int(input('Enter account number: '))
        password = input('Please enter your password: ')
        balance = getBalance(accountNumber, password)
        if balance is not None:
            print(f'Your balance is: ${balance}')
    elif action == 'd':
        accountNumber = int(input('Enter account number: '))
        depositAmount = int(input('How much would you like to deposit? $'))
        password = input('Please enter your password: ')
        newBalance = deposit(accountNumber, depositAmount, password)
        if newBalance is not None:
            print(f'You deposited: ${depositAmount}')
            print(f'Your new balance is: ${newBalance}')
    elif action == 's':
        print('Show:')
        accountNumber = int(input('Enter account number: '))
        show(accountNumber)
    elif action == 'q':
        print('Thank you for using the bank. Goodbye!')
        break
    elif action == 'w':
        accountNumber = int(input('Enter account number: '))
        withdrawAmount = int(input('How much would you like to withdraw? $'))
        password = input('Please enter your password: ')
        newBalance = withdraw(accountNumber, withdrawAmount, password)
        if newBalance is not None:
            print(f'You withdrew: ${withdrawAmount}')
            print(f'Your new balance is: ${newBalance}')

""" No começo do programa, nós criamos três listas vazias. Para criar novas contas, nós fizemos um append dos valores para cada 
uma das três listas.
Agora, estamos usando um conceito básico de número de uma conta bancaria. Cada vez que o usuário criar uma conta, o código usara a função len()
e retornará o número de contas existentes. Qundo criamos a conta para o primeiro usuário, o tamanho de accountnamelist é zero. Então, o primeiro
usuário recebe o número da conta 0. Quando o segundo usuário cria uma conta, o tamanho da lista é 1, então o segundo usuário recebe o número da conta 1.
Esse sistema de numeração funciona porque as listas em Python são indexadas a partir de zero."""

"""Os dados são mantidos como três listas globais do Python, onde cada lista
representa uma coluna nesta tabela.
 todas as senhas estão agrupadas em uma lista. Os
nomes dos usuários estão agrupados em outra lista e os saldos estão agrupados em
uma terceira lista. Com essa abordagem, para obter informações sobre uma conta, você
precisa acessar essas listas com um valor de índice comum.

Embora isso funcione, parece extremamente estranho. Os dados não estão agrupados de
uma maneira lógica. Por exemplo, não parece correto manter todas as senhas dos usuários
juntas. Além disso, toda vez que você adiciona um novo atributo a uma conta, como um
endereço ou número de telefone, você precisa criar e acessar outra lista global."""


# Banco Simples - Versão 5/ Contas Múltiplas com dicionários

"""Neste livro, sempre que eu apresentar um valor entre colchetes angulares (<>), isso significa que você deve
substituir esse item (incluindo os colchetes) por um valor de sua escolha. Por exemplo,
na linha de código anterior, <someName>, <somePassword> e <someBalance> são marcadores de posição e devem ser substituídos por valores reais.
"""

accountsList = []  # Lista para armazenar todas as contas
def newAccount(name, balance, password):
    global accountsList
    accountDict = {'name': name, 'balance': balance, 'password': password}
    accountsList.append(accountDict)
def show(accountNumber):
    global accountsList
    accountDict = accountsList[accountNumber]
    print(' Account', accountNumber)
    print('      Name:', accountDict['name'])
    print('      Balance:', accountDict['balance'])
    print('      Password:', accountDict['password'])
    print()
def getBalance(accountNumber, password):
    global accountsList
    accountDict = accountsList[accountNumber]
    if password != accountDict['password']:
        print('Incorrect password')
        return None
    return accountDict['balance']
def deposit(accountNumber, depositAmount, password):
    global accountsList
    accountDict = accountsList[accountNumber]
    if depositAmount < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountDict['password']:
        print('Incorrect password')
        return None
    accountDict['balance'] += depositAmount
    return accountDict['balance']
def withdraw(accountNumber, withdrawAmount, password):
    global accountsList
    accountDict = accountsList[accountNumber]
    if withdrawAmount < 0:
        print('You cannot withdraw a negative amount!')
        return None
    if withdrawAmount > accountDict['balance']:
        print('Insufficient funds for this withdrawal!')
        return None
    if password != accountDict['password']:
        print('Incorrect password')
        return None
    accountDict['balance'] -= withdrawAmount
    return accountDict['balance']

print('Joe, o número da sua conta é:', len(accountNamesList))
newAccount('Joe', 100, 's3cr3t')

print('Mary, o número da sua conta é:', len(accountNamesList))
newAccount('Mary', 50, 'p4ssw0rd')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower() # forçar tudo para minúsculas
    action = action[0] # usar apenas a primeira letra
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('You deposited:', userDepositAmount)
            print('Your new balance is:', newBalance)
    elif action == 'n':
        print('New Account:')
        name = input('Enter account name: ')
        balance = int(input('Enter initial balance: $'))
        password = input('Enter account password: ')
        newAccount(name, balance, password)
        accountNumber = len(accountsList) - 1
        print(f'Account {accountNumber} created successfully.')
    elif action == 's':
        print('Show:')
        for accountNumber in range(len(accountsList)):
            show(accountNumber)
    elif action == 'q':
        print('Thank you for using the bank. Goodbye!')
        break
    elif action == 'w':
        print('Withdraw:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('You withdrew:', userWithdrawAmount)
            print('Your new balance is:', newBalance)

""" Com essa abordagem, todos os dados associados a uma conta podem ser encontrados em um dicinário.
Para criar uma nova conta, nós construimos um dicionário e adicionamos em uma lista de contas. 
Esses tratamentos tornam a organização dos dados mais lógica, mas para cada função no programa ainda teremos que acessar 
a lista global de contas. Como veremos na próxima seção, conceder acesso a todos os dados da conta para as funções aumenta os riscos de segurança. Idealmente, cada função
 deveria poder afetar apenas os dados de uma única conta."""

 """" Problemas comuns em procedural implementations

 Os exemplos mostrados no capitulo compartilham um problema em comum: todos os dados
sobre os quais as funções operam são armazenados em uma ou mais variáveis ​​globais
Pelos
seguintes motivos, usar muitos dados globais com programação procedural é
uma má prática de programação:

1. Qualquer função que use e/ou mude dados globais podem ser mais complexas de usar em diferentes programas. Uma função que acessa dados globais está operando em dados que existem em um nível superior do código da própria função. 
Essa função precisara de um global statement para acessar esses dados. Você não pode simplesmente pegar uma função que depende de dados globais
e reutilizá-la em outro programa; ela só pode ser reutilizada em um programa
com dados globais semelhantes.

2. Muitos programas procedurais tendem a ter grandes coleções de variáveis ​​globais. Por definição, uma variável global pode ser usada ou alterada por qualquer trecho de código em qualquer lugar do programa. As atribuições a variáveis ​​globais são frequentemente dispersas por programas procedurais, tanto no código principal quanto dentro de funções. Como os valores das variáveis ​​podem mudar em qualquer lugar, pode ser extremamente difícil depurar e manter programas escritos dessa maneira.

3. Funções escritas para usar dados globais frequentemente têm acesso a dados em excesso.

Quando uma função usa uma lista global, um dicionário ou qualquer outra estrutura de dados global, ela tem acesso a todos os dados dessa estrutura. No entanto, normalmente a função deve operar apenas em uma parte (ou apenas uma pequena quantidade) desses dados. Ter a capacidade de ler e modificar quaisquer dados em uma grande estrutura de dados pode levar a erros, 
como usar ou sobrescrever acidentalmente dados que a função não deveria acessar."""

""" Orientação a Objetos para Resolver Problemas de Procedural Coding - Uma primeira olhada em uma Classe

Uma abordagem orientada a objetos combina todos os códigos e associa dados a uma única conta. Mas note que agora temos uma 
combinação de código e dados em um único logal (chamado classe). Vamos dar uma primeira olhada."""

class Conta():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def show(self):
        print('      Name:', self.name)
        print('      Balance:', self.balance)
        print('      Password:', self.password)
        print()

    def getBalance(self, password):
        if password != self.password:
            print('Incorrect password')
            return None
        return self.balance

    def deposit(self, depositAmount, password):
        if depositAmount < 0:
            print('You cannot deposit a negative amount!')
            return None
        if password != self.password:
            print('Incorrect password')
            return None
        self.balance += depositAmount
        return self.balance

    def withdraw(self, withdrawAmount, password):
        if withdrawAmount < 0:
            print('You cannot withdraw a negative amount!')
            return None
        if withdrawAmount > self.balance:
            print('Insufficient funds for this withdrawal!')
            return None
        if password != self.password:
            print('Incorrect password')
            return None