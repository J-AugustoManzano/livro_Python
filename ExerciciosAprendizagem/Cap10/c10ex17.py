try:
    arquivo = open("ARQBIN05.BIN", "rb")
    print("*** O arquivo foi aberto ***")
except FileNotFoundError:
    print("*** O arquivo não existe ***")
finally:
    if ("arquivo") in locals():
        arquivo.close()    
