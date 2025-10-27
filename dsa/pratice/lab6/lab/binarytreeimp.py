class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
            return

        curr = self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = newnode
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = newnode
                    break
                else:
                    curr = curr.right
    def inorder(self,node):
        if node is not None:
         self.inorder(node.left)
         print(node.data,end='->')
         self.inorder(node.right)
    def preorder(self,node):
        if node is not None:
         print(node.data,end='->')
         self.inorder(node.left)
         self.inorder(node.right)  
    def postorder(self,node):
        if node is not None: 
         self.inorder(node.left)
         self.inorder(node.right) 
         print(node.data,end='->')         
bt = BTree()
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)

print("Inorder Traversal:")
bt.inorder(bt.root) 

print("preorder Traversal:")
bt.preorder(bt.root) 

print("postorder Traversal:")
bt.postorder(bt.root)
        
        
        
        
                        