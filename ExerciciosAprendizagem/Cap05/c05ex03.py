x = 9

print("\nValor da variável 'x' no programa principal com %d." % x)
print()

def valor():
    global x
    x = 1
    y = 2
    print("coordenadas 'x' (sub-rotina) com %d e 'y' (sub-rotina) com %d." % (x, y))

print("Valores da função valor()")
print()

valor()

print("\nValor da variável 'x' no programa principal (alterado) com %d.'" % x)

enter = input("\nPressione <Enter> para encerrar... ")
