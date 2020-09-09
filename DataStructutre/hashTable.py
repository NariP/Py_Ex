# 리스트로 구현하는 해쉬

# hash_table=list(0 for i in range(10))



class HashList:

    def __init__(self):
        self.hash_table = list(0 for i in range(8))
        self.description = '리스트로 구현한 해쉬 함수'

    def get_key(self, data):
        return hash(data)

    def hash_function(self, key):
        return key % 8

    def save_data(self, data, value):
        hash_address = self.hash_function(self.get_key(data))
        self.hash_table[hash_address] = value

    def get_data(self, data):
        hash_address = self.hash_function(self.get_key(data))
        return self.hash_table[hash_address]

    def __repr__(self):
        return self.description

if __name__ == "__main__":
    h1 = HashList()
    print(h1.hash_table)
    h1.save_data('Dave', '1234')
    print(h1.hash_table)
    print(h1.get_data('Dave'))