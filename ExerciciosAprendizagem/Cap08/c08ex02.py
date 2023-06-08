a = []
s = 0

print("Exemplo de checagem de elemento\n")

# Entrada de dados

for i in range(5):
    a.append(int(input("Entre o {0:2}o. valor: ".format(i + 1))))

# Processamento par ou impar

for i in range(len(a)):
    if (a[i] % 2 == 0):
        s += a[i]

# Apresentação das listas

print()
print("Soma dos elementos pares = {0}".format(s))

enter = input("\nPressione <Enter> para encerrar... ")
