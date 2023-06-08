import datetime

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

data = datetime.date(2015,11,19)
dias = data.toordinal()
futuro = dias + 10
passado = dias - 10

print("Data na forma DD/MM/AAAA .......: ", data.strftime("%d/%m/%Y"))
print("Dia da semana ..................: ", data.weekday())
print("Data em dias julianos ..........: ", dias)

print()
print("Data futura ....................: ", data.fromordinal(futuro).strftime("%d/%m/%Y"))
print("Dia da semana ..................: ", data.weekday())
print("Data furura em dias julianos ...: ", futuro)

print()
print("Data passado ...................: ", data.fromordinal(passado).strftime("%d/%m/%Y"))
print("Dia da semana ..................: ", data.weekday())
print("Data passado em dias julianos ..: ", passado)

pausa()
