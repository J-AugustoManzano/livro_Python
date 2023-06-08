dicionario = {"nome":"Carlos", "idade":34, "escolaridade":"superior"}

for i, j in dicionario.items():
    print(i, " = ", j)

print()

for i in dicionario.keys():
    print(i)

print()

for i in dicionario.values():
    print(i)

enter = input("\nPressione <Enter> para encerrar... ")
