arquivo = open("ARQTXT04.TEX", "r")

soma = 0
for registro in arquivo:
    soma += float(registro)

print("Somatório = ", soma)

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")
