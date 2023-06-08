class TipoExemploPrivado():

    __nome = "" # campo privado

    def poeNome(self, nome): # método setter
        self.nome = nome

    def pegNome(self): # método getter
        return nome

produto = TipoExemploPrivado()

# Rotina para a entrada de dados

nome = input("Informe o nome do produto ..: ")
produto.poeNome(nome)

print("Produto informado ..........: {0}".format(produto.pegNome()))

enter = input("\nPressione <Enter> para encerrar... ")
