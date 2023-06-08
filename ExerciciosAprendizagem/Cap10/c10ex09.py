import struct

arquivo = open("ARQBIN01.BIN", "wb")

for indice in range(10):
    print("Entre o %2io. valor: " % (indice + 1), end="")
    valor = float(input())
    arquivo.write(struct.pack("f", valor))

arquivo.close()        

enter = input("\nPressione <Enter> para encerrar... ")
