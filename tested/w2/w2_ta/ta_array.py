import array

class ArrayList:
    def __init__(self,n):
        self.capacity = n
        self.array = array.array('h',[0]*self.capacity)
        self.size = 0

    def add(self,idx,item):
        if self.size < self.capacity:
            self.size = self.size+1
        for i in range(self.capacity-2,idx-1,-1):
            self.array[i+1] = self.array[i]
        
        self.array[idx] = item
    
    def remove(self,idx):
        for i in range(idx+1, self.size):
            self.array[i-1] = self.array[i]
        
        self.size = self.size - 1
        self.array[self.size] = 0
    
    def print(self):
        for i in range(0,self.capacity):
            print(self.array[i],end=" ")
        print()    

    def replace(self,idx,item):
        self.array[idx] = item

    def find(self,item):
        for i in range(self.size):
            if self.array[i] == item:
                return i
        return -1
    
    def is_full(self):
        print(self.size == self.capacity)
        

if __name__=='__main__':
    arr = ArrayList(5)
    arr.add(0,6)
    arr.add(1,1)
    arr.add(2,4)
    arr.add(3,7)
    arr.is_full()

    arr.print()
    

    arr.add(4,1)
    arr.replace(2,5)
    arr.is_full()
    arr.print()
 
    arr.add(1,10)
    arr.print()