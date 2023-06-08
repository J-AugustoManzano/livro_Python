class Hexadecimal(object):

    def __init__(self, valor):
        self.resultado = hex(valor)

    def __str__(self):
        return "%s" % (self.resultado[2:].upper() + "h")

valor = Hexadecimal(1965)

print("Resultado ", valor)

enter = input("\nPressione <Enter> para encerrar... ")
