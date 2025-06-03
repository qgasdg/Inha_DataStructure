import numpy as np
import array

class Exists:
    '''=======Student's code======='''

class Item:
    def __init__(self, key, value):
        '''=======Student's code======='''

class HashMap:
    def __init__(self):
        '''=======Student's code======='''
            
    
    def hash(self, key):
        '''=======Student's code======='''
    def setitem(self, key, value):
        '''=======Student's code======='''

    def getitem(self, key):
        '''=======Student's code======='''

def disjoint(array1 : array.array, n1, array2 : array.array, n2):
    '''=======Student's code======='''

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