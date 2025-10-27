class stack:
    def __init__(self,data):
        self.data = data
        self.Next = None

def push(head,data):
    newnode = stack(data)
    if head is None:
        return newnode
    newnode.Next =   head
    head = newnode
    return head
def pop(head):
    if head is None:
        return 'is empty'
    deletedelement = head.data
    head = head.Next
    return deletedelement
def travis(head):
    curr =  head
    while curr is not None:
        print(curr.data,end='->')
        curr = curr.Next
    print("null")    
n1 = stack(1)
n2 = stack(2)
n3 = stack(3)
n4 = stack(4)
n5 = stack(5)


n1.Next = n2
n2.Next = n3
n3.Next = n4
n4.Next = n5
travis(n1)
head = push(n1,28)
travis(head)
pop(head)
travis(n1)
    
             