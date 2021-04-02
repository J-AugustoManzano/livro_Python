import struct

arquivo = open("DADOS1.BIN", "rb")

for indice in range(5):
    valores = list(struct.unpack("i", arquivo.read(4)))
    print(valores[0])

arquivo.close()    

enter = input("\nPressione <Enter> para encerrar... ")
