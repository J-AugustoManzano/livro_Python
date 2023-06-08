while (True):
    try:
        valor = int(input("Entre um valor inteiro: "))
        resultado = valor ** 3
        print("\nResultado = ", resultado)
        break
    except ValueError:
        print("\nEntrada Inválida. Tente novamente")
        print()

enter = input("\nPressione <Enter> para encerrar... ")
