import locale

locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

def pausa():
  enter = input("\nPressione <Enter> para encerrar... ")

def fv(pmt, i, n, typ = 0):
  import math
  cfv = 0.0
  if (typ < 0 or typ > 1):
    cfv = math.nan
  else:
    cfv = pmt * ((math.pow(1 + i, n) - 1) / i)
    if (typ == 1):
      cfv = pmt * ((math.pow(1 + i, n) - 1) / i) * (1 + i)
  return cfv

PMT = 2000.00
I   = 0.075 # 7.5% (7.5 / 100.0)
N   = 20.0
  
print("Fim do período ......: ", locale.currency(fv(PMT, I, N), grouping = True))
print("Início do período ...: ", locale.currency(fv(PMT, I, N, 1), grouping = True))

pausa()
