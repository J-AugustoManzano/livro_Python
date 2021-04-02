def positivo(numero):
    if (numero < 0):
        print(numero * -1)
    else:
        print(numero)
        
n = int(input("Entre um valor numérico inteiro: "))

print()

positivo(n)

enter = input("\nPressione <Enter> para encerrar... ")
