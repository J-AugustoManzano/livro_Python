mes = float(input("Entre um numero equivalente a um MÊS: "))

print()

if (mes == 1):
    print("Janeiro.")
else:
    if (mes == 2):
        print("Fevereiro.")
   else:
       if (mes == 3):
           print("Março.")
       else:
          if (mes == 4):
              print("Abril.")
          else:
              if (mes == 5):
                  print("Maio.")
              else:
                  if (mes == 6):
                      print("Junho.")
                  else:
                      if (mes == 7):
                          print("Julho.")
                     else:
                         if (mes == 8):
                             print("Agosto.")
                         else:
                             if (mes == 9):
                                 print("Setembro.")
                             else:
                                 if (mes == 10):
                                     print("Outubro.")
                                 else:
                                     if (mes == 11):
                                         print("Novembro.")
                                     else:
                                         if (mes == 12):
                                             print("Dezembro.")
                                         else:
                                             if (mes < 1 or mes > 12):
                                                 print("Mês inválido.")
 
enter = input("\nPressione <Enter> para encerrar... ")
