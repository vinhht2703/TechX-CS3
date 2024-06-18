class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]  # [ [] ,  [] , [] , [] , [] , [] , [] ]

    def hashFunction(self, value):
        return value % self.size

    def insert(self, value):
        index = self.hashFunction(value)
        self.table[index].append(value)

    def search(self, value):
        index = self.hashFunction(value)
        items = self.table[index]
        for i in range(len(items)):
            if items[i] == value:
                return "Found"
        return "Not found"

    def delete(self, value):
        index = self.hashFunction(value)
        self.table[index].remove(value)
        
    


# size = 7
lstNumber = [25, 14, 33, 11, 10, 20, 30]

hashTable = HashTable(len(lstNumber))

for number in lstNumber:
    hashTable.insert(number)

print(hashTable.table)
print(hashTable.search(11))  # found
print(hashTable.search(10))  # found
print(hashTable.search(69))  # not found
print(hashTable.delete(10))  # deleted
print(hashTable.delete(69))  # not found
print(hashTable.delete(25))  # deleted
print(hashTable.search(10))  # not found
print(hashTable.table)
