# Classe é uma estrutura que abstrai um conjuntos de objtos através de métodos
# e os estados possiveis destes objetos.
# Uma classe é como um template aonde organiza os métodos que iram tratar os
# objetos ou seja uma classe representa
# um conjunto de objeto com suas caracteristicas afins.

#Exemplo:
class Cadastro:
    lista = []
     def Nome_sobrenome(self):
         cad = str(input('Digite seu nome completo: '))
        return cad.appende


     def Cad_Idade(self):
         idade = int(input('Digite sua idade: '))
         print(f'{idade}')

     def Cad_Endereco(self):
         rua = str(input('Digite a rua de seu endereço: '))
         print(f'{rua}')

c = Cadastro()

print(c.Nome_sobrenome(), c.Cad_Endereco() ,c.Cad_Idade())


