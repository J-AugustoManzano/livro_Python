arquivo = open("ARQTXT01.TEX", "a")

palavra = input("Entre uma palavra --> ")

arquivo.write("%s\n" % palavra)

print(palavra, "foi gravado no arquivo 'ARQTXT01.TEX'.")

arquivo.close()

enter = input("\nPressione <Enter> para encerrar... ")
