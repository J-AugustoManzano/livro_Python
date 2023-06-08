def multiplicativo(*valores):
    fator = 1
    for i in range(0, len(valores)):
        fator *= valores[i]
    return fator

lista = [1, 2, 3, 3]
tupla = (1 ,2, 3, 3)
agMut = {1 ,2, 3, 3}
agImt = frozenset({1 ,2, 3, 3})

print("Lista ...........: ", multiplicativo(*lista))
print("Tupla ...........: ", multiplicativo(*tupla))
print("Agrup. mutável ..: ", multiplicativo(*agMut))
print("Agrup. imutável .: ", multiplicativo(*agImt))

enter = input("\nPressione <Enter> para encerrar... ")
