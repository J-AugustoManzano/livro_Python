# c02ex08.py

''' Projeto .........: c02ex08
    Autor(es) .......: Augusto Manzano
    Data ............: 22/01/2018
    Versão ..........: 1.0
    Revisão .........: 22/01/2018
'''

""" Finalidade

    Este programa ter por finalidade apresentar alguns resultados
    Obtidos a partir do uso do módulo de biblioteca matemática 
    Interna da linguagem Python.
"""

import math # Chamada do módulo de recursos matemáticos

print("2 ^ 3 ............: %10.2f" % math.pow(2, 3))
print("sqrt 25 ..........: %10.2f" % math.sqrt(25))
print("floor 2.10 .......: %10.2f" % math.floor(2.10))
print("ceiling 2.10 .....: %10.2f" % math.ceil(2.10))
print("e ^ 2 ............: %10.2f" % math.exp(2))
print("log2(2) ..........: %10.2f" % math.log2(2))
print("log10(2) .........: %10.2f" % math.log10(2))
print("factorial(5) .....: %10.2f" % math.factorial(5))

enter = input("\nPressione <Enter> para encerrar... ")
