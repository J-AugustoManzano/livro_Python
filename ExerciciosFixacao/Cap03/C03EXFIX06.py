a = int(input("Informe o 1o. valor ....: "))
b = int(input("Informe o 2o. valor ....: "))
c = int(input("Informe o 3o. valor ....: "))
d = int(input("Informe o 4o. valor ....: "))

print()

if (a % 2 == 0 or a % 3 == 0):
    print("%i" % a)
if (b % 2 == 0 or b % 3 == 0):
    print("%i" % b)
if (c % 2 == 0 or c % 3 == 0):
    print("%i" % c)
if (d % 2 == 0 or d % 3 == 0):
    print("%i" % d)

enter = input("\nPressione <Enter> para encerrar... ")
