import math

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

# Exponenciação
print("%14.10f" % math.pow(2.0,3.0))         # =   8.0000000000
print("%14.10f" % math.pow(2.0,0.0))         # =   1.0000000000

# Radiciação com raiz quadrada
print("%14.10f" % math.sqrt(144))            # =  12.0000000000
print("%14.10f" % math.sqrt(math.sqrt(16)))  # =   2.0000000000

pausa()
