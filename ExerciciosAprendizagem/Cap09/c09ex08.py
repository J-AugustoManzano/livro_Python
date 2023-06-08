class Pessoa():

    @property
    def nome(self): 
        return self._nome

    @nome.setter
    def nome(self, nome): 
        self._nome = nome

    @property
    def profissao(self): 
        return self._profissao

    @profissao.setter
    def profissao(self, profissao): 
        self._profissao = profissao

    def __init__(self, nome, profissao):
        self._nome = nome
        self._profissao = profissao.capitalize()

pessoa1 = Pessoa("José Carlos", "medicina")
pessoa2 = Pessoa("Marlene Oliveira", "matemática")
pessoa3 = Pessoa("Carla Abreu", "datiloscopista")

print("Nome .......: %s" % pessoa1.nome)
print("Profissão ..: %s" % pessoa1.profissao)
print()

print("Nome .......: %s" % pessoa2.nome)
print("Profissão ..: %s" % pessoa2.profissao)
print()

print("Nome .......: %s" % pessoa3.nome)
print("Profissão ..: %s" % pessoa3.profissao)

enter = input("\nPressione <Enter> para encerrar... ")
