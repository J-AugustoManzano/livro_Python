import os

arquivo = open("ARQTXT03.TEX", "w+")

A = []
B = []

for indice in range(8):
    A.append(float(input("Entre o " + str(indice + 1) + " valor: ")))
    arquivo.write("%f\n" % A[indice])

arquivo.seek(0, 0)
print()

conta = 0
for indice in arquivo.readlines():
    B.append(indice)
    print("O", int(B.index(indice)) + 1, "o. elemento equivale a ", B[conta], end="")
    conta += 1

arquivo.close()

for arquivo in os.listdir():
    if arquivo == "ARQTXT03.TEX":
        os.remove(arquivo)

enter = input("\nPressione <Enter> para encerrar... ")
