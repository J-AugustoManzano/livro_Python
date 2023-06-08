notas = []
lin = int(input("Quantas linhas ...: "))
col = int(input("Quantas colunas ..: "))
for i in range(lin):
    notas.append([])
    for j in range(col):
        notas[i].append(0)

print()
for i in range(lin):
    print("\nLinha {0:2} ...: \n".format(i + 1))
    for j in range(col):
        notas[i][j] = int(input("Coluna {0:2} ..: ".format(j + 1)))

print()
for i in range(lin):
    print("\nLinha {0:2} ...: \n".format(i + 1))
    for j in range(col):
        print("Coluna {0:2} ..: {1:4}".format(j + 1, notas[i][j]));

enter = input("\nPressione <Enter> para encerrar... ")
