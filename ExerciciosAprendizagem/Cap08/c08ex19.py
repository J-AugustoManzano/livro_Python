def somatorio(*valores):
    soma = 0
    for i in range(0, len(valores)):
        soma += valores[i]
    return soma

dados1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
dados2 = [1, 2, 3, 4, 5]
dados3 = [22, 33, 55]

print(somatorio(*dados1))
print(somatorio(*dados2))
print(somatorio(*dados3))

enter = input("\nPressione <Enter> para encerrar... ")
