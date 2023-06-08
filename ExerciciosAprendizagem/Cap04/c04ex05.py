n = int(input("Entre o valor da tabuada: "))

print()

for i in range(10):
    r = n * (i + 1)
    print("%2d x %2d = %3d" % (n, i + 1, r))

enter = input("\nPressione <Enter> para encerrar... ")
