import struct

arquivo = open("ARQBIN01.BIN", "rb")

for indice in range(10):
    valores = list(struct.unpack("f", arquivo.read(4)))
    print(valores[0])

arquivo.close()    

enter = input("\nPressione <Enter> para encerrar... ")
