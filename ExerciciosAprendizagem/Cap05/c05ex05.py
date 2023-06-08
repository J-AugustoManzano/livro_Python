def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

def fatorial():
    while (True):
        n = int(float(input("Entre um valor inteiro positivo: ")))
        if (n >= 0): break
    f = 1
    for i in range(1, n + 1):
        f *= i # equivale a f = f * i
    print("Resultado = %d" % f)
    pausa()
  
fatorial()
