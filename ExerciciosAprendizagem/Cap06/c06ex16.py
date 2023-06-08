import hashlib

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

print(hashlib.md5(b"Jose").hexdigest())
print(hashlib.md5(b"Josi").hexdigest())
print(hashlib.md5(b"Augusto").hexdigest())
print(hashlib.md5(b"Augusta").hexdigest())
print(hashlib.md5(b"1").hexdigest())

pausa()
