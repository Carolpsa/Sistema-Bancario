LIMITE_VALOR_SAQUE = 500.00
LIMITE_QTD_SAQUE = 3
saldo = 0.00
contador = 0
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

def saque(saldo, valor_saque, extrato, numero_limite_saques, valor_limite_saque, contador):
    if(valor_saque < 0):
        print("Valor de saque inválido!")
    else: 
        if(valor_saque > saldo):
            print("Saldo insuficiente")
        elif(valor_saque > valor_limite_saque):
            print("Você atingiu o valor limite de saque diário!")
        elif(contador >= numero_limite_saques):
            print("Você atingiu a quantidade limite de saques diários!")
        else:
            contador += 1
            saldo_final_saque = saldo - valor_saque
            saldo = saldo_final_saque
            extrato += f"Valor saque: R${valor_saque: .2f}\n"
    return saldo, extrato, contador

def deposito(saldo, valor_deposito, extrato):
    if(valor_deposito < 0):
        print("Valor inválido!")
    else:
        Saldo_final_deposito = valor_deposito + saldo 
        saldo = Saldo_final_deposito
        extrato += f"Valor depósito: R${valor_deposito: .2f}\n"
    return saldo, extrato

def exibir_extrato(saldo, extrato = extrato):
    print(f"""
..........EXTRATO..........""")
    
    if(extrato != ""):
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    
    print(f"""
Saldo atual: R$ {saldo:.2f}
        
.............................
            """)
    return saldo, extrato
    
def verifica_cpf(cpf, lista_clientes):
    for cliente in lista_clientes:
        if cliente["CPF"] == cpf:
            return None
    return lista_clientes
    
def cadastro_cliente(lista_clientes):
    cpf = input("Informe o CPF do cliente: ")
    resultado = verifica_cpf(cpf, lista_clientes)
    if resultado == None:
        return print("Cliente já cadastrado")
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Informe o endereço do cliente (logradouro, número - bairro - cidade/estado): ")
    clientes = {
        "CPF": cpf, 
        "Nome": nome,
        "Data de nascimento": data_nascimento,
        "Endereço": endereco
    }
    lista_clientes.append(clientes)
    return lista_clientes

def cadastro_conta(lista_clientes, contador_conta, lista_contas):
    cpf = input("Informe o CPF do cliente: ")
    resultado = verifica_cpf(cpf, lista_clientes)
    for cliente in lista_clientes:
        if resultado == None:
            contador_conta += 1
            conta = {
            "CPF": cpf,
            "Numero da Conta": contador_conta,
            "Agência": "0001"
            }
            lista_contas.append(conta)
            return contador_conta
    return print("Cliente nao cadastrado")

while True:
    Opcao = input(menu_cadastro).upper()

    if(Opcao == "C"):
        cadastro_cliente(lista_clientes)
        
    elif(Opcao == "IC"):
        print(lista_clientes)
    
    elif(Opcao == "IO"):
        print(lista_contas)
    
    elif(Opcao == "O"):
        contador_conta = cadastro_conta(lista_clientes, contador_conta, lista_contas)

    elif(Opcao == "M"):
        print("Cadastros finalizados!")
        break
    
    else:
        print("Opção inválida")

while True: 

    Operacao = input(menu_operacoes).upper()
    
    if(Operacao == "S"):
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        saldo, extrato, contador = saque(saldo = saldo, extrato = extrato, valor_saque = valor_saque, numero_limite_saques = LIMITE_QTD_SAQUE, valor_limite_saque = LIMITE_VALOR_SAQUE, contador = contador)
     
    elif(Operacao == "E"):
        exibir_extrato(saldo, extrato = extrato)

    elif(Operacao == "D"):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)
        
    elif(Operacao == "Q"):
        print("Obrigada por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida")
