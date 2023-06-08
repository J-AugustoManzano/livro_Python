import hashlib

def pausa():
    enter = input("\nPressione <Enter> para encerrar... ")

print(hashlib.blake2b(b"Jose").hexdigest())
print(hashlib.blake2s(b"Jose").hexdigest())
print(hashlib.md5(b"Jose").hexdigest())
print(hashlib.sha1(b"Jose").hexdigest())
print(hashlib.sha224(b"Jose").hexdigest())
print(hashlib.sha256(b"Jose").hexdigest())
print(hashlib.sha3_224(b"Jose").hexdigest())
print(hashlib.sha3_256(b"Jose").hexdigest())
print(hashlib.sha3_384(b"Jose").hexdigest())
print(hashlib.sha3_512(b"Jose").hexdigest())
print(hashlib.sha384(b"Jose").hexdigest())
print(hashlib.sha512(b"Jose").hexdigest())

pausa()
