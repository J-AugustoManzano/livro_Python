linhas = 5
colunas = 3

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

c = []
for linha in range(linhas):
    c.append([])                
    for coluna in range(colunas):
        c[linha].append(int(0))

print("Lista bidimensional <A>")

for linha in range(linhas):
    print("\nLinha ...: {:2}".format(linha + 1))
    for coluna in range(colunas):
        a[linha][coluna] = int(input("Coluna ..: {0:2} = ".format(coluna + 1)))

print()

print("Lista bidimensional <B>")

for linha in range(linhas):
    print("\nLinha ...: {:2}".format(linha + 1))
    for coluna in range(colunas):
        b[linha][coluna] = int(input("Coluna ..: {0:2} = ".format(coluna + 1)))

for linha in range(linhas):
    for coluna in range(colunas):
        c[linha][coluna] = a[linha][coluna] + b[linha][coluna]

print()

print("Lista bidimensional <C>")

for linha in range(linhas):
    print("\nLinha ...: {:2}".format(linha + 1))    
    for coluna in range(colunas):
        print("Coluna ..: {0:2} = {1:4}".format(coluna + 1, c[linha][coluna]));

enter = input("\nPressione <Enter> para encerrar... ")
