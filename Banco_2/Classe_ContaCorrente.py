from Classe_Conta import Conta


class ContaCorrente(Conta):
    
    def __init__(self, cliente):
        super().__init__(cliente)
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
            print("Valor inválido!")
            return False
        elif valor > self._limite:
            print(f"Valor de saque acima do limite. O limite é de R$ {self._limite:.2f}")
            return False
        elif self.contador_saques > self._limite_saques:
            print(f"Número de saques acima do limite. O limite é de {self._limite_saques} saques")
            return False
        else:
            self.contador_saques += 1
            self._saldo -= valor
            return True

    @classmethod
    def nova_conta(cls, cliente):
        return cls(cliente)
    
    def __str__(self):
        return f"""
        Agência: {self.agencia}
        C/C: {self.numero}
        Titular: {self.cliente.nome}
        """