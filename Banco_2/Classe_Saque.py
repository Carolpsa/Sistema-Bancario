from Classe_Transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        return conta.sacar(self._valor)

    @property
    def valor(self):
        return self._valor 

    def __str__(self):
        return f"Saque: R$ {self._valor:.2f}"
