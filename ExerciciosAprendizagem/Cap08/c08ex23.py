def listaDici(**dicionario):
    for i, j in dicionario.items():
        print(i, " = ", j)

dicionario = {str(10):0, str(20):2, str(30):4, str(40):6, str(50):8}

listaDici(**dicionario)

enter = input("\nPressione <Enter> para encerrar... ")
