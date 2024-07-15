from Classe_Transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor    
    
    def registrar(self, conta):
        return conta.depositar(self._valor)

    def __str__(self):
        return f"Deposito: R$ {self._valor:.2f}"
