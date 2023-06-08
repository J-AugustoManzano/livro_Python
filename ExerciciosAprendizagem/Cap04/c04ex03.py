n = int(input("Entre o valor da tabuada: "))

print()

i = 1
while not (i > 10):
    r = n * i;
    print("%2d x %2d = %3d" % (n, i, r))
    i = i + 1

enter = input("\nPressione <Enter> para encerrar... ")
