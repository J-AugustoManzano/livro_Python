class TipoSala():

    @property
    def sala(self): 
        return self._sala

    @sala.setter
    def sala(self, sala): 
        self._sala = sala

class TipoSerie():

    @property
    def serie(self): 
        return self._serie

    @serie.setter
    def sala(self, serie): 
        self._serie = serie

class TipoAluno(TipoSala):

    _notas = []
   
    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, notas):
        self._notas = notas

    @property
    def nome(self): 
        return self._nome

    @nome.setter
    def nome(self, nome): 
        self._nome = nome

    @property
    def media(self): 
        return self._media

    @media.setter
    def media(self, media): 
        self._media = media

    def calcMedia(self):
        soma = 0.0
        for indice in range(4):
            soma += self._notas[indice]
        self._media = soma / 4.0

aluno = TipoAluno()

# Rotina para a entrada de dados

print(" CADASTRO DE ALUNO ".center(80, "-"))
print()
aluno.nome = input("Informe o nome ...: ")
aluno.sala = input("Informe a sala ...: ")
aluno.serie = input("Informe a série ..: ")
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
print("Sala .........: {0}".format(aluno.sala))
print("Série ........: {0}".format(aluno.serie))
print()
for indice in range(4):
    print(str(indice + 1) + "a. nota .....: {0:6.2f}".format(aluno.notas[indice]))
print()
print("Média ........: {0:6.2f}".format(float(aluno.media)))
print()
if (aluno.media >= 6.0):
    print("Situação .....: Aprovado")
else:
    print("Situação .....: Reprovado")

enter = input("\nPressione <Enter> para encerrar... ")
