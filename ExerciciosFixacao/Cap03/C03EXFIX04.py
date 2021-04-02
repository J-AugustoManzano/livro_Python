a = int(input("Informe o 1o. valor ....: "))
b = int(input("Informe o 2o. valor ....: "))
c = int(input("Informe o 3o. valor ....: "))

if (a > b):
    a, b = b, a
if (a > c):
    a, c = c, a
if (b > c):
    b, c = c, b

print()
print("1o. valor %i" % a)
print("2o. valor %i" % b)
print("3o. valor %i" % c)

enter = input("\nPressione <Enter> para encerrar... ")
