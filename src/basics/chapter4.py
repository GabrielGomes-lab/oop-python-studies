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

""" Criando um gerenciador de objetos
    Um objeto que mantém uma lista ou dicionário de objetos gerenciados, e chama métodos desses objetos. 
Então vamos construir
"""

from Account import *

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you want to use for this account? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)

        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you.')
            # Remove user's account from the dictioary of accounts
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]        
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('   Account number:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)

    def bankInfo(self):
        print('Hours: 9 to 5')
        print('Address: 123 Main Street, Anytown, USA')
        print('Phone:  (650) 555-1212')
        print('We currently have', len(self.accountsDict), 'account(s) open.')


## Main code

# Main program for controlling a Bank made up of Accounts

# Bring in all the code of the Bank class
from Bank import *

# Create an instance of the Bank
oBank = Bank()

# Main code
# Create two test accounts
joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = oBank.createAccount('Mary', 12345, 'MarysPassword')
print("Mary's account number is:", marysAccountNumber)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter
    print()
    
    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'i':
        oBank.bankInfo()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action.  Please try again.')
        
print('Done')


"""Melhores maneiras de trabalhar com erros

No código acima, sempre que um erro ocorre, uma mensagem de erro é impressa na tela e o método retorna None. Embora isso funcione, não é a melhor maneira de lidar com erros em Python.

Podemos usar o try e except para capturar exceções e lidar com erros de forma mais elegante.

try:
    # código que pode gerar uma exceção
except SomeException as e:
    # código para lidar com a exceção
Se o código que está no bloco de try funcionar sem erros, não será necessário gerar uma excessão, mas se o código gerar uma exceção, o fluxo de execução será transferido para o bloco except, onde podemos lidar com o erro de forma apropriada.

exemplo:
age = input("Please enter your age: ")
try:
    age = int(age)
except ValueError:
    print("That's not a valid age. Please enter a number.")

The raise statement e Custom Exceptions
Se o seu código detectar uma condição de erro em tempo de execução, você pode usar a instrução raise para sinalizar uma exceção. Existem muitas formas de usar a instrução raise,
mas a abordagem padrão é usar esta sintaxe:

raise SomeException("Error message")

"""

# Account class
# Errors indicated by "raise" statements

# Define a custom exception
class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance
        
    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account')

        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Added for debugging
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)

# Bank that manages a dictionary of Account objects

from Account import *

class Bank():
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account ' + str(accountNumber))
        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    def askForValidPassword(self, oAccount):
        password = input('Please enter your password: ')
        oAccount.checkPasswordMatch(password)
    
    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is your name? ')
        userStartingAmount = input('How much money to start your account ? ')
        userPassword = input('What password would you like to use for this account? ')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        theBalance = oAccount.getBalance()
        print('You had', theBalance, 'in your account, which is being returned to you.')
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        oAccount = self.getUsersAccount()
        theBalance = oAccount.getBalance()
        print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')

    # Special method for Bank administrator only
    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account:', userAccountNumber)
            oAccount.show()
            print()

