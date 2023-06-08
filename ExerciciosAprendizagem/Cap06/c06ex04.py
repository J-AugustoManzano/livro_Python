import math

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

# Arredondamento para cima
print("%3d" % math.ceil(2.03))               # =   3
print("%3d" % math.ceil(-2.03))              # =  -2

# Arredondamento para baixo
print("%3d" % math.floor(2.03))              # =   2
print("%3d" % math.floor(-2.03))             # =  -3

# Obter o valor absoluto real
print("%14.10f" % math.fabs(-8.238765))      # =   8.2387650000
print("%14.10f" % math.fabs(-2.03))          # =   2.0300000000

# Obter o resto de divisão de valores reais
print("%14.10f" % math.fmod(5.3,2))          # =   1.3000000000
print("%14.10f" % math.fmod(10.0,3.0))       # =   1.0000000000

# Obter o máximo divisor comum de dois valores inteiros
print("%3d" % math.gcd(12,36))               # =   12
print("%3d" % math.gcd(12,18))               # =    6

pausa()
