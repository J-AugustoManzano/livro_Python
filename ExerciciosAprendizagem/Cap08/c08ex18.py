def listagem(*lista):
    print(lista)
    print()
    for i in range(0, len(lista)):
        print(lista[i])

valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

listagem(*valores)

enter = input("\nPressione <Enter> para encerrar... ")
