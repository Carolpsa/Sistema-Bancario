from abc import ABC, abstractmethod

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
        cliente = cliente
        numero = cls.contador_conta
        saldo = 0
        agencia = AGENCIA
        historico = Historico()
        return cls(numero, cliente)

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
            print("Operação não realizada. Valor inválido!")
            return False
        elif valor > self._limite:
            print("Operação não realizada. Valor de saque acima do limite!")
            return False
        elif self.contador_saques > self._limite_saques:
            print("Operação não realizada. Número de saques acima do permitido!")
            return False
        else:
            self.contador_saques += 1
            self._saldo -= valor
            return True

    @classmethod
    def nova_conta(cls, cliente):
        cliente = cliente
        numero = cls.contador_conta 
        saldo = 0
        agencia = AGENCIA
        historico = Historico()
        limite = 500.00
        limite_saques = 3
        return cls(cliente)
    
    def __str__(self):
        return f"""
        Agência: {self.agencia}
        C/C: {self.numero}
        Titular: {self.cliente.nome}
        """

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
    
    def extrato(self, conta):
        if not conta.historico.lista_historico:
            print("Não foram realizadas movimentações")
        for item in conta.historico.lista_historico:
            print(item)
        print(f"Saldo: R$ {conta.saldo:.2f}")

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
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def nome(self):
        return self._nome
        
    @property
    def data_nascimento(self):
        return self._data_nascimento

    def __str__(self):
        return f"""
        Nome: {self.nome}
        CPF: {self.cpf}
        Endereco: {self.endereco}
        Data de nacimento: {self.data_nascimento}
        """

lista_clientes = []
lista_contas = []

def verifica_cpf(cpf, lista_clientes):
    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def verifica_conta(cliente, lista_contas):
    for conta in lista_contas:
        if conta.cliente == cliente:
            return conta
    return None

menu = """ 
    ............MENU.............
    
    Digite S para Sacar
    Digite D para Depósito
    Digite E para Extrato
    Digite C para Cadastrar Cliente
    Digite O para Cadastrar Conta
    Digite Q para Sair
    
    .................................
    
    -> """

while True:
    Opcao = input(menu).upper()

    if(Opcao == "C"):
        cpf = input("Digite o CPF: ")
        if verifica_cpf(cpf, lista_clientes):
            print("Cliente já cadastrado!")
        else:
            nome = input("Digite o nome: ")
            data_nascimento = input("Digite a data de nascimento: ")
            endereco = input("Digite o endereço: ")
            pessoa = PessoaFisica(endereco, cpf, nome, data_nascimento)
            lista_clientes.append(pessoa)
            print("Cliente cadastrado com sucesso!")
        
    elif(Opcao == "O"):
        cpf = input("Digite o CPF: ")
        if verifica_cpf(cpf, lista_clientes):
            pessoa = verifica_cpf(cpf, lista_clientes)
            conta = ContaCorrente.nova_conta(pessoa)
            pessoa.adicionar_conta(conta)
            lista_contas.append(conta)
            print("Conta cadastrada com sucesso!")
        else:
            print("Cliente não cadastrado!")

    elif(Opcao == "S"):
        cpf = input("Digite o CPF: ")
        if verifica_cpf(cpf, lista_clientes):
            pessoa = verifica_cpf(cpf, lista_clientes)
            if verifica_conta(pessoa, lista_contas):
                conta = verifica_conta(pessoa, lista_contas)
                valor_saque = float(input("Digite o valor de saque: "))
                saque = Saque(valor_saque)
                pessoa.realizar_transacao(conta, saque)
            else:
                print("Conta não cadastrada!")
        else:
            print("Cliente não cadastrado!")

    elif(Opcao == "D"):
        cpf = input("Digite o CPF: ")
        if verifica_cpf(cpf, lista_clientes):
            pessoa = verifica_cpf(cpf, lista_clientes)
            if verifica_conta(pessoa, lista_contas):
                conta = verifica_conta(pessoa, lista_contas)
                valor_deposito = float(input("Digite o valor do depósito: "))
                deposito = Deposito(valor_deposito)
                pessoa.realizar_transacao(conta, deposito)
            else:
                print("Conta não cadastrada!")
        else:
            print("Cliente não cadastrado!")
            
    elif(Opcao == "E"):
        cpf = input("Digite o CPF: ")
        if verifica_cpf(cpf, lista_clientes):
            pessoa = verifica_cpf(cpf, lista_clientes)
            if verifica_conta(pessoa, lista_contas):
                conta = verifica_conta(pessoa, lista_contas)
                conta.historico.extrato(conta)
            else:
                print("Conta não cadastrada!")
        else:
            print("Cliente não cadastrado!")
        
    elif(Opcao == "Q"):
        print("Obrigada por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida")
