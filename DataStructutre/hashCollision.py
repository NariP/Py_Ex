# 해쉬 충돌
# Chaining 기법 ( 링크드리스트 활용 )
import sys
sys.path.append('C:/Users/nrp/Documents/Py_Ex/DataStructutre/hashCollision.py')
import hashTable

h2 = hashTable.HashList()
h2.save_data('Andy','34567')
print(h2.get_data('Andy'))
print(h2)

# HashList 클래스의 함수를 오버라이딩 함 - 체이닝 기능이 들어가게
class ChainHashList(hashTable.HashList):
    def save_data(self, data, value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(self.get_key(data))
        if self.hash_table[hash_address] != 0:
            for index in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][index][0] == index_key:
                    self.hash_table[hash_address][index][1] = value
                    return
                self.hash_table[hash_address].append([index_key, value])
        else:
            self.hash_table[hash_address] = [[index_key, value]]

    def get_data(self, data):
        index_key = self.get_key(data)
        hash_address = self.has_function(index_key)
        if self.hash_table[hash_address] != 0:
            for index in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][index][0] == index_key:
                    return self.hash_table[hash_address][index][1]
                else:
                    return None
        else:
            return None


# Close hash 기법 - linear probing
class LinearProbingHashList(hashTable.HashList):
    def save_data(self, data, value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(self.get_key(data))
        if self.hash_table[hash_address] != 0:
            for index in range(hash_address, len(self.hash_table)):
                if self.hash_table[index] == 0:
                    self.hash_table[index] = [index_key, value]
                    return
                elif self.hash_table[index][0] == index_key:
                    self.hash_table[index][1] = value
                    return
        else:
            self.hash_table[hash_address] = [index_key, value]

    def get_data(self, data):
        index_key = self.get_key(data)
        hash_address = self.has_function(index_key)
        if self.hash_table[hash_address] != 0:
            for index in range(hash_address, len(self.hash_table)):
                if self.hash_table[index] == 0:
                    return None
                elif self.hash_table[index][0] == index_key:
                    return self.hash_table[index][1]
        else:
            return None
