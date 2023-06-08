class TipoAluno():

    nome = ""
    notas = []
    media = 0.0

    def calcMedia(self):
        soma = 0.0
        for indice in range(4):
            soma += self.notas[indice]
        self.media = soma / 4.0

aluno = TipoAluno()

# Rotina para a entrada de dados

print(" CADASTRO DE ALUNO ".center(80, "-"))
print()
aluno.nome = input("Informe o nome ...: ")
print()
print("Informe as quatro notas bimestrais:")
print("".ljust(35, "="))
print()
for indice in range(4):
    aluno.notas.append(float(input(str(indice + 1) + "a. nota .........: ")))
aluno.calcMedia()

# Rotina para a saída de dados

print()
print("".ljust(80, "-"))
print("Relatório")
print("".ljust(80, "-"))
print()
print("Nome .........: {0}".format(aluno.nome))
print()
for indice in range(4):
    print(str(indice + 1) + "a. nota .....: {0:6.2f}".format(aluno.notas[indice]))
print()
print("Média ........: {0:6.2f}".format(aluno.media))
print()
if (aluno.media >= 6.0):
    print("Situação .....: Aprovado")
else:
    print("Situação .....: Reprovado")
 
enter = input("\nPressione <Enter> para encerrar... ")
