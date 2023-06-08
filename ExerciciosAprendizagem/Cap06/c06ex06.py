import datetime

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

agora = datetime.datetime.now()

print("Ano ......: ", agora.year)
print("Mês ......: ", agora.month)
print("Dia ......: ", agora.day)
print("Hora .....: ", agora.hour)
print("Minuto ...: ", agora.minute)
print("Segundo ..: ", agora.second)

pausa()
