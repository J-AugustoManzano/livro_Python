def fatorial(valor):
    if (valor == 0):
        return 1
    else:
        return valor * fatorial(valor - 1)

def somatorio(valor):
    if (valor == 0):
        return 0
    else:
        return valor + somatorio(valor - 1)

n = int(float(input("Entre o valor numérico inteiro: ")))

resposta = fatorial
print("Resultado da fatorial de %d = %d." % (n, resposta(n)))

resposta = somatorio
print("Resultado do somatório de %d = %d." % (n, resposta(n)))

enter = input("\nPressione <Enter> para encerrar... ")
