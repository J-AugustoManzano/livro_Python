def somatorio(n):
    s = 0
    for i in range(1, n+1):
        s += i
    print("Somatório = %i" % s)

n = int(input("Entre valor para limite de somatório: "))

print()

somatorio(n)

enter = input("\nPressione <Enter> para encerrar... ")
