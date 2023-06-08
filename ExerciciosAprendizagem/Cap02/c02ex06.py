horaTrabalhada = float(input("Entre a quantidade de horas trabalhadas ...: "))
vlrHora = float(input("Entre o valor da hora de trabalho .........: "))
percentDesconto = float(input("Entre o valor do percentual de desconto ...: "))

salarioBruto = horaTrabalhada * vlrHora
totalDesconto = (percentDesconto / 100.00) * salarioBruto
salarioLiquido = salarioBruto - totalDesconto

print()
print("Salário bruto .......... %8.2f" % salarioBruto)
print("Desconto ............... %8.2f" % totalDesconto)
print("Salário líquido ........ %8.2f" % salarioLiquido)

enter = input("\nPressione <Enter> para encerrar... ")
