try:
    arquivo = open("ARQBIN04.BIN", "rb")
    print(arquivo.read().decode("utf-8"))
    arquivo.close()    
except FileNotFoundError:
    print("Arquivo inexistente")

enter = input("\nPressione <Enter> para encerrar... ")
