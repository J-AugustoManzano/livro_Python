import platform
    
print("Sistema .......: ", platform.system())
print("Processador ...: ", platform.machine())
print("Plataforma ....: ", platform.platform())
print("Versão ........: ", platform.version())
print("Release .......: ", platform.release())
print("Padrão ........: ", platform.os.name)

enter = input("\nPressione <Enter> para encerrar... ")
