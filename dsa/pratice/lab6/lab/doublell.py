class Node:
    def __init__(self,data):
        self.pre = None
        self.Next = None
        self.data = data
        
        
def inseret(data,head,pos):
 newnode = Node(data)
 if head ==None:
     return newnode
 if pos ==1:
     newnode.Next = head
     head.pre = newnode
     head = newnode
     return head
 count =1
 curr = head 
 while count<pos-1 and curr.Next is not None:
     curr = curr.Next
     count+=1
 if curr.Next is not None:     
  newnode.Next = curr.Next
  newnode.pre = curr
  curr.Next = newnode    
 return head

def delete(pos,head):
    if head is None:
        return 'is empty'
    curr = head
    if pos ==1:
       head = head.Next
       return head  
    count=1
    while count<pos-1 and curr.Next is not  None:
        curr = curr.Next
        count +=1
    temp = curr.Next    
    curr.Next = temp.Next
    temp.Next.pre = curr   
    return head
            
def travis(head):
    curr = head
    while curr is not None:
     print(curr.data,end='<->')
     curr = curr.Next
    print( 'Null')
n1 = Node(8)
n2 = Node(7)
n3 = Node(5)
n4 = Node(4)

n1.Next = n2
n2.pre = n1

n2.Next = n3
n3.pre = n2

n3.Next = n4
n4.pre = n3
travis(n1)
head = inseret(33,n1,4)
travis(head)

    
            