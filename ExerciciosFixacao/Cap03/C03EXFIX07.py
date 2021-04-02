a = int(input("Informe o 1o. valor ....: "))
b = int(input("Informe o 2o. valor ....: "))
c = int(input("Informe o 3o. valor ....: "))
d = int(input("Informe o 4o. valor ....: "))
e = int(input("Informe o 5o. valor ....: "))

x = a

if (x < b):
    x = b
if (x < c):
    x = c
if (x < d):
    x = d
if (x < e):
    x = e

y = a

if (y > b):
    y = b
if (y > c):
    y = c
if (y > d):
    y = d
if (y > e):
    y = e

print()
print("Menor valor = %i" % x)
print("Maior valor = %i" % y)

enter = input("\nPressione <Enter> para encerrar... ")
