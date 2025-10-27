class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next = None
    def insertion(head,Data,pos):
        newnode = Node(Data)
        if head is None:
            return newnode
        if pos == 1:
            newnode.Next = head
            return newnode   
        curr = head
        count = 1
        while count<pos-1 and curr.Next is not None:           
            curr = curr.Next
            count= count+1
        newnode.Next = curr.Next
        curr.Next = newnode    
        return head  
def delection(head,pos):
        if head is None :
            return "is empty"
        if head ==1:
            return head.Next
        curr = head
        count = 1
        while count<pos-1 and curr.Next is not None:  
            curr = curr.Next
            count= count+1
        curr.Next =  curr.Next.Next 
        return head  
def travis(head):
       curr = head
       while curr is not None: 
            print(curr.Data,end="->")
            curr = curr.Next  
       print("NULL") 
        
           
node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.Next = node2
node2.Next = node3
node3.Next = node4

travis(node1)
head = Node.insertion(node1,88,2)
travis(head)
head = delection(node1,5)
travis(head)

        
            