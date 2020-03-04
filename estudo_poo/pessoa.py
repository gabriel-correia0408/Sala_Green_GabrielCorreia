#criando uma classe "Pessoa", que posteriormente será importada ,no
#arquivo "main"

#aonde tem o if deve ser usado soemnte o retun e msg que está escrita
#pois deve haver um método #get para os outros métoods que vão conter ações ou valores

class Pessoa:
    #cridndo método connstrutor,e passando parametros para ele e utilizando o "self"
    #para poder charmar essas variaveis que contém os valores ,dentro de outros
    #métodos dentro dentro dessa classe.
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    #criando o método comer,que tem o,self,por convenção para fazer a ligação
    #passando o parametro "alimento",que recebera o nome de uma comida
    #esse parametro "alimento",receberá um valor no arquivo "main".
    #lembrando que aonde contém o print deve ser  um return,para poder ver
    #a msg deve ter um método get, que será criado.
    def comer(self,alimento):
        if self.comendo:
            return f'{self.nome} já está comendo'


        self.comendo = True
        return (f'{self.nome} está comendo {alimento}')






