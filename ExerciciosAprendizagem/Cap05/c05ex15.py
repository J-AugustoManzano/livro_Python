def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

def somatorio(n):
    s = 0
    for i in range(1, (n + 1)):
        s += i
    return s

def fatorial(n):
    f = 1
    for i in range(1, (n + 1)):
        f *= i
    return f

operacao = somatorio

print("Somatório de 5 é igual a ....: %5d" % operacao(5))

operacao = fatorial

print("Fatorial de 5 é igual a .....: %5d" % operacao(5))

pausa()
