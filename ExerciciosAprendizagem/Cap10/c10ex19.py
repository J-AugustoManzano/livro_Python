import struct

try:
    arquivo = open("ARQBIN06.BIN", "a+b")

    print("Cadastro sequencial de valores")

    while True:
        print()
        valor = int(input("Informe um valor inteiro: "))
        arquivo.write(struct.pack("i", valor))
        print("\nDeseja continuar?\n")
        resp = input("[S] para Sim | [qualquer letra] para Nao --> ")
        if (resp.upper() != "S"): break
    arquivo.close()    

except FileNotFoundError:
    print("Arquivo inexistente")

enter = input("\nPressione <Enter> para encerrar... ")
