try:
    arquivo = open("ARQBIN04.BIN", "wb")
    try:
        arquivo.write(str.encode("Dado gravado"))
    finally:
        arquivo.close()    
except IOError:
    print("Arquivo corrompido ou em uso")    
