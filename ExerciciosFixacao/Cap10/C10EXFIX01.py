import struct

arquivo = open("DADOS1.BIN", "wb")

for indice in range(5):
    print("Entre o %2io. valor: " % (indice + 1), end="")
    valor = int(input())
    arquivo.write(struct.pack("i", valor))

arquivo.close()        

enter = input("\nPressione <Enter> para encerrar... ")
