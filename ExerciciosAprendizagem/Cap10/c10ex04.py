arquivo = open("ARQTXT02.TEX", "w+")

A = []
B = []

for indice in range(5):
    A.append(int(input("Entre o " + str(indice + 1) + " valor: ")))
    arquivo.write("%i\n" % A[indice])

arquivo.seek(0)
print()

conta = 0
for indice in arquivo.readlines():
    B.append(indice)
    print("O", int(B.index(indice)) + 1, "o. elemento equivale a ", B[conta], end="")
    conta += 1

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")
