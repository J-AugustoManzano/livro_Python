arquivo = open("ARQTXT01.TEX", "r")

for palavra in arquivo.readlines():
    print(palavra, end="")

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")
