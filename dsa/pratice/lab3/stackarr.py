class ArrStack:
    def __init__(self, max_capacity):
        self.top = -1
        self.stack = [None] * max_capacity
        self.max_capacity = max_capacity

    def push(self, value):
        if self.isfull():  
            print("The stack is full.")
            return
        self.top += 1
        self.stack[self.top] = value 
        print(f"Pushed value is {value}")

    def pop(self):
        if self.isempty():
            print("It is empty, so can't pop.")
            return -1
        removed = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        print(f"Popped value is {removed}")
        return removed

    def peek(self):
        if self.isempty():
            print("It is empty, so no top value.")
            return -1
        return self.stack[self.top]

    def isfull(self):
        return self.top == self.max_capacity - 1

    def isempty(self):
        return self.top == -1

    def size(self):
        return self.top + 1  # ✅ Add 1 because index starts at 0

    def display(self):
        if self.isempty():
            print("Stack is empty!")
            return
        print("Stack (top to bottom):")
        for i in range(self.top, -1, -1):
            print(self.stack[i])


# Testing the ArrStack
stack = ArrStack(5)
stack.push(2)
stack.push(4)
stack.push(6)
stack.push(5)
stack.display()

stack.pop()
stack.display()

print("Is Empty?", stack.isempty())   # False
print("Is Full?", stack.isfull())     # False (4 items, max is 5)
print("Current Size:", stack.size())  # Should print 3
print("Top element is:", stack.peek())  # Should print 6
