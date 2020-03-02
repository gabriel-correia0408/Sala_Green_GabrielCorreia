# A composição bascamente é uma boa escolha quando se trata
# de um objeto que está dentro de outro de outro ou deve estar
#por exemplo quando uma classe mais simples "A" está dentro de
#uma classe mais complexa "b"

#
class Aluno:
    def __init__(self, nome):
        self.__nome = nome

    def retornaNome(self):
        return self.__nome


class Escola:
    aluno = []

    def __init__(self):
        print("Colégio em funcionamento em funcionamento")

        while True:
            print("1. matricular")
            print("2. Exibir lista de alunos")
            al = int(input())

            if al == 1:
                self.matricular()
            elif al == 2:
                self.exibir()
            else:
                print("Opçao invalida")

    def matricular(self):
        nome = input("Nome: ")
        self.aluno.append(Aluno(nome))

    def exibir(self):
        for alun in self.aluno:
            print(alun.retornaNome())


Escola()


