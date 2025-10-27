class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        newnode = Node(x)
        newnode.next = self.head
        self.head = newnode

    def pop(self):
        if self.isEmpty():
            return -1  # or None depending on spec
        removed = self.head.data
        self.head = self.head.next
        return removed

    def top(self):
        if self.isEmpty():
            return -1  # or None depending on spec
        return self.head.data

    def isEmpty(self):
        return 1 if self.head is None else 0
