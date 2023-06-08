soma = 0.0
entrada = 1
print("Somatório de valores positivos")
print()
while (entrada <= 10):
    valor = float(input("Entre um valor numérico positivo: "))
    if (valor < 0):
        print()
        print("O programa foi encerrado, entrada inválida.")
        break
    soma += valor
    entrada += 1
else:
    print()
    print("Somatório = ", soma)

enter = input("\nPressione <Enter> para encerrar... ")
