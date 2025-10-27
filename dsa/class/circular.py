class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

def travis(head):
    if not head:
        print("List is empty")
        return
    curr = head
    while True:
        print(curr.Data, end="->")
        curr = curr.Next
        if curr == head:
            break
    print("NULL")

def insertion(head, Data, pos):
    newnode = Node(Data)
    if head is None:
        newnode.Next = newnode
        return newnode

    if pos == 1:
        curr = head
        while curr.Next != head:
            curr = curr.Next
        curr.Next = newnode
        newnode.Next = head
        head = newnode
        return head

    curr = head
    count = 1
    while count < pos - 1 and curr.Next != head:
        curr = curr.Next
        count += 1

    newnode.Next = curr.Next
    curr.Next = newnode
    return head

def delection(head, pos):
    if head is None:
        print("List is empty")
        return None

    # If there's only one node
    if head.Next == head and pos == 1:
        return None

    # Deletion at position 1
    if pos == 1:
        last = head
        while last.Next != head:
            last = last.Next
        head = head.Next
        last.Next = head
        return head

    curr = head
    count = 1
    while count < pos - 1 and curr.Next != head:
        curr = curr.Next
        count += 1
    curr.Next = curr.Next.Next
    return head
# Creating circular linked list manually
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.Next = n2
n2.Next = n3
n3.Next = n4
n4.Next = n1
head = n1

travis(head)

# Insert at position 1
head = insertion(head, 44, 1)
travis(head)

# Delete position 3
head = delection(head, 3)
travis(head)
