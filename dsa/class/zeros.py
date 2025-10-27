class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(0,n):
            if nums[i] ==0:
                nums[i] = nums[-1]
                i+=1
                
sol =  Solution()
nums = [1,3,4,6,7]
print(sol.moveZeroes(nums))

               
                
                
                