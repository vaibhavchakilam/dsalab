class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')

def preorder(node):
    if node is None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)


# build the tree
root = node(1)
n1 = node(2)
n2 = node(3)
n3 = node(4)
n4 = node(5)
n5 = node(6)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n2.left = n5

# run traversals
print("Preorder:")
preorder(root)
print("\nPostorder:")
postorder(root)
print("\nInorder:")
inorder(root)
print()
