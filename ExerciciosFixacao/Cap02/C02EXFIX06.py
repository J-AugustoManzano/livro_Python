sa = float(input("Informe valor do salário .........: "))
pr = float(input("Informe percentual de reakuste ...: "))

ns = sa + sa * (pr / 100)

print()
print("Novo salário = %12.2f" % ns)

enter = input("\nPressione <Enter> para encerrar... ")
