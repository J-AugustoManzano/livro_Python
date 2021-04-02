a = []
b = []
c = []

for i in range(5):
    a.append(float(input("Entre o {0:2}o. valor em <A>: ".format(i + 1))))

print()
for i in range(5):
    b.append(float(input("Entre o {0:2}o. valor em <B>: ".format(i + 1))))

for i in range(5):
    c.append(a[i] - b[i])

print()
for i in range(5):
    print("C[{0:2}] = {1:9.3f} na posição {2:2}.".format(i + 1, c[i], i))

enter = input("\nPressione <Enter> para encerrar... ")
