
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
    
    @property
    def lista_de_contas(self):
        return self._contas
    
    def listar_contas_cliente(self):
        for conta in self._contas:
            print(conta)