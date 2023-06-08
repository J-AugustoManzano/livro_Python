valor1 = 1
valor2 = 10
valor3 = 100
valor4 = 26.1965

print("|%d|" % valor1)
print("|%d|" % valor2)
print("|%d|" % valor3)
print()

print("|%3d|" % valor1)
print("|%3d|" % valor2)
print("|%3d|" % valor3)
print()

print("|%-3d|" % valor1)
print("|%-3d|" % valor2)
print("|%-3d|" % valor3)
print()

print("|%03d|" % valor1)
print("|%03d|" % valor2)
print("|%03d|" % valor3)
print()

print("|%6.0f|" % valor4)
print("|%6.1f|" % valor4)
print("|%6.2f|" % valor4)

enter = input("\nPressione <Enter> para encerrar... ")
