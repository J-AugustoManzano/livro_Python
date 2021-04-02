def somatorio(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

n = int(input("Entre valor para limite de somatório: "))

print()

print("Somatório = %i" % somatorio(n))

enter = input("\nPressione <Enter> para encerrar... ")
