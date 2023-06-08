import random
import datetime

random.seed(datetime.datetime.now())

print("Adivinhe um número!\n")

numeroSecreto = random.randint(1, 10)
while (True):
    numeroInformado = int(input("Entre um valor numérico: "))
    print("Você informou o valor: ", numeroInformado);
    if (numeroInformado < numeroSecreto):
        print("Valor é baixo!")
    elif (numeroInformado > numeroSecreto):
        print("Valor é alto!")
    elif (numeroInformado == numeroSecreto):
        print("Você acertou!")
        break

enter = input("\nPressione <Enter> para encerrar... ")
