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
# sugestao de retorno: saldo e extrato

def saque(valor_saque, numero_limite_saques, valor_limite_saque):
    global Saldo
    global contador
    global Extrato
    
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
            print(Saldo)
            print(Extrato)
    return Saldo, Extrato

# deposito: positional only - sugestao de argumentos: saldo, valor, extrato
# sugestao de retorno: saldo e extrato

def deposito(valor_deposito):
    global Saldo
    global Extrato
    if(valor_deposito < 0):
        print("Valor inválido!")
    else:
        Saldo_final_deposito = valor_deposito + Saldo 
        Saldo = Saldo_final_deposito
        Extrato += f"Valor depósito: R${valor_deposito: .2f}\n"
        print(Extrato)
        print(Saldo)
    return Saldo, Extrato

# extrato: positional only e keyword only. Argumento posicional: saldo. Argumento nomeado: extrato

def exibir_extrato():
    global Saldo
    global Extrato
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

# criar funcao cadastrar cliente: armazenar em lista. Cliente e composto por: nome, data de nascimento, CPF e endereco
# o endereco e uma string com o formato: logradouro, numero, bairro, cidade/sigla estado

def cadastro_cliente(nome, data_nascimento, cpf, logradouro, numero, bairro, cidade_estado):
    dados_clientes=[]
    clientes = {}
    dados_clientes = [clientes]
    clientes["Nome"] = nome
    clientes["Data de nascimento"] = data_nascimento
    clientes["CPF"] = cpf
    clientes["Endereço"] = {}
    clientes["Endereço"]["Logradouro"] = logradouro
    clientes["Endereço"]["Nº"] = numero
    clientes["Endereço"]["Bairro"] = bairro
    clientes["Endereço"]["Cidade/Estado"] = cidade_estado
    
    print(dados_clientes)
    return dados_clientes

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

cadastro_cliente("Carol", "16/12/1987", "23075043893", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")
#cadastro_cliente("jessica", "16/12/1987", "23075043894", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")
#cadastro_cliente("michelle", "16/12/1987", "23075043895", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")
#cadastro_cliente("ray", "16/12/1987", "23075043896", "Avenida Uchoa", "393", "Vila Xavier", "Araraquara/SP")

#print(list(cadastro_cliente))

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
        
        cadastro_cliente(nome, data_nascimento, cpf, logradouro, numero, bairro, cidade_estado)
    
    if(Operacao == "S"):
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        saque(valor_saque = valor_saque, numero_limite_saques = LIMITE_QTD_SAQUE, valor_limite_saque = LIMITE_VALOR_SAQUE)
     
    elif(Operacao == "E"):
        exibir_extrato()

    elif(Operacao == "D"):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        deposito(valor_deposito)
        
    elif(Operacao == "Q"):
        print("Obrigada por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida")



