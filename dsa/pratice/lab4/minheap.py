class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [0] * capacity

    def parent(self, i):
        return (i - 1) // 2

    def right(self, i):
        return (2 * i) + 2

    def left(self, i):
        return (2 * i) + 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, data):
        if self.isfull():
            print("Heap is full")
            return
        self.heap[self.size] = data
        curr = self.size
        self.size += 1

        while curr > 0 and self.heap[curr] < self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

    def delete(self):
        if self.isempty():
            print("The heap is empty")
            return
        data = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0)
        return data

    def heapify(self, i):
        smallest = i
        leftchild = self.left(i)
        rightchild = self.right(i)

        if leftchild < self.size and self.heap[leftchild] < self.heap[smallest]:
            smallest = leftchild
        if rightchild < self.size and self.heap[rightchild] < self.heap[smallest]:
            smallest = rightchild

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def display(self):
        print("The Min Heap is:")
        if self.size == 0:
            print("[]")
        else:
            print("[", end="")
            for i in range(self.size):
                print(self.heap[i], end=" ")
            print("]")

    def isfull(self):
        return self.size == self.capacity

    def isempty(self):
        return self.size == 0


# ---- Main code ----
hp = MinHeap(10)
values = [10, 5, 20, 30, 3, 15]
for val in values:
    hp.insert(val)
    hp.display()

while not hp.isempty():
    deleted = hp.delete()
    print("Deleted element:", deleted)
    hp.display()
