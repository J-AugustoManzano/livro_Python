a = []

for i in range(10):
    a.append(input("Entre o {0:2}o. nome: ".format(i + 1)))

print()
for i in range(10):
    print("{0:2}o. nome {1}.".format(i + 1, a[i]))

enter = input("\nPressione <Enter> para encerrar... ")
