
class Node:
    def __init__(self,Data):
     self.Data = Data
     self.Next = None
class Solution:
    def deleteHead(self, head):
        self.curr = head
        while head is not None:
            self.curr = self.curr.Next
         
        return self.curr    
    def travising(self,head):
        self.curr = head
        while head is not None:
            print(self.curr.Data,end="->")
            self.curr = self.curr.Next
        return self.curr
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.Next = n2
n2.Next = n3
n3.Next = n4
sol = Solution()
print(sol.deleteHead(n1))
print(sol.travising(n1))

        
        


