# 해쉬값 보장 hashlib
import hashlib

# SHA-1
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA-256
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)


# 예제
import hashTable

class GoodHashList(hashTable.HashList):
    def get_key(self, data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16)

h1 = GoodHashList()
print(h1.get_key('Dave'))