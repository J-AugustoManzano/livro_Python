import struct

try:
    arquivo = open("ARQBIN06.BIN", "r+b")

    print("Pesquisa direta de valores")

    arquivo.seek(0, 2)
    tamanho = arquivo.tell()
    nr_regs = tamanho / 4
    arquivo.seek(0)

    while True:
        print()
        pos = int(input("Informe a posicao a ser pesquisada: "))
        if (pos >= 1 and pos <= nr_regs):
            arquivo.seek((pos - 1) * 4, 0)
            valor = list(struct.unpack("i", arquivo.read(4)))
            print("\nPosição " + str(pos) + " valor = ", end="")
            print(valor[0])
        else:
            print("\nPosicao informada - invalida.")

        print("\nDeseja continuar?\n")
        resp = input("[S] para Sim | [qualquer letra] para Nao --> ")
        if (resp.upper() != "S"): break
    arquivo.close()    

except FileNotFoundError:
    print("Arquivo inexistente")

enter = input("\nPressione <Enter> para encerrar... ")
