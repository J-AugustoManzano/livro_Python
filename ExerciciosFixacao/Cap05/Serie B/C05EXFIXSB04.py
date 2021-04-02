def positivo(numero):
    if (numero < 0):
        return numero * -1
    else:
        return numero
        
n = int(input("Entre um valor numérico inteiro: "))

print()

print(positivo(n))

enter = input("\nPressione <Enter> para encerrar... ")
