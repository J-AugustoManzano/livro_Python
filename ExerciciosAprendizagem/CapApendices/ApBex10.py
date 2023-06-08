def cls():
    import subprocess 
    import platform 

    sistema = platform.system()
    if (sistema == "Windows"):
        subprocess.call("cls", shell = True)
    elif (sistema == "Linux" or sistema == "Darwin"):
        subprocess.call("clear", shell = True)

cls()
print("Teste")

enter = input("\nPressione <Enter> para encerrar... ")
