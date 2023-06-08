escolar = {}

# Entrada de dados

for i in range(8):
    nome = input("Entre o nome do {0:2}o. aluno: ".format(i + 1))
    escolar[i] = nome

# Apresentação das listas

print()
for i in range(8):
    print("Aluno {0} ...: {1}".format(i + 1, escolar[i]))

enter = input("\nPressione <Enter> para encerrar... ")
