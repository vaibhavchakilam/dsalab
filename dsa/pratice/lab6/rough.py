class Node:
    def __init__(self,data,priority):
        self.data = data
        self.next  = None
        self.priority = priority
        
class priorityqueue():
     def __init__(self):
        self.front = None
       
            
     def enqueu(self,data,priority): 
         newnode = Node(data,priority)   
         if self.front is  None:
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
         
     def travise(self):
         curr = self.front
         while  curr:
             print(curr.data,end='->')
             curr = curr.next
         return 'Null'
pq = priorityqueue()    
print(pq.travise())
n1 = pq.enqueu('t',1)
print(pq.travise())
n2 = pq.enqueu('v',2)
n3 = pq.enqueu('a',3)
print(pq.travise())
n4 = pq.enqueu('s',3)
print(pq.travise())
print(pq.dequeue())
print(pq.travise())

         
              
                  
         
         
    