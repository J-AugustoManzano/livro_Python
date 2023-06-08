import math

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

# Arco cosseno
print("%14.10f" % math.acos(-1))                     # =   3.1415926536 
print("%14.10f" % (math.acos(0.5) * 180 / math.pi))  # =  60.0000000000 

# Arco semo
print("%14.10f" % math.asin(-1))                     # =  -1.5707963268
print("%14.10f" % (math.asin(0.5) * 180 / math.pi))  # =  30.0000000000

# Arco tangente
print("%14.10f" % math.atan(0.5))                    # =   0.4636476090
print("%14.10f" % (math.atan(1) * 180 / math.pi))    # =  45.0000000000

# Arco tangente de coordenadas cartesianas
print("%14.10f" % math.atan2(1,1))                   # =   0.7853981634
print("%14.10f" % math.atan2(-1,-1))                 # =  -2.3561944902

# Cosseno
print("%14.10f" % (math.cos(45 * math.pi / 180)))    # =   0.7071067812
print("%14.10f" % math.cos(math.atan (1)))           # =   0.7071067812

# Seno
print("%14.10f" % math.sin(math.pi / 6))             # =   0.5000000000
print("%14.10f" % math.sin(1))                       # =   0.8414709848

# Tangente
print("%14.10f" % math.tan(4))                       # =   1.1578212823
print("%14.10f" % math.tan(math.pi / 4))             # =   1.0000000000

pausa()
