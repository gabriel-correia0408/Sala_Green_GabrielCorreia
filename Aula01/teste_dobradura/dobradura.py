# DOBRADURA de Papel
#
# Uma professora de arte pediu um programa para clacular quanto poderia dividir um papel com
# uma quantidade de dobradura.
#
# Ela falou que com uma dobradura, poderia dividir o papel em 2 pedaços e com três dobraduras
# pode-se dividir o papel em 8 pedaços.
#
# Faça uma classe que:
# 1) calcule e retorne a quantidade de divisões do papel por uma quantidade de dobradura.
# 2) A quantidade de dobraduras não pode ser numero negativo e nem aceitar string. Caso seja colocado
#       numero negativo e caracteres a função deve retornar False
#
#
# Atenção!!!
# A estrutura do programa é a seguinte:
# 1) Nome da classe: Dobradura.
# 2) Nome do metodo: get_dobrar(self,numero_dobradura)
#
# Deve ser salvado com o nome do arquivo dobradura.py dentro da pasta teste_dobradura.
# Deve ser executado o arquivo teste_de_dobradura.py e o mesmo deve aparecer a mensagem 'Teste Conculido com Sucesso!'

#criando a classe
class Dobradura:

    def get_dobrar(self,numero_dobradura):
        self.numero_dobradura = numero_dobradura
        if self.numero_dobradura == self.numero_dobradura *-1:
            return False
        elif self.numero_dobradura == str(self.numero_dobradura):
            return False
        else:
            dobradura = 2
            folha = dobradura
            calculo = folha**self.numero_dobradura
        return calculo

       # while count(self.numero_dobradura) <= expoente_dobradura:
            #for i in base_folha:
                #a = (i ** 2)
            #else:
                #'false'

if __name__ == '__main__':
    a = Dobradura()
a = Dobradura()
print(a.get_dobrar(13))











