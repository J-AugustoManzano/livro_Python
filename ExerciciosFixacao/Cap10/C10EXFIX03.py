import struct

arquivo = open("DADOS2.BIN", "wb")

a = []
b = []
c = []

for i in range(10):
    valor = float(input("Entre o {0:2}o. valor: ".format(i + 1)))
    a.append(valor)

print()
for i in range(10):
    b.append(a[i] ** 2)

for i in range(10):
    valor = b[i]
    arquivo.write(struct.pack("f", valor))

arquivo.close()

arquivo = open("DADOS2.BIN", "rb")

for i in range(10):
    valores = list(struct.unpack("f", arquivo.read(4)))
    c.append(valores[0])

print()
for i in range(10):
    print("C[{0:2}] = {1:7.2f} na posição {2:2}.".format(i + 1, c[i], i))

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")

