# A herença na programação visa fazer um reaproveitamento decódigo
#fazendo que uma classe "filha" herde os atributos de uma classe"mae"
# como no exemplo a baxo,ea função "seper()" serve para chmar ou fazer
#essa herença desses atributos da classe "mae",para a classe "filha".

class Mae():
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def Mostra(self):
        a = (F'O peso da mae é de {self.peso}, ea altura é de {self.altura}, e sua cor de cabelo é de {self.cabelo}')
        print(a)


class Filha(Mae):
    def __init__(self, peso, altura, cabelo):
        super().__init__(peso, altura)
        self.cabelo = cabelo
        #self.sexo = sexo

    def Mostra(self):
        C = (F'O peso da filha é de {self.peso}, ea altura é de {self.altura}, e sua cor de cabelo é de {self.cabelo}')
        print(C)

M = Mae(60,160,'PRETO')
M.Mostra()

#F = Filha(60, 1.60, 'PRETO','S')
#F.Mostra()