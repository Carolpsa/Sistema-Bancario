from abc import ABC, abstractmethod

AGENCIA = "001"

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()
        self._saldo = 0
        self._agencia = AGENCIA
    
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
            return False
        elif valor < 0:
            print("Valor inválido")
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
        saldo = 0
        agencia = AGENCIA
        historico = Historico()
        return cls(numero, cliente)

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self._limite = 500.00
        self._limite_saques = 3
        self.contador_saques = 1
    
    @property
    def historico(self):
        return self._historico

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente        

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
        agencia = AGENCIA
        historico = Historico()
        limite = 500.00
        limite_saques = 3
        return cls(numero, cliente)

class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor    
    
    def registrar(self, conta):
        return conta.depositar(self._valor)
        
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        return conta.sacar(self._valor)

    @property
    def valor(self):
        return self._valor 

class Historico:
    def __init__(self):
        self.lista_historico = []
    
    def adicionar_transacao(self, transacao):
        self.lista_historico.append(f"{transacao.__class__.__name__}: R$ {transacao.valor:.2f}")
        print(self.lista_historico)

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        if transacao.registrar(conta):
            conta.historico.adicionar_transacao(transacao)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf= cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


pessoa1 = PessoaFisica("Avenida 01", "01", "Carol", "16/12/1987")

conta1 = ContaCorrente.nova_conta(pessoa1, 1)
deposito1 = Deposito(1000)
pessoa1.realizar_transacao(conta1, deposito1)
saque1 = Saque(100)
pessoa1.realizar_transacao(conta1, saque1)

conta2 = ContaCorrente.nova_conta(pessoa1, 2)
deposito2 = Deposito(900)
pessoa1.realizar_transacao(conta2, deposito2)
saque2 = Saque(10)
pessoa1.realizar_transacao(conta2, saque2)
