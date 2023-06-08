import datetime
import calendar

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

dataHoje = datetime.date.today()

calendario = calendar.month(dataHoje.year, dataHoje.month)

print("Calendário Python\n")
print(calendario)

pausa()
