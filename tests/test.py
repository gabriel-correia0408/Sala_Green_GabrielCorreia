# O unittest é um framework padrão do python que nos auxilia nos testes unitários,
# para utilizar suas funcionalidades, devemos criar uma pasta com o nome tests,
# dentro dela devemos criar arquivos python onde iremos escrever os nossos testes.
# cada teste unitário será realizado por um método e deverá iniciar seu nome com
# test_ para ser encontrado pelo unittest e executado.

####### exemplos de métodos usaremos unitesttest ############

#criando método,"soma" para ser usado como exemplo,sendo passado para esse méetodo
#dois parametros o "x" eo "y"
def soma(x,y):
    # usando o return para reotrnar a variavel "resultado soma" que contém o resultado
    #da equação de x + y
    return  resultado_soma = x + y

#mesmo padrão do código acima diferença que a equação é de subtração ao invés de ser de
#soma
def subtracao(x,y):
    return reultado_subtracao = x - y
#crianddo classe "carro"
class carro:
    #criando método construtor "__init__" e passando dois parametros "marca,modelo"
    def __init__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca



