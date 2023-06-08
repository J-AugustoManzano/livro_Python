class Teste(object):

    def __new__(cls):
        print("Objeto criado")
        return super(Teste, cls).__new__(cls)

    def __init__(self):
        print("Objeto inicializado")

    def __del__(self):
        print("Objeto finalizado")

objeto = Teste()
del objeto

enter = input("\nPressione <Enter> para encerrar... ")
