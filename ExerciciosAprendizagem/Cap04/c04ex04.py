n = int(input("Entre o valor da tabuada: "))

print()

for i in range(1, 11):
    r = n * i
    print("%2d x %2d = %3d" % (n, i, r))

enter = input("\nPressione <Enter> para encerrar... ")
