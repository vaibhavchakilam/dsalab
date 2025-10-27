class CircularQueue:
    def __init__(self, max_capacity):
        self.queue = [None] * max_capacity
        self.front = -1
        self.rear = -1
        self.max_capacity = max_capacity

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_capacity

        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:
            # only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_capacity

        print(f"Dequeued: {removed}")

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Queue: ", end="")
        i = self.front
        while True:
            print(self.queue[i], end=" -> ")
            if i == self.rear:
                break
            i = (i + 1) % self.max_capacity
        print("(circular)")

    def get_size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.max_capacity - (self.front - self.rear - 1)
# Test the CircularQueue
if __name__ == "__main__":
    cq = CircularQueue(max_capacity=3)

    print("Is queue empty?", cq.is_empty())
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(50)

    cq.display()
    print("Is queue full?", cq.is_full())

    cq.enqueue(40)  # should show full

    cq.dequeue()
    cq.display()

    cq.enqueue(40)
    cq.display()

    print(f"Final size of queue: {cq.get_size()}")
    print("Is queue empty?", cq.is_empty())
    print("Is queue full?", cq.is_full())
