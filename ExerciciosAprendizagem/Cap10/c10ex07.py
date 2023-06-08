arquivo = open("ARQTXT04.TEX", "r")

soma = ""
for registro in arquivo:
    soma += registro

print("Somatório = ", soma)

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")
