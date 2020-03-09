#unittest.mock é uma biblioteca para teste em Python. Que permite substituir partes
# do seu sistema em teste por
# objetos simulados e fazer afirmações sobre como elas foram usadas.

#unittest.mock fornece uma classe core Mock removendo a necessidade de criar uma série de stubs
# em tod o seu conjunto de testes.
# Depois de executar uma ação, você pode fazer afirmações sobre quais métodos / atributos foram usados
# e com quais argumentos foram chamados. Você também pode especificar valores de
# retorno e definir os atributos necessários da maneira normal.

#Adicionalmente, o mock fornece um decorador patch() que lida com os atributos
# do módulo de patch e do nível de classe no escopo de um teste,junto com sentinel para criar
# objetos únicos. Veja o guia rápido para alguns exemplos de como usar Mock, MagicMock e patch().

#Mock é muito fácil de usar e foi projetado para uso com unittest. O mock é baseado no padrão
# ‘ação -> asserção’ em vez de ‘gravar -> reproduzir’ usado por muitas estruturas de simulação.

#Existe um backport de unittest.mock para versões anteriores do Python, disponível como mock no PyPI.

#exemplo a baixo deve ser refeito contendo classe qu existem e devem serm importadas
from unittest.mock import MagicMock
thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')