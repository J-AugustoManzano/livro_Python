import struct

arquivo = open("DADOS3.BIN", "rb")

a = []

for i in range(5):
    valores = list(struct.unpack("f", arquivo.read(4)))
    a.append(valores[0])

print()
for i in range(5):
    print("A[{0:2}] = {1:7.2f} na posição {2:2}.".format(i + 1, a[i], i))

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")

