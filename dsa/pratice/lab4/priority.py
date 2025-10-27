class Node:
    def __init__(self, Data=None, pri=None):
        self.Data = Data
        self.Next = None
        self.pri = pri

def insertion(self, Data, pri):
        newnode = Node(Data, pri)
        if self.Data is None:  # If first node
            self.Data = Data
            self.pri = pri
            return

        if self.Next is None and pri < self.pri:  # New node becomes head
            newnode.Next = Node(self.Data, self.pri)
            self.Data = Data
            self.pri = pri
            return

        if pri < self.pri:  # Insert at head
            newnode.Next = self
            return newnode

        temp = self
        while temp.Next and temp.Next.pri <= pri:
            temp = temp.Next
        newnode.Next = temp.Next
        temp.Next = newnode
        return self

def display(self):
        temp = self
        while temp:
            print(temp.Data, "(", temp.pri, ")", "->", end=" ")
            temp = temp.Next
        print("None")


# Example usage
N = Node()
N1 = insertion("task2", 2) 
N2 = insertion("task1", 1) 
N3 = insertion("task3", 3) 
N4 = insertion("task0", 0) 

display()
