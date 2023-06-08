import datetime

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

data = datetime.date(1965, 4, 26)
print(data.strftime("%d/%m/%Y"))

hora = datetime.time(13 ,10, 15)
print(hora.strftime("%H:%M:%S"))

tempo = datetime.datetime(1965, 4, 26, 13, 10, 15)
print(tempo.strftime("%d/%m/%Y | %H:%M:%S"))

pausa()
