import array
import numpy as np

class Exists:
    NOT_EXISTS = 0
    EXISTS = 1
    AVAILABLE = 2


class Item:
    def __init__(self, key, value):
        '''=======Student's code======='''

class HashMap:
    def __init__(self,n,k):
        '''=======Student's code======='''
    
    def hash(self, key):
        '''=======Student's code======='''
    
    def putitem(self, key, value):
        '''=======Student's code======='''
        
    def getCount(self, key):
        '''=======Student's code======='''


class checker:
    def canArray(self, arr : array.array, n, k):
        '''=======Student's code======='''

def main():
    c = checker()

    n = 4
    k = 6
    arr = array.array('h', [9, 7, 5, 3])
    if c.canArray(arr, n, k): # YES
        print("YES")
    else:
        print("NO")
    
    
    n = 6
    k = 10
    arr = array.array('h', [92, 75, 65, 48, 45, 35])
    if c.canArray(arr, n, k): # YES
        print("YES")
    else:
        print("NO")

    n = 4
    k = 10
    arr = array.array('h', [91, 74, 66, 48])
    if c.canArray(arr, n, k): # NO
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()