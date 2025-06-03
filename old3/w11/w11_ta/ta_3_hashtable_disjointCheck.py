import numpy as np
import array

class Exists:
    NOT_EXISTS = 0
    EXISTS = 1
    AVAILABLE = 2

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.exists = Exists.NOT_EXISTS

class HashMap:
    def __init__(self):
        self.size = 1000
        self.PrimeNumber = 101
        self.table = np.empty(self.size, dtype=object)
        for i in range(self.size):
            self.table[i] = Item(0,None)
            
    
    def hash(self, key):
        return key % self.PrimeNumber
    
    def setitem(self, key, value):
        index = self.hash(key)
        new_item = Item(key, value)
        
        while self.table[index].exists == Exists.EXISTS:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            index = (index + 1) % self.size
        self.table[index] = new_item
        self.table[index].exists = Exists.EXISTS

    def getitem(self, key):
        index = self.hash(key)
        
        while self.table[index].exists != Exists.NOT_EXISTS:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.size
        return None

def disjoint(array1 : array.array, n1, array2 : array.array, n2):
    hashmap = HashMap()
    
    for i in range(n1):
        hashmap.setitem(array1[i], array1[i])
    for i in range(n2):
        if hashmap.getitem(array2[i]) is not None:
            return True
    return False

def main():
    n1 = 4
    n2 = 4
    array1 = array.array('h', [1, 2, 3, 4])
    array2 = array.array('h', [5, 6, 7, 8])
    
    if disjoint(array1, n1, array2, n2): # No
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()