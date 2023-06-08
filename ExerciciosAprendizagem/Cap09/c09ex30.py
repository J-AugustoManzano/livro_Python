while (True):
    try:
        print("Efetue uma das seguintes entradas:")
        print()
        print("Acione <Ctrl> + <C>")
        print("Acione <Ctrl> + <D>")
        print("Entre um dado qualquer")
        print("Informe 'fim1' para sair")
        print()
        entrada = input("Entrada: ")
        if (entrada == "fim"):
            break
    except KeyboardInterrupt as ki:
        print("\nAs teclas <Ctrl> + <C> foram acionadas [" + str(type(ki)) + "]\n")
    except EOFError as ee:
        print("\nAs teclas <Ctrl> + <D> foram acionadas [" + str(type(ee)) + "]\n")
    else:
        print("\nDado informado: ", entrada, "\n")

enter = input("Pressione <Enter> para encerrar... ")
