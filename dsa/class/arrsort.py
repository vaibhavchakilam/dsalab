class Solution:
    def isSorted(self, nums):
        n = len(nums)
        for i in range(0,n-1):
            if nums[i]>nums[i+1]:
                return False
        else:
                return True
            
sol =  Solution()
nums = [1,2,3,4,5]
print(sol.isSorted(nums))
     