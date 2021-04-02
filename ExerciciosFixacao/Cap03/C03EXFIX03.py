n1 = float(input("Informe nota 1 ....: "))
n2 = float(input("Informe nota 2 ....: "))
n3 = float(input("Informe nota 3 ....: "))
n4 = float(input("Informe nota 4 ....: "))

md1 = (n1 + n2 + n3 + n4) / 4.0

if (md1 >=  7.0):
    print("Aprovado com média %5.2f" % md1, end="")
else:
    ex = float(input("Informe nota 5 ....: "))
    md2 = (md1 + ex) / 2.0
    if (md2 >= 5.0):
        print("Aprovado em exame com média", end="")
    else:
        print("Reprovado com média ", end="")
    print("%5.2f" % md2)

enter = input("\nPressione <Enter> para encerrar... ")
