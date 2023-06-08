import datetime

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

entraData = input("Emtre uma data no formato DD/MM/AAAA: ")

dia = int(entraData[ 0: 2])
mes = int(entraData[ 3: 5])
ano = int(entraData[ 6:10])

data = datetime.date(ano, mes, dia)

if (data.weekday() == 0):
    print("segunda-feira")
elif (data.weekday() == 1):
    print("terça-feira")
elif (data.weekday() == 2):
    print("quarta-feira")
elif (data.weekday() == 3):
    print("quinta-feira")
elif (data.weekday() == 4):
    print("sexta-feira")
elif (data.weekday() == 5):
    print("sábado")
elif (data.weekday() == 6):
    print("domingo")

pausa()
