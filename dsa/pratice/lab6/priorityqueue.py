class node:
    def __init__(self,data,priority):
        self.next = None
        self.data = data
        self.priority = priority
class priorityqueue:
    def __init__(self):
        self.front = None
    def enqueue(self,data,priority):
        newnode = node(data,priority)
        if self.front is None:
            self.front = newnode
            return
        if(self.front.priority>priority):
            newnode.next = self.front
            self.front = newnode
            return
        curr = self.front
        while curr.next is not None and curr.next.priority<=priority:
            curr = curr.next
        newnode.next = curr.next 
        curr.next = newnode
            
    def dequeue(self):
        self.front = self.front.next
        return        
            
                
    def travis(self):
        curr = self.front
        while curr :
            print(curr.data,end='->')  
            curr = curr.next
        return 'null'    
    
    
pq = priorityqueue()
n1 = pq.enqueue('a',1)
n2 = pq.enqueue('b',2)
n3 = pq.enqueue('c',3)
print(pq.travis())
print(pq.dequeue())
print(pq.travis())
              
                