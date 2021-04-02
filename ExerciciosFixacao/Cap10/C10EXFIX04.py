import struct

arquivo = open("DADOS3.BIN", "wb")

a = []

for i in range(5):
    a.append(float(input("Entre o {0:2}o. valor: ".format(i + 1))))

for i in range(5):
    arquivo.write(struct.pack("f", a[i]))

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")

