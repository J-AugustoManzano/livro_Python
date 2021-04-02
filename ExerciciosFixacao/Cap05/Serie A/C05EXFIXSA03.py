def checaNumero(numero):
    if (numero % 2 == 0):
        print("Valor par")
    else:
        print("Valor impar")
        
n = int(input("Entre um valor numérico inteiro: "))

print()

checaNumero(n)

enter = input("\nPressione <Enter> para encerrar... ")
