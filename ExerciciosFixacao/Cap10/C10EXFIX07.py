import struct

arquivo1 = open("ARQ1.BIN", "rb")
arquivo2 = open("ARQ2.BIN", "rb")

x = []

for i in range(8):
    valores = list(struct.unpack("f", arquivo1.read(4)))
    x.append(valores[0])

for i in range(8):
    valores = list(struct.unpack("f", arquivo2.read(4)))
    x.append(valores[0])

print()
for i in range(16):
    print("X[{0:2}] = {1:7.2f} na posição {2:2}.".format(i + 1, x[i], i))

arquivo1.close()
arquivo2.close()

enter = input("\nPressione <Enter> para encerrar... ")

