a = []

sp = 0
si = 0

i = 1
while (i <= 12):
    a.append(int(input("Entre o {0:2}o. nome em <A>: ".format(i))))
    i += 1

for i in range(12):
    if (a[i] % 2 == 0):
        sp += 1
    else:
        si += 1

print()

print("Total: pares ....: {0:4}".format(sp))
print("Total: impares ..: {0:4}".format(si))

enter = input("\nPressione <Enter> para encerrar... ")
