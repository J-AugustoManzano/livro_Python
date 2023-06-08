dividendo = float(input("Informe um valor do dividendo...: "))
divisor = float(input("Informe um valor do divisor.....: "))

if (divisor == 0):
    print("\nImpossível realizar o cálculo.")
else:
    quociente = dividendo / divisor
    print("\nResultado = ", quociente)

enter = input("\nPressione <Enter> para encerrar... ")
