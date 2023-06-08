diaSemana = (
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
)

meses = (
    "Jáneiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
)

print(diaSemana)
print()

for i in range(len(diaSemana)):
    print("{0}".format(diaSemana[i]))
print()

print(meses)
print()

for i in range(len(meses)):
    print("{0}".format(meses[i]))

enter = input("\nPressione <Enter> para encerrar... ")
