from c06modulo import root

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

base = float(input("Emtre o valor da base da raiz ....: "))
indice = int(input("Emtre o valor do índice da raiz ..: "))

resultado = root(base, indice)

print()
print("O valor da raiz calculada equivale  a: ", resultado)

pausa()
