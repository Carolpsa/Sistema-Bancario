from abc import ABC, abstractmethod

LIMITE_VALOR_SAQUE = 500.00
LIMITE_QTD_SAQUE = 3
contador_conta = 0
extrato = ""
lista_clientes=[]
lista_contas=[]
menu_operacoes = """ 
    ..........MENU.OPERAÇÕES..........
    
    Digite S para Sacar
    Digite D para Depósito
    Digite E para Extrato
    Digite Q para Sair
    
    .................................
    
    -> """

menu_cadastro = """ 
    ..........Menu.de.Cadastro..........
    
    Digite C para Cadastrar Cliente
    Digite O para Cadastrar Conta
    Digite IC para Visualizar a Lista de Clientes
    Digite IO para Visualizar a Lista de Contas
    Digite M para Menu de Operacoes
    
    ...................................
    
    -> """

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
            return False
        self._saldo += valor
        return True

    @classmethod
    def nova_conta(cls, cliente, numero):
        saldo = 0
        numero += 1
        agencia = "0001"
        cliente = "cliente"
        historico = "historico"
        return cls(saldo, numero, agencia, cliente, historico)

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques
        self.contador = 0
        
    def sacar(self, valor):
        if valor > self._saldo:
            return False
        elif valor < 0:
            return False
        elif valor > self._limite:
            return False
        elif self.contador >= self._limite_saques:
            return False
        else:
            self.contador += 1
            self._saldo -= valor
            return True

class Historico:
    def __init__(self):
        pass

    def adicionar_transacao(self, transacao):
        pass


class Transacao(ABC):
    @abstractmethod
    def registrar(conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(conta):
        pass


class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        self.conta = conta
        self.transacao = transacao

    def adicionar_conta(self, conta):
        self.conta = conta


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas, cpf, nome, data_nascimento)
        self._cpf= cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def adicionar_conta(self, conta):
        self.conta = conta

conta1 = ContaCorrente(0.00, 1, "0001", "cliente", "historico", 500.00, 3)
print(conta1._saldo)
print(conta1.depositar(1000.00))
print(conta1.sacar(100.00))
print(conta1._saldo)
print(conta1.sacar(100.00))
print(conta1.sacar(100.00))
print(conta1.sacar(100.00))
