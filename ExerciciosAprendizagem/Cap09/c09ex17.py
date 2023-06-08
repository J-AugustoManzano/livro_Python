class Hexadecimal(object):

    def __init__(self, valor):
        self.resultado = hex(valor)

    def __str__(self):
        return "%s" % (self.resultado[2:].upper() + "h")

    def __gt__(self, entrada):
        return self.resultado > entrada.resultado

    def __add__(self, entrada):
        return str(hex(int(self.resultado, 16) + int(entrada.resultado, 16)))[2:].upper() + "h"

valor1 = Hexadecimal(10)
valor2 = Hexadecimal(15)

if (valor1 > valor2):
    print("O valor %s é maior que o valor %s" % (valor1, valor2))
else:
    print("O valor %s é menor ou igual ao valor %s" % (valor1, valor2))

print("A soma dos valores hexadecimais corresponde a: ", valor1 + valor2)

enter = input("\nPressione <Enter> para encerrar... ")
