a = []
b = []

print("Exemplo de checagem de índice\n")

# Entrada de dados

for i in range(10):
    valor = int(input("Entre o {0:2}o. valor: ".format(i + 1)))
    a.append(valor)

# Processamento par ou impar

print()
for i in range(10):
    if (i % 2 == 0):
        b.append(a[i] * 5)
    else:
        b.append(a[i] + 5)

# Apresentação das listas

print()
for i in range(10):
    print("A[{0:2}] = {1:4} na posição {2:2}.".format(i + 1, a[i], i))

print()
for i in range(10):
    print("B[{0:2}] = {1:4} na posição {2:2}.".format(i + 1, b[i], i))

enter = input("\nPressione <Enter> para encerrar... ")
