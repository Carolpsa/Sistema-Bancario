from Classe_Historico import Historico

AGENCIA = "001"

class Conta:
    contador_conta = 0
    
    def __init__(self, cliente):
        Conta.contador_conta +=1
        self._numero = Conta.contador_conta
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
    def nova_conta(cls, cliente):
        return cls(cliente)