while (True):
    try:
        valor = int(input("Entre um valor numérico inteiro: "))
    except ValueError:
        print("\nEntrada inválida, Tente novamente...")
    else:
        resultado = valor ** 3
        print("\nResultado do cubo: ", resultado)
        break
    finally:
        print("\n+--------------------+")
        print("| Programação Python |")
        print("+--------------------+\n")

enter = input("Pressione <Enter> para encerrar... ")
