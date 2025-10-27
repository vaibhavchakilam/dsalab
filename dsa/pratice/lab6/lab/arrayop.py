class array():
    def __init__(self):
        self.arr = []
        self.n = int(input("enter the array len: "))
    def print1(self):
     for i in range(0, self.n):
        elements = int(input("enter the elements: "))
        self.arr.append(elements)
     for elements in self.arr:
        print(elements)
    def inseretion(self,val):
        val = int(input("enter the value"))
        self.arr.append(val)
        for elements in self.arr:
         print(elements)
    def delection(self,ind):
        dd = int(input("enter del val"))
        self.arr.pop(ind)
        for elements in self.arr:
         print(elements)
             
         
ar = array()
ar.print1()  
ar.inseretion(8)
ar.delection(4)
        
        