# Métodos são sub-rotinas,associadas a um objeto que possui acesso a seus dados. Os métodos determinam
# o comportamento dos objetos de uma classe métodos são "formas"moldes que irão tratar
# objetos e seus respctivos valores e dados,retornando ou melhor executando a tarefa  que ele
# foi programado para fazer.Em exemlo simples pense em uma classe,ela contém quatro métodos
# , adição ,subtração,divisão e multiplicação, esses quatro métodos irão receber os mesmo os objetos
# porém cada um vai retornar ou executar de sua forma, trasendo assim cada um .um resultado,nos mostrando
# que métos são como moldes que iram tratar os objetos e seus respctivos valores.
#######---------------------------########---------------########--------------##########--------

#exemplo

num1 = 10
num2 = 5

def adicao(n1,n2):
    res = n1 + n2
    print(f'A soma entre {n1} e {n2} da um total de: {res}')

def subtracao(n1,n2):
    res = n1 - n2
    print(f'A subtração entre {n1} e {n2} da um total de: {res}')

def multilicacao(n1,n2):
    res = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} da um total de: {res}')

def divisao(n1,n2):
    res = n1 / n2
    print(f'A divisão entre {n1} e {n2} da um total de: {res}')

ad = adicao(num1,num2)
sub = subtracao(num1,num2)
mult = multilicacao(num1,num2)
div = divisao(num1,num2)