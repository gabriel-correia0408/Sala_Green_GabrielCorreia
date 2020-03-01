#   Um objeto é uma referência a um local da memória que possui um valor.O OBJETO TAMBÉM é uma instância
# da classe,ou seja uma representação da classe.

#exemplo número 1
#criando uma primeira variavél de nome "num1",que ira armazenar um valor int que será o 10
num1 = 10

#criando uma segunda variavél de nome "num2",que ira armazenar um valor int que será o 20
num2 = 20

#criando uma tereceira variavél "calculo",que ira receber as duas variaveis anteriores,atraavés do "+",
#irá somar as duas.
calculo = num1 + num2
# o primeiro print mostra o valor do objeto que está contido na variavel "num1"
print(num1)
# o primeiro print mostra o valor do objeto que está contido na variavel "num2"
print(num2)
# o primeiro print mostra o valor do objeto que está contido na variavel "calculo"
print(calculo)

# sendo assim temos um objto na primeira variavél um na segunda, e na variavél "calculo"fazemos
#a soma dos dois objtos,criando um terceiro valor no caso terceiro objeto que ficraa contido na variavél
#"calculo"

#-----------------------------------------#########---------------------#######---------------

#exemplo número dois:
class Calculo:
    def soma(self,a,b):
        adicao = a + b
        print(f'A soma entre {a} e {b} da um total de: {adicao}')

  #  def subtracao(self):
     #   n1 - n2  = n3
      #  print(f'A subtração  entre {n1} e {n2} da um total de: {n3}')

#criando uma varivaél de nome "c" que ira receber a classe "Calculo"
c = Calculo()
#aqui fazemos uso do print, na ariavél "c" que por sua vez quando colocado o "." nos tras os métodos da classe
# ou seja a varivél "c" que se torna um objeto é uma instancia da classe
print(c.soma(10,5))


