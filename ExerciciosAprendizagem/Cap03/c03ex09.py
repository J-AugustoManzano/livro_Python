﻿mes = float(input("Entre um numero equivalente a um MÊS: "))

print()

if (mes == 1):
    print("Janeiro.")
elif (mes == 2):
    print("Fevereiro.")
elif (mes == 3):
    print("Março.")
elif (mes == 4):
    print("Abril.")
elif (mes == 5):
    print("Maio.")
elif (mes == 6):
    print("Junho.")
elif (mes == 7):
    print("Julho.")
elif (mes == 8):
    print("Agosto.")
elif (mes == 9):
    print("Setembro.")
elif (mes == 10):
    print("Outubro.")
elif (mes == 11):
    print("Novembro.")
elif (mes == 12):
    print("Dezembro.")
else:
    if (mes < 1 or mes > 12):
        print("Mês inválido.")
    
enter = input("\nPressione <Enter> para encerrar... ")
