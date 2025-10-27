class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
        
class queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self, data):
        newnode = Node(data)
        if self.front is None:
         self.front = newnode
         self.rare = newnode
        else:
         self.rare.Next = newnode  
         self.rare = newnode  
       
    def dequeue(self):
        popnode = self.front
        self.front = self.front.Next
      

    def traverseAndPrint(self):
        currentNode = self.front
        while currentNode:
            print(currentNode.Data, end=" -> ")
            currentNode = currentNode.Next
        print("Null")  # properly indented here

myqueue = queue()
myqueue.enqueue('A')
myqueue.enqueue('B')
myqueue.enqueue('C')
myqueue.traverseAndPrint()
myqueue.dequeue()
myqueue.traverseAndPrint()




