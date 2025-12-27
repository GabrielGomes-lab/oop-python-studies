""" Gerenciando múltiplos objetos
Nossa classe de conta bancária precisará, no mínimo, de um nome, senha e saldo como dados. Para os comportamentos, o usuário deve ser capaz de criar uma conta, depositar e sacar dinheiro e verificar seu saldo.
Definiremos e inicializaremos as variáveis ​​para o nome, senha e saldo, e criaremos métodos para implementar cada uma das operações.
Assim, poderemos instanciar qualquer número de objetos Account. Como a classe inicial do Capítulo 1, esta é uma classe Account simplificada que usa apenas números inteiros para o saldo e mantém a senha em texto simples. Embora você não use simplificações como essas em um aplicativo bancário real, elas nos permitirão concentrar nos aspectos de POO envolvidos.

"""


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Senha incorreta. Depósito falhou.")
            return None
        
        if amountToDeposit <= 0:
            print("O valor do depósito deve ser positivo.")
            return None
        self.balance += self.balance + amountToDeposit
        return self.balance
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Senha incorreta. Saque falhou.")
            return None
        
        if amountToWithdraw <= 0:
            print("O valor do saque deve ser positivo.")
            return None
        
        if amountToWithdraw > self.balance:
            print("Saldo insuficiente para saque.")
            return None
        
        self.balance -= amountToWithdraw
        return self.balance
    def getBalance(self, password):
        if password != self.password:
            print("Senha incorreta. Não é possível obter o saldo.")
            return None
        return self.balance
    def show(self):
        print(f"Nome: {self.name}, Saldo: {self.balance}")

""" Note como os metodos manipualm os dados. Os dados são passados dentro de cada método através dos parametros, que são varivaveis locais qque apenas existem enquanto o método está sendo executado. 
 Primeiro, temos o método __init__() com três parametros: name, balance e password. Esses parâmetros são usados ​​para inicializar as variáveis ​​de instância correspondentes (self.name, self.balance e self.password).

 A instanciação se da seguinte forma:
    account1 = Account("Alice", 1000, "senha123")

Quando isntanciamos o objeto, os valores dos três argumentos são passados dentro do método __init__(),
o método deposit() permite ao usuário realizar um depósito na sua conta, depois de instanciar um objeto Account e salvar na variável account1, podemos chamar o método deposit() assim:
novosaldo = account1.deposit(500, "senha123")

Essa chamada diz pra depositarmos 500 reais e passamos a senha. Dentro do deposit() temos duas checagens, a primeira validação é se a senha que está sendo passada é a mesma que foi passada quando o objeto account1 foi criado, e o segundo é se o valor de depósito é negativo, em caso de ambos os testes passarem, é depositado o valor na conta. 

Temos o saque (withdraw()) que funciona de forma similar, com a diferença que além de validar a senha e o valor do saque, também valida se há saldo suficiente na conta para realizar o saque.

Para checar o saldo fazemos apenas a chamada:
saldoatual = account1.getBalance("senha123")
"""

""" Importando classes no código
Existem duas maneira para usar uma classe que nós construimos em nosso próprio codigo. A primeira é escrever toda a classe dentro do nosso código principal, 
mas isso faria com que o código ficasse grande e difícil de ler além de dificultar a reusabilidade.
A segunda maneira é salvar a classe em um arquivo separado e importá-la para o nosso código principal quando necessário. Para isso é necessário que o código da classe estja na mesma 
pasta que o nosso código principal ou em uma pasta que esteja no caminho de busca do interpretador Python.
Podemos editar para que haja interação entre o usuário e a classe.
"""

username = input('Qual o seu nome?')
balance = input('Qual o saldo inicial da sua conta?')
balance  = int(balance)
password = input('Defina uma senha para sua conta:')

account1 = Account(username, balance, password)


"""
A forma que estamos realizando pode ser melhorada se usarmos uma lista de contas, então podemos iniciar com uma lista vazia e adicionar um número variado de contas. 
Além disso, a melhor forma de interagir com essa lista é criando dicionários. Suponha que tenhamos na lista cinco contas, caso o usuário número dois queria fechar sua conta e reaizamos um 
pop() na lista, o usuário número três se tornaria o usuário número dois, o que pode causar confusão, além de dificultar a busca por uma conta específica fazendo com que o usuário
tenha que atualizar seu número de conta sempre. Com um dicionário, podemos usar o nome do usuário como chave e o objeto Account como valor, assim podemos buscar a conta diretamente pelo nome do usuário.
"""

accounts = {}
nexaccountnumber = 0
oAccount = Account(username, balance, password)
joesaccountnumber = nexaccountnumber
accounts[joesaccountnumber] = oAccount
nexaccountnumber += 1
print(f"Sua conta foi criada com o número {joesaccountnumber}")

""" Então iniciamos com um dicionário vazio chamado accounts, e iniciamos o número de contas em 0, toda vez que instanciamos uma nova conta, nós adicionamos uma nova 
entrada no dicionário de contas usando o valor de nexaccountnumber como chave e o objeto Account como valor. Depois incrementamos o número da próxima conta em 1.
e isso se tornará a chave para o próximo objeto Account que for instanciado."""

"""Construindo um menu interativo
Com nossa classe Account pronta e a estrutura de dados, vamos fazer um código principal interativo, perguntando ao usuário que operação ele gostaria de realizar"""

accountsDict = {}
nextAccountNumber = 0
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('*** Deposit ***')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)
    elif action == 'o':
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to use for this account? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Your new account number is:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()
    elif action == 's':
        print('Show:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print(' Account number:', userAccountNumber)
            oAccount.show()
    elif action == 'q':
     break
    elif action == 'w':
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input('Please enter the amount to withdraw: ')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)