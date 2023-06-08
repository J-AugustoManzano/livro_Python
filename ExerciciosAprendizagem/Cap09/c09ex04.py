class TipoExemploPrivado():

    @property
    def nome(self): # propriedade substituindo método getter
        return self.__nome

    @nome.setter
    def nome(self, nome): # método setter
        self.__nome = nome

produto = TipoExemploPrivado()

# Rotina para a entrada de dados

nome = input("Informe o nome do produto ..: ")
produto.nome = nome

print("Produto informado ..........: {0}".format(produto.nome))

enter = input("\nPressione <Enter> para encerrar... ")
