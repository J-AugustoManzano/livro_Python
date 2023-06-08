x = 9

print("\nValor da variável 'x' no programa principal com %d." % x)
print()

def valores():
    x = 7

    def valor1():
        global x
        x = 1
        y = 2
        print("coordenadas 'x' (sub-rotina) com %d e 'y' (sub-rotina) com %d." % (x, y))

    print("Valores da função valor1()")
    print()

    valor1()

    print("\nValor da variável 'x' na sub-rotina 'valores' com %d." % x)

    def valor2():
        nonlocal x
        x = 3
        y = 4
        print("coordenadas 'x' com %d e 'y' com %d." % (x, y))

    print()
    print("Valores da função valor2()")
    print()

    valor2()

    print("\nValor da variável 'x' na sub-rotina 'valores' após 'valor2' com %d." % x)

print("Valores da função valores()")
print()

valores()

print("\nValor da variável 'x' no programa principal (alterado) com %d.'" % x)

enter = input("\nPressione <Enter> para encerrar... ")
