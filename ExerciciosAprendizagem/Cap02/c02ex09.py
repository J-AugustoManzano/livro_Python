nome = input("Entre seu nome: ")
idade = int(input("Entre dua idade: "))

print()

print("Olá, %s." % nome)
print("você tem %i anos de idade." % idade)

print()

print("Olá, %s" % nome, end="")
print(" você tem %i anos de idade." % idade)

enter = input("\nPressione <Enter> para encerrar... ")
