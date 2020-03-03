class Pessoa:
    # método construtor
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.endereco = Endereco()

    # método de set nome
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_sexo(self):
        return self.sexo

    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade
class Endereco:
    def __init__(self,cidade, bairro, rua, numero):
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

    def get_cidade(self):
        return self.cidade

    def set_cidade(self,cidade):
        self.cidae = cidade


    def get_bairro(self):
        return self.bairro

    def set_bairro(self,bairro):

    def get_rua(self):
        return self.rua

    def set_rua(self,rua):
        self.rua = rua

    def get_numero(self):
        return self.numero

    def set_numero(self,numero):
        self.numero = numero



class Engenheiro(Pessoa):
    def __init__(self,numero,especificacao,nome,sexo , idade):
        super().__init__(nome,sexo,idade)
        self.numero = numero
        self.especificacao = especificacao

    def get_numero(self):
        return  self.numero

    def set_numero(self,numero):
        self.numero = numero

    def get_especificacao(self):
        return self.especificacao

    def set_especificacao(self,especificacao):
        self.especificacao = especificacao
        










