LIMITE_VALOR_SAQUE = 500.00
LIMITE_QTD_SAQUE = 3
Saldo = 0.00
contador = 0
Extrato = ""
menu = """ 
    ..........MENU..........
    
    Digite S para Sacar
    Digite D para Depósito
    Digite E para Extrato
    Digite Q para Sair
    Digite C para cadastrar
    
    .........................
    
    -> """

# saque: keyworld - sugestao de argumentos: saldo, valor, extrato, limite, numero_saques, limites_saques

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
    #dados_clientes=[]
    clientes = {}
    #dados_clientes = [clientes]
    clientes["Nome"] = nome
    clientes["Data de nascimento"] = data_nascimento
    clientes["CPF"] = cpf
    clientes["Endereço"] = {}
    clientes["Endereço"]["Logradouro"] = logradouro
    clientes["Endereço"]["Nº"] = numero
    clientes["Endereço"]["Bairro"] = bairro
    clientes["Endereço"]["Cidade/Estado"] = cidade_estado
    
    print(clientes)
    return clientes

# criar funcao de cadastrar conta corrente: armazenar em lista, A conta e composta por: agencia, numero da conta e usuario.
# Numero da conta e sequencial, comecando em 1
# Numero da agencia e fixo 0001
# usuario pode ter mais de uma conta, mas uma conta nao pode pertencer a mais de um usuario 

def cadastro_conta(clientes, cpf):
    global contador
    conta = {}
    for cliente in clientes:
        if (cliente["CPF"] == cpf):
            print("Cliente cadastrado")
            conta["CPF"] = cpf
            conta["Nome"] = cliente["Nome"]
            contador += 1
            conta["Numero da Conta"] = contador
            conta["Agência"] = "0001"
            print(conta)
        else:
            print("Cliente não cadastrado")
    return conta

# Dica: Para vincular um usuario a uma conta, filtre a lista de usuarios buscando o numero do CPF

# cliente_1 = cadastro_cliente("Carol", "16/12/1987", "23075043893", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")
# cliente_2 = cadastro_cliente("jessica", "16/12/1987", "23075043894", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")
# cliente_3 = cadastro_cliente("michelle", "16/12/1987", "23075043895", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")
# cliente_4 = cadastro_cliente("ray", "16/12/1987", "23075043896", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")


#cadastro_conta(lista_clientes,"23075043893")

while True: 

    Operacao = input(menu)
    Operacao = Operacao.upper()
    
    if(Operacao == "C"):
        nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento: ")
        cpf = input("Digite o cpf: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o numero: ")
        bairro = input("Digite o bairro: ")
        cidade_estado = input("Digite cidade_estado: ")
        
        lista_cliente = []

        teste = cadastro_cliente(nome, data_nascimento, cpf, logradouro, numero, bairro, cidade_estado)

        lista_cliente.append(teste)

        print(lista_cliente)
    
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
