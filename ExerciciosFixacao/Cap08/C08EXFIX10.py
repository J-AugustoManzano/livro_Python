linhas = 5
colunas = 5

a = []
for linha in range(linhas):
    a.append([])                
    for coluna in range(colunas):
        a[linha].append(int(0))

b = []
for linha in range(linhas):
    b.append([])                
    for coluna in range(colunas):
        b[linha].append(int(0))


print("Lista bidimensional <A>")

for linha in range(linhas):
    print("\nLinha ...: {:2}".format(linha + 1))
    for coluna in range(colunas):
        a[linha][coluna] = int(input("Coluna ..: {0:2} = ".format(coluna + 1)))

for linha in range(linhas):
    for coluna in range(colunas):
        if (linha == coluna):
            b[linha][coluna] = a[linha][coluna] * 3
        else:
            b[linha][coluna] = a[linha][coluna] * 2

print()
print("Lista bidimensional <B>")

for linha in range(linhas):
    for coluna in range(colunas):
        print("B[{0},{1}] = {2:4}".format(linha + 1, coluna + 1, \
        b[linha][coluna]))

enter = input("\nPressione <Enter> para encerrar... ")
