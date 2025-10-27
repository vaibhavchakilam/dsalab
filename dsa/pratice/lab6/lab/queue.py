class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newnode = Node(data)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = newnode
            return
        self.rear.Next = newnode
        self.rear = newnode

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        self.front = self.front.Next
        if self.front is None:  # Queue became empty
            self.rear = None

    def travis(self):
        curr = self.front
        while curr is not None:
            print(curr.data, end="->")
            curr = curr.Next
        print("null")
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.travis()     # Output: 1->2->3->4->null

q.enqueue(18)
q.travis()     # Output: 1->2->3->4->18->null

q.dequeue()
q.travis()     # Output: 2->3->4->18->null
