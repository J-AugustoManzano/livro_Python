import const

# Constantes para as cores de texto e fundo

const.black = 0
const.blue = 1
const.green = 2
const.cyan = 3
const.red = 4
const.magenta = 5
const.brown = 6
const.lgray = 7

# Constantes para as cores de texto e fundo

const.dgray = 8
const.lblue = 9
const.lgreen = 10
const.lcyan = 11
const.lred = 12
const.lmagenta = 13
const.yellow = 14
const.white = 15

# Funcionalidades

def normal():
    print("\033[0m")

def clear(): 
    print("\033[2J")

def background(cor): 
    if (cor == 0):
        print("\033[40m", end="")
    if (cor == 1):
        print("\033[44m", end="")
    elif (cor == 2):
        print("\033[42m", end="")
    elif (cor == 3):
        print("\033[46m", end="")
    elif (cor == 4):
        print("\033[41m", end="")
    elif (cor == 5):
        print("\033[45m", end="")
    elif (cor == 6):
        print("\033[43m", end="")
    elif (cor == 7):
        print("\033[47m", end="")

def text(cor): 
    if (cor == 0):
        print("\033[30m", end="")
    if (cor == 1):
        print("\033[34m", end="")
    elif (cor == 2):
        print("\033[32m", end="")
    elif (cor == 3):
        print("\033[36m", end="")
    elif (cor == 4):
        print("\033[31m", end="")
    elif (cor == 5):
        print("\033[35m", end="")
    elif (cor == 6):
        print("\033[33m", end="")
    elif (cor == 7):
        print("\033[37m", end="")
    elif (cor == 8):
        print("\033[1;30m", end="")
    elif (cor == 9):
        print("\033[1;34m", end="")
    elif (cor == 10):
        print("\033[1;32m", end="")
    elif (cor == 11):
        print("\033[1;36m", end="")
    elif (cor == 12):
        print("\033[1;31m", end="")
    elif (cor == 13):
        print("\033[1;35m", end="")
    elif (cor == 14):
        print("\033[1;33m", end="")
    elif (cor == 15):
        print("\033[1;37m", end="")

def position(linha, coluna): 
    if (coluna >= 1 and coluna <= 80 and linha >= 1 and linha <= 24): 
        print("\033[" + str(linha) + ";" + str(coluna) + "H", end="");
    
# Programa principal

clear()
position(1, 1)
print("Teste de padrão de Cores com Código Numérico")

position(3, 1)
background(1)
text(14)
print("Fundo: Azul // Texto: Amarelo")
normal()

position(5, 1)
background(1)
text(7)
print("Fundo: Azul // Texto: Cinza claro")
normal()

position(7, 1)
background(4)
text(14)
print("Fundo: Vermelho // Texto: Amarelo")
normal()

position(9, 1)
background(0)
text(2)
print("Fundo: Preto // Texto: Verde")
normal()

position(11, 1)
background(7)
text(12)
print("Fundo: Cinza claro // Texto: Vermelho claro")
normal()

position(13, 1)
background(const.brown)
text(const.white)
print("Fundo: Marrom // Texto: Branco")
normal()

print()
position(24,1)

enter = input("\nPressione <Enter> para encerrar... ")
