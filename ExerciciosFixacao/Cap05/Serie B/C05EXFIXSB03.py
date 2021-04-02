def checaNumero(numero):
    if (numero % 2 == 0):
        return "Valor par"
    else:
        return "Valor impar"
        
n = int(input("Entre um valor numérico inteiro: "))

print()

print(checaNumero(n))

enter = input("\nPressione <Enter> para encerrar... ")
