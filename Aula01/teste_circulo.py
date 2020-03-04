#criando teste para a classe "Circulo"

from Aula01.Exercicio03 import Circulo
cor = 'amarelo'
circulo = Circulo('azul',10,'papel')
raio = 10


print('TESTE get_Cor')
assert circulo.cor == circulo.get_Cor(), f'ERRO A cor : {cor} não está sendo passada para o objeto'
#assert cor == circulo.get_Cor() f'ERRO a cor: {cor} não está seno passada para o objto '
assert Circulo.cor == int(cor), f'ERRO a varivél cor: {cor} deve ser um string(letras)'
print('Teste get_Cor OK *-*\n')

print('TESTE trocar_Cor')
assert  Circulo.cor == circulo.trocar_Cor(), f'ERRO a cor{cor}, não está sendo passada'
assert Circulo.cor == int(cor), f'Erro a cor: {cor}, deve ser uma string(letras)'
print(('Teste trocar_Cor OK *-*\n'))

print('TESTE calculo_Area')
assert Circulo.raio == circulo.calculo_Area(), f'ERRO o raio{raio}, não esta sendo passdado para o objeto'
assert not  f'ERRO o raio: {raio},não pode ser um número negativo'


