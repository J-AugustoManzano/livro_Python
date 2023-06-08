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

listaPessoa.append(Pessoa("João", 23))
listaPessoa.append(Pessoa("Carla", 32))
listaPessoa.append(Pessoa("Antônio", 23))
listaPessoa.append(Pessoa("Pedro", 35))
listaPessoa.append(Pessoa("Marisa", 43))
listaPessoa.append(Pessoa("Silvio", 35))
listaPessoa.append(Pessoa("Juliana", 23))
listaPessoa.append(Pessoa("Silvia", 35))
listaPessoa.append(Pessoa("Esmeralda", 31))
listaPessoa.append(Pessoa("Alfonso", 35))

listaPessoa.sort(key=operator.attrgetter("nome"), reverse=True)

for registro in listaPessoa:
    print(registro.nome + " tem " + str(registro.idade) + " anos de idade.")

enter = input("\nPressione <Enter> para encerrar... ")
