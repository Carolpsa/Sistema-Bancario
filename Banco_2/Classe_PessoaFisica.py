from Classe_Cliente import Cliente

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