import numpy as np

class Exists:
    '''=======Student's code======='''

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
    hashmap.setitem(101, "A")
    hashmap.setitem(202, "B")
    hashmap.setitem(303, "C")
    
    print(hashmap.getitem(101))  # A
    print(hashmap.getitem(202))  # B
    print(hashmap.getitem(303))  # C
    
    hashmap.delitem(202)
    print(hashmap.getitem(202))  # None

    hashmap.setitem(303, "D")
    print(hashmap.getitem(303))  # D

if __name__ == "__main__":
    main()