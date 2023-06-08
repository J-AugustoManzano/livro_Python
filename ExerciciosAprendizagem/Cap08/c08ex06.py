linhas = 5
colunas = 4

a = []
for linha in range(linhas):
    a.append([])                
    for coluna in range(colunas):
        a[linha].append(int(0))

b = []
for linha in range(linhas):
    b.append([])                
    for coluna in range(colunas):
        b[linha].append(float(0.0))

print("Entrada de dados")

for linha in range(linhas):
    print("\nLinha ...: {:2}".format(linha + 1))
    for coluna in range(colunas):
        a[linha][coluna] = int(input("Coluna ..: {0:2} = ".format(coluna + 1)))

for linha in range(linhas):
    for coluna in range(colunas):
        b[linha][coluna] = a[linha][coluna] ** (1/3)

print()
print("Saída dos dados\n")

for linha in range(linhas):
    for coluna in range(colunas):
        print("A[{0},{1}] = {2:4} | A[{0},{1}] = {3:0.8f}".format(linha \
        + 1, coluna + 1, a[linha][coluna], b[linha][coluna]))

enter = input("\nPressione <Enter> para encerrar... ")
