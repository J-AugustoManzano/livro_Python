import datetime

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

agora = datetime.datetime.now()

print(agora.strftime("%d/%m/%Y | %H:%M:%S"))

pausa()
