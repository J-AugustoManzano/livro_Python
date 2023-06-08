import c06modulo

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

base = float(input("Emtre o valor da base da raiz ....: "))
indice = int(input("Emtre o valor do índice da raiz ..: "))

resultado = c06modulo.root(base, indice)

print()
print("O valor da raiz calculada equivale a: ", resultado)

pausa()
