LIMITE_VALOR_SAQUE = 500.00
LIMITE_QTD_SAQUE = 3
Saldo = 0.00
contador = 0
contador_conta = 0
Extrato = ""
lista_clientes=[]
menu = """ 
    ..........MENU..........
    
    Digite S para Sacar
    Digite D para Depósito
    Digite E para Extrato
    Digite Q para Sair
    
    .........................
    
    -> """

def saque(Saldo, valor_saque, Extrato, numero_limite_saques, valor_limite_saque):
    global contador
    
    if(valor_saque < 0):
        print("Valor de saque inválido!")
    else: 
        if(valor_saque > Saldo):
            print("Saldo insuficiente")
        elif(valor_saque > valor_limite_saque):
            print("Você atingiu o valor limite de saque diário!")
        elif(contador >= numero_limite_saques):
            print("Você atingiu a quantidade limite de saques diários!")
        else:
            contador += 1
            saldo_final_saque = Saldo - valor_saque
            Saldo = saldo_final_saque
            Extrato += f"Valor saque: R${valor_saque: .2f}\n"
    return Saldo, Extrato

def deposito(Saldo, valor_deposito, Extrato):
    if(valor_deposito < 0):
        print("Valor inválido!")
    else:
        Saldo_final_deposito = valor_deposito + Saldo 
        Saldo = Saldo_final_deposito
        Extrato += f"Valor depósito: R${valor_deposito: .2f}\n"
    return Saldo, Extrato

def exibir_extrato(Saldo, Extrato = Extrato):
    print(f"""
..........EXTRATO..........""")
    
    if(Extrato != ""):
        print(Extrato)
    else:
        print("Não foram realizadas movimentações.")
    
    print(f"""
Saldo atual: R$ {Saldo:.2f}
        
.............................
            """)
    return Saldo, Extrato

def cadastro_cliente(nome, data_nascimento, cpf, logradouro, numero, bairro, cidade_estado):
    clientes = {}
    clientes["Nome"] = nome
    clientes["Data de nascimento"] = data_nascimento
    clientes["CPF"] = cpf
    clientes["Endereço"] = {}
    clientes["Endereço"]["Logradouro"] = logradouro
    clientes["Endereço"]["Nº"] = numero
    clientes["Endereço"]["Bairro"] = bairro
    clientes["Endereço"]["Cidade/Estado"] = cidade_estado
    return clientes

def cadastro_conta(clientes, cpf):
    global contador_conta
    conta = {}
    for cliente in clientes:
        if (cliente["CPF"] == cpf):
            conta["CPF"] = cpf
            conta["Nome"] = cliente["Nome"]
            contador_conta += 1
            conta["Numero da Conta"] = contador_conta
            conta["Agência"] = "0001"
            return conta
    return print("Cliente não cadastrado")

lista_clientes.append(cadastro_cliente("Carol", "16/12/87", "01", "Rua 01", "01", "Jardim 01", "Araraquara/SP"))
lista_clientes.append(cadastro_cliente("Michelle", "16/11/1987", "02", "Rua 02", "02", "Jardim 02", "Araraquara/SP"))
lista_clientes.append(cadastro_cliente("Ray", "18/12/1997", "03", "Rua 03", "03", "Jardim 03", "Araraquara/SP"))

cadastro_conta(lista_clientes, "01")
cadastro_conta(lista_clientes, "02")
cadastro_conta(lista_clientes, "03")
cadastro_conta(lista_clientes, "04")

while True: 

    Operacao = input(menu)
    Operacao = Operacao.upper()
    
    if(Operacao == "S"):
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        Saldo, Extrato = saque(Saldo = Saldo, Extrato = Extrato, valor_saque = valor_saque, numero_limite_saques = LIMITE_QTD_SAQUE, valor_limite_saque = LIMITE_VALOR_SAQUE)
     
    elif(Operacao == "E"):
        exibir_extrato(Saldo, Extrato = Extrato)

    elif(Operacao == "D"):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        Saldo, Extrato = deposito(Saldo, valor_deposito, Extrato)
        
    elif(Operacao == "Q"):
        print("Obrigada por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida")
