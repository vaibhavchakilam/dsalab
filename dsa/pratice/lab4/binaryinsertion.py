class btree:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


def insert(data, root):
    if root is None:
        return btree(data)
    curr = root
    while True:
        if curr.data <= data:
            if curr.right is not None:
                curr = curr.right
            else:
                curr.right = btree(data)
                break
        else:
            if curr.left is not None:
                curr = curr.left
            else:
                curr.left = btree(data)
                break
    return root


def delete(root, target):
    if root is None:
        return None

    if root.data == target:
        return helper(root)

    temp = root
    while root is not None:
        if root.data > target:
            if root.left is not None and root.left.data == target:
                root.left = helper(root.left)
                break
            else:
                root = root.left
        else:
            if root.right is not None and root.right.data == target:
                root.right = helper(root.right)
                break
            else:
                root = root.right
    return temp


def helper(root):
    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    else:
        rightChild = root.right
        lastRight = findLastRight(root.left)
        lastRight.right = rightChild
        return root.left


def findLastRight(root):
    if root.right is None:
        return root
    return findLastRight(root.right)


def search(root, target):
    curr = root
    parent = None
    while curr is not None:
        if curr.data == target:
            print("Node", target, "found!")
            return curr  # return the node (or you can return (parent, curr) if you want parent)
        elif target < curr.data:
            parent = curr
            curr = curr.left
        else:
            parent = curr
            curr = curr.right
    print("Node", target, "not found!")
    return None




def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.data, end=", ")
    inOrderTraversal(root.right)


# ---------------------------
# Create Tree
# ---------------------------
root = btree(13)
node7 = btree(7)
node15 = btree(15)
node3 = btree(3)
node8 = btree(8)
node14 = btree(14)
node19 = btree(19)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

# ---------------------------
# Operations
# ---------------------------
print("Initial Inorder Traversal:")
inOrderTraversal(root)
print("\n")

root = insert(10, root)
print("After inserting 10:")
inOrderTraversal(root)
print("\n")

root = delete(root, 7)
print("After deleting 7:")
inOrderTraversal(root)
print("\n")

search(root, 15)
search(root, 3)
