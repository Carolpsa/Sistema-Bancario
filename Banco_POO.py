from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor > self._saldo:
            return False
        elif valor < 0:
            return False
        else: 
            self._saldo -= valor
            return True

    def depositar(self, valor):
        if valor < 0:
            print("Valor invalido!")
            return False
        self._saldo += valor
        return True

    @classmethod
    def nova_conta(cls, cliente, numero):
        cliente = cliente
        numero = numero
        saldo = saldo
        agencia = agencia
        historico = historico
        return cls(saldo, numero, agencia, cliente, historico)

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques
        self.contador_saques = 1
        
    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
            return False
        elif valor < 0:
            print("Operacao nao realizada. Valor invalido!")
            return False
        elif valor > self._limite:
            print("Operacao nao realizada. Valor de saque acima do limite!")
            return False
        elif self.contador_saques > self._limite_saques:
            print("Operacao nao realizada. Numero de saques acima do permitido!")
            return False
        else:
            self.contador_saques += 1
            self._saldo -= valor
            return True

    @classmethod
    def nova_conta(cls, cliente, numero):
        cliente = cliente
        numero = numero
        saldo = 0
        agencia = agencia
        historico = historico
        limite = limite
        limite_saques = limite_saques
        return cls(saldo, numero, agencia, cliente, historico, limite, limite_saques)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            return f"Depósito no valor de: R${self._valor:.2f}" 

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        if conta.sacar(self._valor):
            return f"Saque no valor de {self._valor:.2f}"
            
class Historico:
    def __init__(self):
        self.lista_historico = []

    def adicionar_transacao(self, transacao):
        if transacao != None:
            self.lista_historico.append(transacao)
            return self.lista_historico
       
class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        if transacao != None:
            return print(transacao, f"\nSaldo: R$ {conta.saldo():.2f}")  
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self._cpf= cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

lista_contas1 = []
lista_contas2 = []
historico1 = Historico()
historico2 = Historico()

pessoa1 = PessoaFisica("Rua 01", lista_contas1, "01", "Carol", "16/12")
conta1 = ContaCorrente(0, 1, "0001", pessoa1, historico1, 500.00, 3)
pessoa1.adicionar_conta(conta1)
conta2 = ContaCorrente(0, 2, "0001", pessoa1, historico2, 500.00, 3)
pessoa1.adicionar_conta(conta2)

deposito1 = Deposito(1000)
transacao1 = deposito1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao1)
historico1.adicionar_transacao(transacao1)

saque1 = Saque(-200)
transacao2 = saque1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao2)
historico1.adicionar_transacao(transacao2)
    
saque1 = Saque(200)
transacao3 = saque1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao3)
historico1.adicionar_transacao(transacao3)

saque1 = Saque(200)
transacao4 = saque1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao4)
historico1.adicionar_transacao(transacao4)

saque1 = Saque(600)
transacao5 = saque1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao5)
historico1.adicionar_transacao(transacao5)

saque1 = Saque(10)
transacao6 = saque1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao6)
historico1.adicionar_transacao(transacao6)

deposito1 = Deposito(-1000)
transacao7 = deposito1.registrar(conta1)
pessoa1.realizar_transacao(conta1, transacao7)
historico1.adicionar_transacao(transacao7)