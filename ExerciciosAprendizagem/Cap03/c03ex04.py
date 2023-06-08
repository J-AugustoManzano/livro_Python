codigo = int(input("Entre o código de acesso: "))

print()

if (codigo == 1 or codigo == 2 or codigo == 3):
    if (codigo == 1):
        print("Foi acionado o código: um.")
    if (codigo == 2):
        print("Foi acionado o código: dois.")
    if (codigo == 3):
        print("Foi acionado o código: três.")
else:
    print("Código inválido.")

enter = input("\nPressione <Enter> para encerrar... ")
