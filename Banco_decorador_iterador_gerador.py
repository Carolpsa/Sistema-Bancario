from abc import ABC, abstractmethod
from datetime import datetime
import pytz

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

    def __str__(self):
        return f"Deposito: R$ {self._valor:.2f}"

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

class Historico:
    def __init__(self):
        self.lista_historico = []
    
    def adicionar_transacao(self, transacao):
        self.lista_historico.append(transacao)
    
    def gerar_extrato(self, conta):
        if not conta.historico.lista_historico:
            return print("Não foram realizadas movimentações")
        for item in conta.historico.lista_historico:
            yield item

    def imprimir_extrato(self, lista, conta):
        for item in lista:
            print(item)
        print(f"Saldo: R$ {conta.saldo:.2f}")

    def gerar_relatorio(self, conta):
        if not conta.historico.lista_historico:
            return print("Não foram realizadas movimentações")
        escolha = input("""
        Selecione a opção desejada:
        S - Listar todos os saques
        D - Listar todos os depósitos
        T - Listar todas as transações 
        --> """).upper()
        if escolha == "S":
            lista_saques = [saques for saques in conta.historico.lista_historico if saques.__class__.__name__ == "Saque"]
            if lista_saques:
                for item in lista_saques:
                    yield item
            else:
                print("Não foram realizados saques!")
        elif escolha == "D":
            lista_depositos = [depositos for depositos in conta.historico.lista_historico if depositos.__class__.__name__ == "Deposito"]
            if lista_depositos:
                for item in lista_depositos:
                    yield item
            else:
                print("Não foram realizados depositos!")
        elif escolha == "T":    
            for item in conta.historico.lista_historico:
                yield item

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

class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            return conta
        except IndexError:
            raise StopIteration


lista_clientes = []
lista_contas = []

menu = """ 
    ............MENU.............
    
    Digite S para Sacar
    Digite D para Depósito
    Digite E para Extrato
    Digite C para Cadastrar Cliente
    Digite O para Cadastrar Conta
    Digite R para Relatorio de Transações
    Digite I para Relatorio de Contas
    Digite Q para Sair
    
    .................................
    
    -> """

def decorador_log(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        log = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%d/%m/%y às %H:%M:%S")
        print(f"Operação {(funcao.__name__).upper()} realizada em {log}")
    return envelope

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

@decorador_log
def cadastrar_cliente():
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

@decorador_log 
def cadastrar_conta():
    cpf = input("Digite o CPF: ")
    if verifica_cpf(cpf, lista_clientes):
        pessoa = verifica_cpf(cpf, lista_clientes)
        conta = ContaCorrente.nova_conta(pessoa)
        pessoa.adicionar_conta(conta)
        lista_contas.append(conta)
        print("Conta cadastrada com sucesso!")
    else:
        print("Cliente não cadastrado!")       

@decorador_log
def saque():
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

@decorador_log
def deposito():
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

def extrato():
    cpf = input("Digite o CPF: ")
    if verifica_cpf(cpf, lista_clientes):
        pessoa = verifica_cpf(cpf, lista_clientes)
        if verifica_conta(pessoa, lista_contas):
            conta = verifica_conta(pessoa, lista_contas)
            transacoes = conta.historico.gerar_extrato(conta)
            conta.historico.imprimir_extrato(transacoes, conta)

        else:
            print("Conta não cadastrada!")
    else:
        print("Cliente não cadastrado!")

def relatorio():
    cpf = input("Digite o CPF: ")
    if verifica_cpf(cpf, lista_clientes):
        pessoa = verifica_cpf(cpf, lista_clientes)
        if verifica_conta(pessoa, lista_contas):
            conta = verifica_conta(pessoa, lista_contas)
            itens = conta.historico.gerar_relatorio(conta)
            for item in itens:
                print(item)
        else:
            print("Conta não cadastrada!")
    else:
        print("Cliente não cadastrado!")

while True:
    Opcao = input(menu).upper()

    if(Opcao == "C"):
        cadastrar_cliente()
        
    elif(Opcao == "O"):
        cadastrar_conta()

    elif(Opcao == "S"):
        saque()

    elif(Opcao == "D"):
        deposito()
            
    elif(Opcao == "E"):
        extrato()

    elif(Opcao == "R"):
        relatorio()

    elif(Opcao == "I"):
        for conta in ContaIterador(lista_contas):
            print(conta)

    elif(Opcao == "Q"):
        print("Obrigada por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida")