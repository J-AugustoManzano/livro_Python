valor = int(input("Entre um valor numérico inteiro: "))

resp = ("Valor impar", "Valor par")[valor % 2 == 0]

print()
print(resp)

enter = input("\nPressione <Enter> para encerrar... ")
