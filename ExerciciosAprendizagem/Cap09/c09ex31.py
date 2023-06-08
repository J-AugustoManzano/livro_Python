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
    except (KeyboardInterrupt, EOFError) as ke:
        print("\nAs teclas <Ctrl> + <C> ou <Ctrl> + <C> foram acionadas")
        print("Ocorrência [" + str(type(ke)) + "]\n")
    else:
        print("\nDado informado: ", entrada, "\n")

enter = input("Pressione <Enter> para encerrar... ")
