a = []
b = []
c = []

i = 1
while (i <= 5):
    valor = int(input("Entre o {0:2}o. nome em <A>: ".format(i)))
    if (valor % 2 == 0):
        a.append(valor)
        i += 1
print()

i = 1
while (i <= 5):
    valor = int(input("Entre o {0:2}o. nome em <B>: ".format(i)))
    if (valor % 2 != 0):
        b.append(valor)
        i += 1

for i in range(10):
    if (i <= 4):
        c.append(a[i])
    else:
        c.append(b[i - 5])

print()
for i in range(10):
    print("C[{0:2}] = {1:5}".format(i + 1, c[i]))

enter = input("\nPressione <Enter> para encerrar... ")
