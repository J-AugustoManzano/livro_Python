import hashlib

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

senha = input("Entre sua senha: ")

if (hashlib.md5(senha.encode()).hexdigest() == "e10adc3949ba59abbe56e057f20f883e"):
    n = int(input("\nEntre o valor da tabuada: "))
    print()
    for i in range(1, 11):
        r = n * i
        print("%2d x %2d = %3d" % (n, i, r))
else:
    print("Senha informa é incorreta")

pausa()
