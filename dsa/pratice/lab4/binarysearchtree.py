class Node:
    def __init__(self,Data):
        self.Data = Data
        self.left = None
        self.right = None
def traves(root):
    if root is not None:
        traves(root.left)
        print(root.Data,end="->")
        traves(root.right)
       
def insertion(root,Data):
   
    if root is None:
      return Node(Data)
    if Data< root.Data: 
             root.left = insertion(root.left,Data)
    else:
            root.right = insertion(root.right,Data)
    return root    
n1 = Node(1)  
n2 = Node(2)
n3 = Node(3)  
n4 = Node(4)  
n5 = Node(5)  
n6 = Node(6)    
n7 = Node(7)

n7.left = n5
n7.right = n6
n5.left = n4
n5.right = n3
n6.left = n1
n6.right = n2

traves(n7)
print(insertion(n7,23))
traves(n7)



    
            