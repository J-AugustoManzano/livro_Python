a = []
b = []

for i in range(8):
    a.append(float(input("Entre o {0:2}o. valor em <A>: ".format(i + 1))))

for i in range(8):
    b.append(a[7 - i])

print()
for i in range(8):
    print("A[{0:2}] = {1:5.2f} | B[{0:2}] = {2:5.2f}".format(i + 1, a[i], b[i]))

enter = input("\nPressione <Enter> para encerrar... ")
