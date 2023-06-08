a = float(input("Entre o lado <A>: "))
b = float(input("Entre o lado <B>: "))

print()
print("[1] - Adição")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
print()

opcao = int(input("Escolha uma opção: "))

if (opcao == 1):
    r = a + b
if (opcao == 2):
    r = a - b
if (opcao == 3):
    r = a * b
if (opcao == 4):
    if (b == 0):
      r = 0
    else:
      r = a / b
if (opcao >= 1 and opcao <= 4):
    print("\nO resultado da operação equivale a: %.2f}" % r)
else:
    print("\nOpção inválida.")

enter = input("\nPressione <Enter> para encerrar... ")
