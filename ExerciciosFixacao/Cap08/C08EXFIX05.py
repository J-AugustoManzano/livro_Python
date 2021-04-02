a = []
b = []
c = []

for i in range(4):
    a.append(input("Entre o {0:2}o. nome em <A>: ".format(i + 1)))

print()
for i in range(3):
    b.append(input("Entre o {0:2}o. nome em <B>: ".format(i + 1)))

for i in range(7):
    if (i <= 3):
        c.append(a[i])
    else:
        c.append(b[i - 4])

print()
for i in range(7):
    print("C[{0:2}] = {1}".format(i + 1, c[i]))

enter = input("\nPressione <Enter> para encerrar... ")
