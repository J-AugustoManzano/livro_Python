a = float(input("Entre o lado <A>: "))
b = float(input("Entre o lado <B>: "))
c = float(input("Entre o lado <C>: "))

print()

if (a < b + c and b < a + c and c < a + b):
    if (a == b and b == c):
        print("Triângulo equilátero.")
    else:
      if (a == b or a == c or c == b):
          print("Triângulo isósceles.")
      else:
          print("Triângulo escaleno.")
else:
    print("Os valores fornecidos não formam um triângulo.")

enter = input("\nPressione <Enter> para encerrar... ")
