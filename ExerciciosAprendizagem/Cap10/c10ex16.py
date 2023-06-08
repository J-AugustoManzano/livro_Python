try:
    arquivo = open("ARQBIN05.BIN", "rb")
    print("*** O arquivo foi aberto ***")
except FileNotFoundError:
    print("*** O arquivo não existe ***")
finally:
    arquivo.close()    
