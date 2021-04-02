import struct

arquivo1 = open("ARQ1.BIN", "wb")
arquivo2 = open("ARQ2.BIN", "wb")

a = []
b = []

for i in range(8):
    a.append(float(input("Entre o {0:2}o. valor da lista <A>: ".format(i + 1))))

for i in range(8):
    b.append(float(input("Entre o {0:2}o. valor da lista <B>: ".format(i + 1))))

for i in range(8):
    arquivo1.write(struct.pack("f", a[i]))

for i in range(8):
    arquivo2.write(struct.pack("f", b[i]))

arquivo1.close()
arquivo2.close()

enter = input("\nPressione <Enter> para encerrar... ")

