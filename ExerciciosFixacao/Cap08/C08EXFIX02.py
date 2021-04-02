a = []
b = []

for i in range(10):
    a.append(int(input("Entre o {0:2}o. valor: ".format(i + 1))))

for i in range(10):
    b.append(a[i] * 3)

print()
for i in range(10):
    print("B[{0:2}] = {1:4} na posição {2:2}.".format(i + 1, b[i], i))

enter = input("\nPressione <Enter> para encerrar... ")
