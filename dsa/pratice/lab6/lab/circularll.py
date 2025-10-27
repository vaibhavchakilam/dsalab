class Node:
    def __init__(self,data):
        self.data = data
        self.pre = None
        self.Next = None
def traves(head):
        curr = head
        while curr is not None:
            print(curr.data,end='<->')
            curr = curr.Next
        return head    
def insertion(head,data,pos):
        newnode = Node(data)
        if head == None:
            newnode.Next = newnode
            return newnode
        if pos ==1:
            newnode.Next = head
            head.Next = newnode
            head = newnode
            return head
        count =1
        curr = head
        while count<pos-1 and curr.Next is not None: 
            curr = curr.Next
            count+=1
        newnode.next = curr.Next
        curr.Next = newnode
        return head
def delection(head,pos):
        if head is None:
            return 'is empty'
        temp = head
        if pos ==1 and head.Next == head:
            return 'None'
        if pos ==1:
            last = head.pre 
            head = head.Next
            head.pre = last
            last.Next = head
            return head
        curr = head 
        count+=1
        while count<pos-1 and curr.Next is not None:
            curr = curr.Next
            count+=1
        curr.Next = curr.Next.Next  
        return head
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.Next = n2
n2.Next = n3
n3.Next = n4
n4.Next = n1
traves(n1)
      
            
            
            
            
                
             
            
            
            
              
                