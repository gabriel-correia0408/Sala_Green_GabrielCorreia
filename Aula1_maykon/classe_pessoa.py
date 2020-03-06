#crie uma class Pessoa com:
#    3 atributos
#    7 métodos

#c
class Pessoa:
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return  self.idade

    def get_sexo(self):
        return  self.sexo

    def set_nome(self,nome):
        self.nome = nome

    def set_idade(self,idade):
        self.idade = idade

    def set_sexo(self,sexo):
        self.sexo = sexo
