import operator 

class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self): 
        return self.__nome

    @nome.setter
    def nome(self, nome): 
        self.__nome = nome

    @property
    def idade(self): 
        return self.__idade

    @idade.setter
    def idade(self, idade): 
        self.__idade = idade

listaPessoa = []

print("Relação classificada de pessoas\n")

for registro in range(10):
    nome = input("Entre o " + str(registro + 1) + "o. nome ...: ")
    idade = int(input("Entre a idade ......: "))
    listaPessoa.append(Pessoa(nome, idade))
    print()

listaPessoa.sort(key=operator.attrgetter("nome"))

for registro in listaPessoa:
    print(registro.nome + " tem " + str(registro.idade) + " anos de idade.")

enter = input("\nPressione <Enter> para encerrar... ")
