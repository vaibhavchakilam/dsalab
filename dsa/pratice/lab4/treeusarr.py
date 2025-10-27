class arraytree():
    def __init__(self,elements):
        self.tree =elements
    def preorder(self,index = 0):
      if index<len(self.tree) and self.tree[index] is not None:
        print(self.tree[index],end="->")   
        self.preorder(2 * index+1 ) 
        self.preorder(2 * index+2 ) 
    def postorder(self,index = 0):
      if index<len(self.tree) and self.tree[index] is not None: 
        self.postorder(2 * index+1 ) 
        self.postorder(2 * index+2 )  
        
        print(self.tree[index],end="->")  
    def inorder(self,index = 0):
      if index<len(self.tree) and self.tree[index] is not None: 
        self.inorder(2 * index+1 ) 
        print(self.tree[index],end="->")  
        self.inorder(2 * index+2 )        
    def getnode(self,index):
        return self.tree[index]        
elements = ['r', 'a', 'b', 'c', 'd', 'e']
tree = arraytree(elements)

# Accessing root.right.left = index 5
print("Node at root.right.left:", tree.getnode(4))  # Output: e
# Preorder traversal
print("Preorder traversal:")
tree.preorder()   
print("Postorder traversal:")
tree.postorder()
print("inorder traversal:")
tree.inorder()     