#criando classe endereco,com 3 atributos e 7 métodos
class Endereco:

    #criando método construtor "__init__"e passando os métodos que devem receber os
    #dados

    def __init__(self, cidade:str, rua:str, numero:str) -> None:
        #criando as variaveis com valore padroes,para independente do dado que entrar
        # a variavél seja,criada,mesmo que não passe pelas verificações abaixo
        #lembrando que pelas anderlines, as variaveis estão privadas.
        self.__cidade = ''
        self.__rua = ''
        self.__numero = 0

        # se p tipo "type" da varivél "nome" for igual a "str"
        #a varivél da classe "self.__cidade", vai receber o valor da variavél
        # do "cidade"  do método construtor "__init__"
        if type(cidade) == str:
            self.__cidade = cidade

        #mesma lógica do código acima única diferença que muda o a varivél
        # aora avariável é a "rua"
        if type(rua) == str:
            self.__rua  = rua

        # mesma lógica de verificação dos códigos acima.
        if type(numero) == int and numero > 0:
            self.__numero = numero

    def get_cidade(self):
        return self.cidade

    def get_rua(self):
        return self.rua

    def get_numero(self):
        return self.numero

    def set_cidade(self, cidade):
        self.cidade = cidade

    def set_rua(self,rua):
        self.rua = rua

    def set_numero(self,numero):
        self.__numero = numero

    def verifica_cidade(self,cidade) -> bool:
        if type(cidade) == str:
            self.__cidade = cidade

    def verefica_rua(self,rua) -> str:
        if type(rua) == str:
            self.__rua = rua

    def verefica_numero(self,numero) -> int:
        if type(numero) == int:
            self.__numero = numero


