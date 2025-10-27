class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newnode = Node(data)
        if self.rear is None:
            self.front = self.rear = newnode
            self.rear.next = self.front  # circular link
        else:
            self.rear.next = newnode
            self.rear = newnode
            self.rear.next = self.front  # keep it circular

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        # Only one element
        if self.front == self.rear:
            print(f"Dequeued: {self.front.data}")
            self.front = self.rear = None
        else:
            print(f"Dequeued: {self.front.data}")
            self.front = self.front.next
            self.rear.next = self.front  # maintain circular link

    def travis(self):
        if self.front is None:
            print("Queue is empty")
            return

        curr = self.front
        print("Circular Queue:", end=" ")
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.front:
                break
        print("(back to front)")



cq = CircularQueue()
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.travis()

cq.dequeue()
cq.travis()
