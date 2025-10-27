class arraytree:
    def __init__(self):
        self.tree = []

    def findroot(self, postorder, inorder):
        if not postorder or not inorder:
            return None

        self.root = postorder[-1]
        print(self.root)

        mid_of_inorder = inorder.index(self.root)
        left_inorder = inorder[0:mid_of_inorder]  
        right_inorder = inorder[mid_of_inorder+1:len(inorder)]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]  

        leftsubtree = self.findroot(left_postorder, left_inorder)
        rightsubtree = self.findroot(right_postorder, right_inorder)  

        tt = self.tree.append((leftsubtree, self.root, rightsubtree))  

        return self.root
def travis()    

a = arraytree()        
po = [1,2,3,4,5]
ino = [1,4,5,2,3]
a.findroot(po, ino) 


print(tt)
