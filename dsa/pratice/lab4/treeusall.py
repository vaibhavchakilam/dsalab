class treenode:
    def __init__(self,Data):
        self.right = None
        self.left = None
        self.Data = Data
def preorder(root):
            if root is not None:
                print(root.Data,end="->")
                preorder(root.left)
                preorder(root.right)
def postorder(root):
            if root is not None:            
                postorder(root.left)
                postorder(root.right)  
                print(root.Data,end="->") 
def inorder(root):
            if root is not None:            
                inorder(root.left)
                print(root.Data,end="->")    
                inorder(root.right)  
                             
                             
                
            
        
root =treenode('r') 
n1 =treenode('a')
n2 =treenode('b')
n3 =treenode('c')
n4 =treenode('d')
n5 =treenode('e')
        
root.right = n1
root.left = n2
n1.left =n3
n1.right = n4
n2.left = n5
print(f"preorder is :{preorder(root)}")
print(f"postrder is :{postorder(root)}")
print(f"inorder is :{inorder(root)}")





        
