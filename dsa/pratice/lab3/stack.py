class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
        
class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        newnode = Node(data)
        newnode.Next = self.head 
        self.head = newnode
        self.size += 1
    def pop(self):
        popnode = self.head
        self.head = self.head.Next
        self.size +=-1 

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.Data, end=" -> ")
            currentNode = currentNode.Next
        print("Null")  # properly indented here

mystack = stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.traverseAndPrint()
mystack.pop()
mystack.traverseAndPrint()




