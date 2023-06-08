soma = media = 0.0
print("Média de valores positivos")
print()
for entrada in range(1, 11):
    valor = float(input("Entre um valor numérico positivo: "))
    if (valor < 0): 
        print()
        print("O programa foi encerrado, entrada inválida.")
        break
    soma += valor
else:
    print()
    print("Somatório = ", soma / entrada)

enter = input("\nPressione <Enter> para encerrar... ")
