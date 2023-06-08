nome = input("Informe seu nome ...........: ")
nasc = int(input("Informe ano de nascimento ..: "))
hoje = int(input("Informe ano atual ..........: "))
idade = hoje - nasc
print("Olá, %s" % nome)
print("você possui em torno de %d anos de idade" % idade)
enter = input("\nPressione <Enter> para encerrar... ")
