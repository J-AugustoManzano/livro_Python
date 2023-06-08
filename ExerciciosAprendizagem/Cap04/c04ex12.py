while (True):
    n = input("Entre um valor numérico: ")
    if (n.isdigit()): break

print()
print("Resultado: %f" % (float(n) + 5))

enter = input("\nPressione <Enter> para encerrar... ")
