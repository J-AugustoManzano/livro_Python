arquivo = open("ARQTXT04.TEX", "w")

conta = 1
for registro in range(10):
    print("Entre o %2io. valor: " % conta, end="")
    valor = float(input())
    arquivo.write("%f\n" % valor)
    conta += 1

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")
