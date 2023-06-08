def checaPar(valor):
    return (valor % 2 == 0)

valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = filter(checaPar, valores)

for i in pares:
    print(i)

enter = input("\nPressione <Enter> para encerrar... ")
