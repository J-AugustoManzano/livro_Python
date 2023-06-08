def divisao(dividendo, divisor):
    return dividendo / divisor

x = eval(input("Entre o dividendo ...: "))
y = eval(input("Entre o divisor .....: "))

try:
    print("\nResultado = ", divisao(x, y))
except ZeroDivisionError:
    print("\nImpossível realizar o cálculo.")

enter = input("\nPressione <Enter> para encerrar... ")
