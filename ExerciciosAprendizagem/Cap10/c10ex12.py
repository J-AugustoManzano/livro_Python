try:
    arquivo = open("ARQBIN02.BIN", "rb")
    arquivo.close()    
except FileNotFoundError:
    print("O arquivo não pode ser aberto")
    print("***  arquivo inexistente  ***")
else:
    print("*** O arquivo foi aberto ***")
