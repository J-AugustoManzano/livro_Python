dividendo = float(input("Informe um valor do dividendo...: "))
divisor = float(input("Informe um valor do divisor.....: "))

try:
    quociente = dividendo / divisor
    print("\nResultado = ", quociente)
except ZeroDivisionError:
    print("\nImpossível realizar o cálculo.")

enter = input("\nPressione <Enter> para encerrar... ")
