# O encapsulamentp é a proteção dos atributos ou métodos de uma classe , no python
#eles são definidos  no próprio nome do atributo ou método.
#atributos ou métodos iniciados porno máximo dois sublinhados ( __ ) e se quiser terminados
#por um sublinhado são privados as outras formas são públicas.
# Ou seja encapsulamento é um meio aonde o programador define que um objeto só pode
# ser acessado  por um método e classe predefinido por ele, e não público.

#######----------------------#################---------------------####################-------

#Exemplo
# No código baixo vemos que a variavél principal "dados"que recebe um dicionário
# está no método construtor "__init__", esta variavél "dados" por sua vez está sem
#o encapsulamento,portanto quando instanciada a classe, no objeto "vl", está por sua vez
#mostra as opções e tudo que contém dentro da classe "valores",mostrando métodos e variaveis
#mostrando assim o método "inserir", e também deixando fazer print da variavél "dados"
# através do vl. , assim que posto o ".", o próprio paycharm, mostra oque há dentro de "vl"
#ou melhor que há dentro da classe "valores", e que há o "dados".
#porém logo a baixo a uma cópia desse código com uma única alteração,este por sua vez
#trás em sua varivél dados dois anderlines antes "self__dados" oque cria um encapsulamento
#tanto que quando tentado fazer o print,o paycharm não mostra a varivél "__dados"
#como se não existisse dentro de "vl" nossa instânca da classe, e mesmo que colocado manualmente
# a linha de código igual ao primeiro código, anteraldo somente os dois anderlines, mesmo assim
#não ocorre o print, o que o termina nos mostra é um erro, este é de como , se a variavél
#não tivesse nada atribuido a ela.
#o único módo para poder ver oque na vrivél quando há os dois anderlines,seria
#criando um método dentro da classe que fizesse isso,e depois chamar ele para
#poder ver oque há dentro da variavél, sendo assim isso é um encapsulamento
class valores:
    def __init__(self):
        self.dados = {}

    def inserir(self, id, nome):
        if 'valores' not in self.dados:
            self.dados ['valores'] =  {id, nome}
        else:
            self.dados['valores'].update({id: nome})

vl = valores()
vl.inserir(20, 'GabrielCorreia')
print(vl.dados)



#class valores:
   # def __init__(self):
       # self.__dados = {}

    #def inserir(self, id, nome):
       # if 'valores' not in self.__dados:
           # self.__dados ['valores'] =  {id, nome}
       # else:
           # self.__dados['valores'].update({id: nome})

#vl = valores()
#vl.inserir(20, 'GabrielCorreia')
#print(vl.__dados)

