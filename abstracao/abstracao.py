#revendo conceitos para trabalhar com listas

# Primeiro conceito a ser visto será p sort, aonde ele tem como objetivo
# a lista tando do menor para o maior, quanto o contrário do maior para
# o menor


# Criando uma lista para usar de exemplo,e adionando números randônicos, no caso os
# elementos da lista
lista_de_exemplo  = [52,36,1,25,2,58,14,3,89,4,456,9,500,7,65,8,210,10]
print(f'lista sem ser alterada: {lista_de_exemplo}\n')

# chamando a variavél lista_de_exemplo,que contém nossa lista
# e aplicando a função "sort",para organizar a lista do menor para o menor
lista_de_exemplo.sort()
print(f'lista já sendo alterada pela função sort \na alterando do menor para o maior {lista_de_exemplo}\n')
 # mais um avez chamando a variavél lista_de_exemplo,desta vez
 #para fazer o reverso ao invés de ordenarmos os elementos
 #do menor para o maior,vamos fazer do maior para o menor
lista_de_exemplo.sort(reverse=True)
print(f'lista alterada agora de forma contrária \ndo maior para o menor{lista_de_exemplo}')

