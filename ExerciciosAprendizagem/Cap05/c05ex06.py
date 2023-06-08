def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

def divisao(dividendo, divisor):
    print("Resultado = %f" % (dividendo / divisor))
    pausa()

a = float(input("Emtre o valor do dividendo ...: "))
b = float(input("Emtre o valor do divisor .....: "))

divisao(a, b)  
pausa()
