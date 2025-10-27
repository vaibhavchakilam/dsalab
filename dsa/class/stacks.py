class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
       
           self.stack1.append(x)
        

    def pop(self):
        while not self.stack2.empty:
            while  self.stack1:
                self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
        

    def peek(self):
         while not self.stack2.empty:
            while  self.stack1.empty:
                self.stack2.append(self.stack1.pop())
         return  self.stack2[-1]     
       
        

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
        
my = MyQueue()
my.push(1)
my.push(2)
my.push(3)

my.pop()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()