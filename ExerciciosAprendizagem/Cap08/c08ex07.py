a = []

# Entrada de dados

quantidade = int(input("Quantos elementos a entrar: "))

print()
for i in range(quantidade):
    valor = int(input("Entre o {0:2}o. valor: ".format(i + 1)))
    a.append(valor)

# Apresentação das listas

print()
for i in range(len(a)):
    print("A[{0:2}] = {1:4} na posição {2:2}.".format(i + 1, a[i], i))

enter = input("\nPressione <Enter> para encerrar... ")
