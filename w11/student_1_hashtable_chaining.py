import numpy as np

class Item:
    def __init__(self, key, value):
        '''=======Student's code======='''

class HashMap:
    def __init__(self):
        self.size = 1000
        '''=======Student's code======='''
    
    def hash(self, key):
        '''=======Student's code======='''
    
    def setitem(self, key, value):
        '''=======Student's code======='''
    
    def getitem(self, key):
        '''=======Student's code======='''
    
    def delitem(self, key):
        '''=======Student's code======='''

def main():
    hashmap = HashMap()
    hashmap.setitem(1, "A")
    hashmap.setitem(2, "B")
    hashmap.setitem(3, "C")
    
    print(hashmap.getitem(1))  # A
    print(hashmap.getitem(2))  # B
    print(hashmap.getitem(3))  # C
    
    hashmap.delitem(2)
    print(hashmap.getitem(2))  # None

    hashmap.setitem(3, "D")
    print(hashmap.getitem(3))  # D

if __name__ == "__main__":
    main()