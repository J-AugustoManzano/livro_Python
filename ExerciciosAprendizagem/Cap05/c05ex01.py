varGlobal = "Texto definido de forma: global."

def texto():
  varLocal = "Texto definido de forma: local."
  print(varGlobal)
  print(varLocal)

print("Acesso com a função: texto()")
print()

texto()

print("\nAcesso sem a função: texto()")
print()

print(varGlobal)
print(varLocal)

enter = input("\nPressione <Enter> para encerrar... ")
