import math

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

# Exponencial de um número
print("%14.10f " % math.exp(3.4))             # =  29.9641000474
print("%14.10f " % math.exp(1))               # =   2.7182818285

# Logaritmo de um número
print("%14.10f " % math.log(math.exp(10)))    # =  10.0000000000
print("%14.10f " % math.log(2.0))             # =   0.6931471806

# Logaritmo de um número na base 10
print("%14.10f" % math.log10(3))              # =   0.4771212547
print("%14.10f" % math.log10(math.exp(10)))   # =   4.3429448190

pausa()
