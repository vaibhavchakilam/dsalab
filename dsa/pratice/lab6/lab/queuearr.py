class queue:
    def __init__(self):
        self.queue = []
    def enqueu(self,data):
        self.queue.append(data)
    def dequeue(self):
        if not self.queue:
            return 'empty'
        print("the queue after ")    
        self.queue.pop(0)
    def display(self):
          print(self.queue)
    def peek(self):
        if not self.queue:
            return 'empty'
        print("the ele is ")
        return  self.queue[0] 
        
              
qu =  queue()
qu.enqueu(1)
qu.enqueu(2)
qu.enqueu(3)
qu.enqueu(4)
qu.display()
qu.dequeue()
qu.display()
print(qu.peek())





               