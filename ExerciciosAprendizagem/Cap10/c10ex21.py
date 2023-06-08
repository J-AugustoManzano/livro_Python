import struct

try:
    arquivo = open("ARQBIN06.BIN", "r+b")

    print("Pesquisa direta e escrita de valores")

    arquivo.seek(0, 2)
    tamanho = arquivo.tell()
    nr_regs = tamanho / 4
    arquivo.seek(0)

    while True:
        print()
        pos = int(input("Informe a posicao a ser alterada: "))
        if (pos >= 1 and pos <= nr_regs):
            print()
            valor = int(input("Informe um valor inteiro: "))
            arquivo.seek((pos - 1) * 4, 0)
            arquivo.write(struct.pack("i", valor))
            print("\nPosição " + str(pos) + " valor = " + str(valor))
        else:
            print("\nPosicao informada - invalida.")

        print("\nDeseja continuar?\n")
        resp = input("[S] para Sim | [qualquer letra] para Nao --> ")
        if (resp.upper() != "S"): break
    arquivo.close()    

except FileNotFoundError:
    print("Arquivo inexistente")

enter = input("\nPressione <Enter> para encerrar... ")
