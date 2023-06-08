resp = "S";
while (resp.upper() == "S"):
  
  n = int(input("Entre o valor da tabuada: "))
  i = 1
  while (i <= 10):
      r = n * i;
      print("%2d x %2d = %3d" % (n, i, r))
      i = i + 1
  print()
  print("Deseja continuar? ")
  resp = input("Tecle [S] para SIM / qualquer caractere para NAO: ")
  print()
