class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
       
class circularqueue:
    def __init__(self, max_capacity):
        self.front = None  
        self.rare = None  
        self.size = 0     
        self.max_capacity = max_capacity
   
    def isempty(self):
        return self.size == 0

    def isfull(self):
        return self.size == self.max_capacity
    
    def enqueue(self, data):
        if self.isfull():
            print("the queue is full cant enqueue")
            return
        newnode = Node(data)
        if self.front is None:
            self.front = newnode
            self.rare = newnode
            self.rare.Next = self.front
        else:
            self.rare.Next = newnode
            self.rare = newnode
            self.rare.Next = self.front   
        self.size += 1
        print("the enqueue element is " + str(data))

    def dequeue(self):
        if self.isempty():
            print("the queue is empty")    
            return  
        removed = self.front.Data
        if self.front == self.rare:
            self.front = self.rare = None
        else:
            self.front = self.front.Next
            self.rare.Next = self.front   
        print("the removed element is " + str(removed))    
        self.size -= 1 

    def display(self):
        if self.isempty():
            print("the queu is empty")
            return
        
        currentnode = self.front
        while currentnode is not None:
            print(currentnode.Data, end="->")
            currentnode = currentnode.Next
            if currentnode == self.front:
                break 
        print("back to front")
        print("size " + str(self.size))
        
    def get_size(self):
        return self.size


# Test the CircularQueue

cq = circularqueue(3)

print("Is queue empty?", cq.isempty())
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

print("Is queue full?", cq.isfull())

cq.enqueue(40)  # should show full

cq.dequeue()
cq.display()

cq.enqueue(40)  # now space is available
cq.display()

print("Final size of queue:", cq.get_size())
print("Is queue empty?", cq.isempty())
print("Is queue full?", cq.isfull())
