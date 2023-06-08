class Pessoa():

    @property
    def nome(self): 
        return self._nome

    @nome.setter
    def nome(self, nome): 
        self._nome = nome

    def __init__(self, nome):
        self._nome = nome

    def profissao(self):
        return "Atividade profissional desconhecida."

class Medico(Pessoa):

    def profissao(self):
        return "Formação em medicina."

class Advogado(Pessoa):

    def profissao(self):
        return "Formação em advocacia."

profissional = Pessoa("Ninguém")

profis1 = Advogado("Marisa Monteiro")
profis2 = Medico("Carlos de Andrade")
profis3 = Pessoa("Joana Silva")

profissional = profis1
print(profissional.nome)
print(profissional.profissao())
print()

profissional = profis2
print(profissional.nome)
print(profissional.profissao())
print()

profissional = profis3
print(profissional.nome)
print(profissional.profissao())

enter = input("\nPressione <Enter> para encerrar... ")
