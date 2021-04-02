n1 = float(input("Informe nota 1 ....: "))
n2 = float(input("Informe nota 2 ....: "))
n3 = float(input("Informe nota 3 ....: "))
n4 = float(input("Informe nota 4 ....: "))

md = (n1 + n2 + n3 + n4) / 4.0

if (md >=  5.0):
    print("Aprovado %5.2f" % md, end="")
else:
    print("Reprovado %5.2f" % md, end="")

print()

enter = input("\nPressione <Enter> para encerrar... ")
