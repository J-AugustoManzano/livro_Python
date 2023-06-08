notas = [
  [2.5, 5.5, 7.0, 8.0],
  [3.7, 6.5, 6.0, 2.0],
  [7.5, 7.5, 7.0, 9.0],
  [1.5, 2.5, 5.3, 1.2],
  [4.5, 5.5, 6.8, 5.5],
  [6.5, 9.5, 7.5, 8.5],
  [8.5, 7.5, 7.2, 3.9],
  [8.5, 2.5, 7.8, 4.8]
]
soma = 0

for i in range(8):
    for j in range(4):
        soma += notas[i][j]
    media = soma / 32

print("Média da sala: {0:6.2f}".format(media))

enter = input("\nPressione <Enter> para encerrar... ")
