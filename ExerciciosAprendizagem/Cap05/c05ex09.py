def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

def fatorial(valor):
    if (valor == 0):
        return 1
    else:
        return valor * fatorial(valor - 1)

while (True):
    n = int(float(input("Entre o valor da fatorial: ")))
    if (n >= 0): break

fatorial(n)

print("Resultado da fatorial de %d! = %d" % (n, fatorial(n)))

pausa()
