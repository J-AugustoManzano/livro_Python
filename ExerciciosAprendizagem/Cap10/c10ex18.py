try:
    with open("ARQBIN05.BIN", "rb").close() as arquivo:
        print("*** O arquivo foi aberto ***")
except FileNotFoundError:
    print("*** O arquivo não existe ***")
