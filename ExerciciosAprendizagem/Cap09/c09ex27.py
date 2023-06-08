from math import *

while (True):
    try:
        valor = float(input("Entre um valor positivo: "))
        resultado = sqrt(valor)
        print("\nResultado da raiz quadrada = ", resultado)
        break
    except ValueError as ve:
        print("\nEntrada inválida. Tente novamente")
        print("\nErro ......: ", ve)
        print("Exceção ...: ", type(ve), "\n")

enter = input("\nPressione <Enter> para encerrar... ")
