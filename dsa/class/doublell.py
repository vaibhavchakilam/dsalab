class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next = None
        self.prev = None
def traves(head):
    curr = head
    while curr is not None:
        print(curr.Data,end="<->")
        curr = curr.Next
    print("Null")    
def insertion(head,pos,Data):
    newnode = Node(Data)
    if head is None:
        return newnode
    if pos ==1:
        newnode.Next = head
        head.prev = newnode
        head = newnode
        return head
    curr = head
    count = 1
    while count<pos-1 and  curr is not None:
        curr = curr.Next
        count = count+1
    newnode.prev = curr
    newnode.Next = curr.Next 
    curr.Next = newnode   
    return head
def delection(head,pos):
    if head is None :
        return "is empty"
    if pos ==1:
         head = head.Next
         head.prev =None
         return head
    curr = head
    count = 1
    while count <pos-1 and curr.Next is not None:
        curr = curr.Next
        count = count+1
    temp = curr.Next    
    curr.Next = temp.Next
    if temp.Next is not None:
      temp.Next.prev =   curr
    return  head 
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.Next = n2
n2.prev = n1
n2.Next = n3
n3.prev = n2
n3.Next = n4
n4.prev = n3
traves(n1)
head = insertion(n1,3,18)
traves(head)
head = delection(head,5)
traves(head)


    
                