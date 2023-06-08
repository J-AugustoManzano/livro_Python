n = int(input("Entre um valor numérico: "))

r4 = n - 4 * (n // 4)
r5 = n - 5 * (n // 5)

if (r4 == 0 and r5 == 0):
    print("%i" % n)
else:
    print("Valor não é divisível por 4 e 5.")

enter = input("\nPressione <Enter> para encerrar... ")
