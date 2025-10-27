class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None    

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rare = None

    def push(self, x):
        newnode = Node(x)
        if self.front is None:
            self.front = newnode
            self.rare = newnode
        else:
            self.rare.Next = newnode  
            self.rare = newnode  

    def pop(self):
        if self.isEmpty():
            return -1 
        removed = self.front.Data
        self.front = self.front.Next
        

    def peek(self):
        if self.isEmpty():
            return -1
        return self.front.Data

    def isEmpty(self):
        return 1 if self.front is None else 0
