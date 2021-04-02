s = 0
for i in range(1, 11):
    n = float(input("Entre um valor numérico real: "))
    s += n

print()
print("Somatório ...: %10.2f" % s)
print("Média .......: %10.2f" % (s/10))

enter = input("\nPressione <Enter> para encerrar... ")
