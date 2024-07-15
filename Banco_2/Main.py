from Classe_ContaCorrente import ContaCorrente
from Classe_PessoaFisica import PessoaFisica
from Classe_Deposito import Deposito
from Classe_Saque import Saque
from Classe_ContaIterador import ContaIterador
from datetime import datetime
import pytz

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
    Digite L para Listar Contas do Cliente
    Digite Q para Sair
    
    .................................
    
    -> """

def decorador_log(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        log = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%d/%m/%y às %H:%M:%S")
        print(f"Operação {(funcao.__name__).upper()} realizada em {log}")
    return envelope

def verificar_cpf(cpf, lista_clientes):
    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            return cliente

def verificar_conta(cliente, lista_contas):
    for conta in lista_contas:
        if conta.cliente == cliente:
            return conta

def selecionar_cliente_e_conta():
    cpf = input("Digite o CPF: ")
    pessoa = verificar_cpf(cpf, lista_clientes)
    if not pessoa:
        print("Cliente não cadastrado!")
    conta = verificar_conta(pessoa, lista_contas)
    if not conta:
        print("Conta não cadastrada!")
    return pessoa, conta

@decorador_log
def cadastrar_cliente():
    cpf = input("Digite o CPF: ")
    if verificar_cpf(cpf, lista_clientes):
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
    pessoa = verificar_cpf(cpf, lista_clientes)
    if pessoa:
        conta = ContaCorrente.nova_conta(pessoa)
        pessoa.adicionar_conta(conta)
        lista_contas.append(conta)
        print("Conta cadastrada com sucesso!")
    else:
        print("Cliente não cadastrado!")

@decorador_log
def saque():
    pessoa, conta = selecionar_cliente_e_conta()
    if pessoa and conta:
        valor_saque = float(input("Digite o valor de saque: "))
        saque = Saque(valor_saque)
        pessoa.realizar_transacao(conta, saque)

@decorador_log
def deposito():
    pessoa, conta = selecionar_cliente_e_conta()
    if pessoa and conta:
        valor_deposito = float(input("Digite o valor do depósito: "))
        deposito = Deposito(valor_deposito)
        pessoa.realizar_transacao(conta, deposito)

def extrato():
    pessoa, conta = selecionar_cliente_e_conta()
    if pessoa and conta:
        transacoes = conta.historico.gerar_extrato(conta)
        conta.historico.imprimir_extrato(transacoes, conta)

def relatorio():
    pessoa, conta = selecionar_cliente_e_conta()
    if pessoa and conta:
        itens = conta.historico.gerar_relatorio(conta)
        for item in itens:
            print(item)

def main():

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

if __name__ == "__main__":
    main()