import hashlib

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

senha = input("Entre uma senha: ")

print("Senha: ", hashlib.md5(senha.encode()).hexdigest())

pausa()
