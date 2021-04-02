s = 0
i = 1
while (i <= 10):
    n = float(input("Entre um valor numérico real: "))
    s += n
    i += 1

print()
print("Somatório ...: %10.2f" % s)
print("Média .......: %10.2f" % (s/10))

enter = input("\nPressione <Enter> para encerrar... ")
