class ArrayQueue:#notcircular queue
    def __init__(self, max_capacity):
        self.queue = [None] * max_capacity          # Fixed-size array
        self.front = 0                              # Front index of the queue
        self.rear = -1                              # Rear index (-1 means no element yet)
        self.max_capacity = max_capacity            # Maximum capacity
        self.count = 0                              # Number of elements in the queue

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
            return
        self.rear += 1
        self.queue[self.rear] = value
        self.count += 1
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        removed = self.queue[self.front]
        # Shift elements to the left
        for i in range(self.front, self.rear):
            self.queue[i] = self.queue[i + 1]
       
        self.rear -= 1
        self.count -= 1
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.queue[self.front]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.rear == self.max_capacity - 1

    def size(self):
        return self.count

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue contents:")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

# ✅ Example usage
q = ArrayQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

print("Peek:", q.peek())
print("Is Empty:", q.isEmpty())
print("Is Full:", q.isFull())
print("Size:", q.size())
