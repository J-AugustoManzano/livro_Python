import random
import datetime

random.seed(datetime.datetime.now())

class Error(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    def __str__(self):
        return str(self. mensagem)

class MaxError(Error):
    pass

class MinError(Error):
    pass

numeroSecreto = random.randint(1, 10)

while (True):
    try:
        numeroInformado = int(input("Entre um valor numérico: "))
        if (numeroInformado < numeroSecreto):
            raise MinError("Valor é baixo!")
        elif (numeroInformado > numeroSecreto):
            raise MaxError("Valor é alto!")
        break
    except MinError as me:
        print(me.mensagem)
    except MaxError as me:
        print(me.mensagem)
print("Você acertou!")

enter = input("\nPressione <Enter> para encerrar... ")
