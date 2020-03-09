#crie uma class Pessoa com:
#    3 atributos
#    7 métodos

from Aula1_maykon.classe_endereco import Endereco

#c
class Pessoa:
    def __init__(self,nome,idade,sexo,endereco:Endereco):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        #composição por que estou recebendo o objeto de uma classe dentro de outra
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return  self.__idade

    def get_sexo(self):
        return  self.__sexo

    def get_endereco(self):
        return self.__endereco

    def set_nome(self,nome):
        self.__nome = nome

    def set_idade(self,idade):
        self.__idade = idade

    def set_sexo(self,sexo):
        self.__sexo = sexo

    def set_endereco(self,endereco):
        self.__endereco = endereco

#a = Pessoa('LOLO',15,'MKMK')
#a.set_nome('Gabriel')
#a.set_idade(20)
#a.set_sexo('M')
#a.get_nome()