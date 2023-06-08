def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

def linha(caractere = "-"):
    print(caractere * 80)

def centraTexto(texto):
    print(texto.center(80))

def titulo(texto, caractere = "-"):
    linha(caractere)
    centraTexto(texto)
    linha(caractere)

titulo("Estudo de linguagem Python 2018")

pausa()
