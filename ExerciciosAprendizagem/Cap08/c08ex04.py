notas = []
for linha in range(8):
    notas.append([])                
    for coluna in range(4):
        notas[linha].append(float(0.0))

# Entrada de notas escolares

print("Leitura e apresentação de notas escolares.")

for linha in range(8):
    print("\nAluno: {:2}\n".format(linha + 1))
    for coluna in range(4):
        notas[linha][coluna] = float(input("Informa a nota {0:2} do aluno {1:2}: ".format(coluna + 1, linha + 1)))

# Saída de notas escolares

for linha in range(8):
    print("\nAs notas do {:2}o. aluno são: \n".format(linha + 1))
    for coluna in range(4):
        print("Nota {0} = {1:6.2f}".format(coluna + 1, notas[linha][coluna]));

enter = input("\nPressione <Enter> para encerrar... ")
