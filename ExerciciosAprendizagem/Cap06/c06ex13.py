import time

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

valor = 0
while (valor <= 9):
    print(valor)
    time.sleep(1)
    valor = valor + 1

pausa()
