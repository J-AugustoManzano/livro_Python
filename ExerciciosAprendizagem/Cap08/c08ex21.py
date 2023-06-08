def multiplicativo(*valores):
    fator = 1
    for i in range(0, len(valores)):
        fator *= valores[i]
    return fator

print(multiplicativo(1, 2, 3, 4, 5))
print(multiplicativo(2, 4))
print(multiplicativo(9, 2, 7))

enter = input("\nPressione <Enter> para encerrar... ")
