class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

# Traversal function
def traves(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->")
        curr = curr.Next
    print("None")

# Insertion at given position
def insertion(head, pos, data):
    newnode = Node(data)

    # Case 1: Empty list
    if head is None:
        return newnode

    # Case 2: Insert at beginning
    if pos == 1:
        newnode.Next = head
        return newnode

    # Case 3: Insert at given position
    curr = head
    count = 1
    while count < pos - 1 and curr.Next is not None:
        curr = curr.Next
        count += 1

    newnode.Next = curr.Next
    curr.Next = newnode
    return head

# Deletion at given position
def delete(head, pos):
    if head is None:
        print("List is empty")
        return None

    # Delete first node
    if pos == 1:
        return head.Next

    curr = head
    count = 1
    while count < pos - 1 and curr.Next is not None:
        curr = curr.Next
        count += 1

    if curr.Next is not None:
        curr.Next = curr.Next.Next
    return head

# -----------------------------
# Create linked list: 1 -> 2 -> 3 -> 4
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.Next = n2
n2.Next = n3
n3.Next = n4

print("Original list:")
traves(n1)

# Insert 99 at position 2
insertion(n1, 2, 99)
print("\nAfter inserting 99 at position 2:")
traves(n1)

# Delete node at position 3
delete(n1, 3)
print("\nAfter deleting node at position 3:")
traves(n1)
