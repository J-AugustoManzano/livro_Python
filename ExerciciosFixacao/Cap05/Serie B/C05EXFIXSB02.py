def potencia(base, expoente):
    p = 1
    for i in range(1, expoente+1):
        p *= base
    return p

b = int(input("Entre valor da base ......: "))
e = int(input("Entre valor do exponete ..: "))

print()

print("Potência = %i" % potencia(b, e))

enter = input("\nPressione <Enter> para encerrar... ")
