try:
    arquivo = open("ARQBIN03.BIN", "rb")
    print("*** O arquivo foi aberto ***")
    arquivo.close()    
except FileNotFoundError:
    arquivo = open("ARQBIN03.BIN", "wb")
    print("*** O arquivo foi criado ***")
    arquivo.close()    
