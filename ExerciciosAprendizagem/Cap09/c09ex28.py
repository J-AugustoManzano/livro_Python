from math import *
from sys import *

while (True):
    try:
        valor = input("Entre um valor numérico inteiro: ")
        resultado = factorial(float(valor))
    except:
        print("\nRelatório de erro")
        print("\nValor informado é incorreto. Tente novamente.")
        print()
        print("Exceção detectada ..: ", exc_info()[0])
        print("Ocorrência .........: ", exc_info()[1])
        print("Endereço memória ...: ", exc_info()[2])
        print()
    else:
        print("\nResultado da fatorial = ", resultado)
        break

enter = input("\nPressione <Enter> para encerrar... ")
