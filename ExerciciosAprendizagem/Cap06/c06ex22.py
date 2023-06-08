import random
import string

def geraSenha():
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.choice(caracteres) for i in range(8))

for i in range(6):
    print(geraSenha())

enter = input("\nPressione <Enter> para encerrar... ")
