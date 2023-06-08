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

def superCalculo(n, operacao):
    return operacao(n)

print("Somatório de 5 é igual a ....: %5d" % superCalculo(5, somatorio))
print("Fatorial de 5 é igual a .....: %5d" % superCalculo(5, fatorial))

pausa()
