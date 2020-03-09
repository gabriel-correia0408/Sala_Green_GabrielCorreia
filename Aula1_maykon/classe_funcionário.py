from Aula1_maykon.classe_pessoa import Pessoa

#criando um classe "funcionário"
class Funcionario(Pessoa):
    #criando método construtor "__init__"
    def __init__(self,nome,idade,sexo,cargo,endereco,registro):
        self.__numero_registro = registro
        self.__cargo = cargo
        super().__init__(nome,idade,sexo,endereco)

    def get_registro(self)-> int:
        return  self.__numero_registro

    def get_cargo(self) -> str:
        return  self.__cargo

    def set_registro(self,numero_registro)-> None:
        self.__numero_registro = numero_registro

    def set_cargo(self,cargo) -> None:
        self.__cargo = cargo


#a = Funcionario('maria',30,'f','eng',201)
#a.set_nome('GABRIEL')
#print(a.get_nome())
