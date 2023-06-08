import datetime

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

dataHoje = datetime.date.today()

print("Data completa ..: ", dataHoje)
print("Ano ............: ", dataHoje.year)
print("Mês ............: ", dataHoje.month)
print("Dia ............: ", dataHoje.day)

pausa()
