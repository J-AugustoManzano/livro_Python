def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

fatorial = lambda x: 1 if (x <= 1) else x * fatorial(x - 1)

print(fatorial(5))

pausa()
