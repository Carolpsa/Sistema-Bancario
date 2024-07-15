
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