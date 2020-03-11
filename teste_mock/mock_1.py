# o assert serve para fazer uma assertativa,ou seja se o valor for verdadeiro(True),
# o programa quando executo não ira mostrar erro,caso contrário,ira aparecer "AssertionError"
assert True
#na linha abaixo estou dizendo que 120 é igual há 120,isso é uma verdade(True) ou seja
#não ira apresenta nenhum erro no terminal quando for executado essas linhass de códigos
assert 120 == 120
#abaixo digo que 16 é maior que 15,isso também é uma verdade ou seja também,não ira apresentar
#nenhum erro no terminal
assert 16 > 15
#abaixo também é uma afirmativa verdadeira,como dito antes quando executado não irá apresentar
#nenhum erro no terminal
assert 'teste' == 'teste'
# Executando o python no terminal, nenhum erro acontece, afirmando que todas as
# condições são verdadeiras.


#agora irei executar linhas de códigos que não são verdadeiras(false)
# 2 - assert com condição falsa
assert 3 == 5
assert 'Ronaldo' == 'Ronaldinho'
#assert False
# Executando o python no terminal, a primeira condição incorreta (assert 3 == 5)
# gera um erro, encerrando a execução.

# Resposta do terminal

###     assert 3 == 5
###     AssertionError

#mostrando assim que como deu erro na linha 19 o python nem seguiu o código
#pois na linha 20 também tem um erro ou melhor uma condição "false"