class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        
        k = 1
        temp = nums[0]
       
        for i in range(1,n):  
         nums[i-1] = nums[i]
        nums[-1] = temp 
        print(nums)
        
sol=Solution()
nums = [1,2,3,4,5]  
print(f"the array befor{nums}") 
sol.rotateArrayByOne(nums)      