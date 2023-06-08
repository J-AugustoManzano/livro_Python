import math

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

# Cosseno hiperbóilico
print("%14.10f" % math.cosh(60 * math.pi / 180))     # =   1.6002868577
print("%14.10f" % math.cosh(-1))                     # =   1.5430806348

# Seno hiperbólico
print("%14.10f" % math.sinh(45 * math.pi / 180))     # =   0.8686709615
print("%14.10f" % math.sinh(-1))                     # =  -1.1752011936

# Tangente hiperbólica
print("%14.10f" % math.tanh(60 * math.pi / 180))     # =   0.7807144354
print("%14.10f" % math.tanh(4))                      # =   0.9993292997

pausa()
