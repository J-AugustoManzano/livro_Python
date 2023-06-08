f = 0
def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

def fatorial(valor):
    global f
    f = 1
    for i in range(1, valor + 1):
        f *= i

while (True):
    n = int(float(input("Entre o valor da fatorial: ")))
    if (n >= 0): break

fatorial(n)

print("Resultado da fatorial de %d! = %d" % (n, f))

pausa()
